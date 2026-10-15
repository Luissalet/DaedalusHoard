import io
import json
from pathlib import Path
import threading
import time

from fastapi.testclient import TestClient
from PIL import Image
import pytest
import trimesh
from hoard_link import proc
from daedalus.api import create_app
from daedalus.store import Store

def image_bytes():
    output=io.BytesIO()
    Image.new('RGBA',(32,24),(50,100,150,255)).save(output,format='PNG')
    return output.getvalue()

def fake_runner(spec,event,cancel):
    event({'stage':'generating_shape','progress':.5})
    folder=Path(spec['output_dir'])
    mesh=trimesh.creation.box()
    mesh.export(folder/'model.glb')
    return {'files':{'glb':'model.glb','full_glb':'model.glb','clay':'model.glb'},
            'metrics':{'faces':12,'vertices':8,'watertight':True,'preview_faces':12},'seconds_total':.1}

def wait_job(client,identity,states={'complete'},timeout=5):
    deadline=time.monotonic()+timeout
    while time.monotonic()<deadline:
        result=client.get('/api/jobs/'+identity).json()
        if result['status'] in states:
            return result
        time.sleep(.01)
    raise AssertionError(result)

@pytest.fixture
def client(tmp_path):
    app=create_app(tmp_path,runner=fake_runner)
    with TestClient(app,base_url='http://127.0.0.1') as client:
        yield client

def create_job(client):
    response=client.post('/api/images',files={'file':('pieza.png',image_bytes(),'image/png')})
    assert response.status_code==200,response.text
    image=response.json()
    response=client.post('/api/jobs',json={'image_id':image['id'],'resolution':512,'seed':42,'title':'Pieza'})
    assert response.status_code==200,response.text
    return wait_job(client,response.json()['id'])

def test_generation_refinement_preserves_original_and_versions(client):
    original=create_job(client)
    response=client.post('/api/jobs/'+original['id']+'/refine',json={'tokens':8192})
    refined=wait_job(client,response.json()['id'])
    assert refined['parent_id']==original['id']
    assert client.get('/api/jobs/'+original['id']).json()['result']==original['result']
    versions=client.get('/api/jobs/'+refined['id']+'/versions').json()['versions']
    assert {job['id'] for job in versions}=={original['id'],refined['id']}

def test_export_scale_matches_glb_meters_and_stl_millimeters(client,tmp_path):
    job=create_job(client)
    for format,expected in [('glb',.12),('stl',120),('ply',120)]:
        response=client.get(f'/api/jobs/{job["id"]}/export',params={'format':format,'size_mm':120})
        assert response.status_code==200,response.text
        path=tmp_path/f'mesh.{format}'
        path.write_bytes(response.content)
        mesh=trimesh.load(path,force='mesh')
        assert max(mesh.extents)==pytest.approx(expected,rel=1e-5)
    for value in [0,-1,'nan','inf']:
        assert client.get(f'/api/jobs/{job["id"]}/export',params={'size_mm':value}).status_code==400

def test_cancel_running_job_cannot_be_resurrected_by_late_progress(tmp_path):
    started=threading.Event()
    def runner(spec,event,cancel):
        event({'stage':'loading_models','progress':.1})
        started.set()
        assert cancel.wait(3)
        event({'stage':'generating_shape','progress':.8})
        return {'files':{}}
    app=create_app(tmp_path,runner=runner)
    with TestClient(app,base_url='http://127.0.0.1') as client:
        image=client.post('/api/images',files={'file':('x.png',image_bytes(),'image/png')}).json()
        job=client.post('/api/jobs',json={'image_id':image['id']}).json()
        assert started.wait(3)
        client.post(f'/api/jobs/{job["id"]}/cancel')
        final=wait_job(client,job['id'],{'cancelled'})
        assert final['result'] is None

def test_cancel_queued_job_does_not_start(tmp_path):
    started=threading.Event()
    release=threading.Event()
    calls=[]
    def runner(spec,event,cancel):
        calls.append(spec['job_id'])
        started.set()
        while not release.wait(.01):
            if cancel.is_set():
                raise proc.Cancelled()
        return fake_runner(spec,event,cancel)
    app=create_app(tmp_path,runner=runner)
    with TestClient(app,base_url='http://127.0.0.1') as client:
        image=client.post('/api/images',files={'file':('x.png',image_bytes(),'image/png')}).json()
        first=client.post('/api/jobs',json={'image_id':image['id']}).json()
        assert started.wait(3)
        second=client.post('/api/jobs',json={'image_id':image['id']}).json()
        client.post(f'/api/jobs/{second["id"]}/cancel')
        release.set()
        wait_job(client,first['id'])
        assert client.get('/api/jobs/'+second['id']).json()['status']=='cancelled'
        assert calls==[first['id']]

def test_recovery_preserves_completed_files_and_marks_unfinished(tmp_path):
    store=Store(tmp_path/'state.db')
    image=store.add_image('x','x',1,1)
    done=store.create('generate',image['id'],'done',{})
    store.update(done['id'],status='running')
    store.finish(done['id'],{'files':{'glb':'original.glb'}})
    active=store.create('generate',image['id'],'active',{})
    store.update(active['id'],status='running')
    store.recover()
    assert store.job(active['id'])['status']=='interrupted'
    assert store.job(done['id'])['result']['files']['glb']=='original.glb'

def test_agent_and_browser_share_jobs_and_reject_missing_images(client):
    token=(client.app.state.config.data/'mcp-token').read_text().strip()
    response=client.post('/api/agent/call',json={'name':'jobs_list'})
    assert response.status_code==401
    job=create_job(client)
    response=client.post('/api/agent/call',headers={'Authorization':'Bearer '+token},json={'name':'job_get','arguments':{'job_id':job['id']}})
    assert response.json()['result']['id']==job['id']
    assert client.post('/api/jobs',json={'image_id':'missing'}).status_code==404
    assert client.get('/api/jobs/missing').status_code==404
    assert client.get(f'/api/jobs/{job["id"]}/files/engine.log').status_code==404

def test_restart_does_not_steal_active_data_directory(client):
    other=create_app(client.app.state.config.data,runner=fake_runner)
    with pytest.raises(RuntimeError,match='instancia'):
        with TestClient(other,base_url='http://127.0.0.1'):
            pass

def test_concurrent_browser_and_agent_settings_keep_valid_configuration(client,tmp_path):
    from concurrent.futures import ThreadPoolExecutor
    folders=[tmp_path/'models-a',tmp_path/'models-b']
    for folder in folders:
        folder.mkdir()
    token=(client.app.state.config.data/'mcp-token').read_text().strip()
    def save(index):
        body={'model_dir':str(folders[index%2])}
        if index%2:
            response=client.post('/api/agent/call',headers={'Authorization':'Bearer '+token},
                                 json={'name':'models_configure','arguments':body})
            assert response.status_code==200,response.text
            return response.json()['result']['model_dir']
        response=client.patch('/api/settings',json=body)
        assert response.status_code==200,response.text
        return response.json()['model_dir']
    with ThreadPoolExecutor(max_workers=8) as pool:
        results=list(pool.map(save,range(32)))
    assert results==[str(folders[index%2]) for index in range(32)]
    saved=json.loads((client.app.state.config.data/'settings.json').read_text())
    assert saved['model_dir']==client.get('/api/settings').json()['model_dir']
