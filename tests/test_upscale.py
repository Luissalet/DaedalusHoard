import hashlib
from pathlib import Path

from fastapi.testclient import TestClient
from daedalus.api import create_app
from daedalus.worker import prepare_input
from test_workflow import create_job,fake_runner,wait_job,image_bytes

def test_upscale_reuses_native_parent_and_preserves_versions(tmp_path):
    captured=[]
    def runner(spec,event,cancel):
        captured.append(spec.copy())
        return fake_runner(spec,event,cancel)
    with TestClient(create_app(tmp_path,runner=runner),base_url='http://127.0.0.1') as client:
        original=create_job(client)
        folder=tmp_path/'jobs'/original['id']
        assert client.post(f'/api/jobs/{original["id"]}/upscale',json={}).status_code==409
        (folder/'latents.pt').write_bytes(b'fixture: runner does not load weights')
        original_bytes=(folder/'model.glb').read_bytes()
        token=(tmp_path/'mcp-token').read_text().strip()
        response=client.post('/api/agent/call',headers={'Authorization':'Bearer '+token},json={
            'name':'model_upscale','arguments':{'job_id':original['id'],'steps':19,'seed':27}})
        assert response.status_code==200,response.text
        upscale=wait_job(client,response.json()['result']['id'])
        assert upscale['kind']=='upscale' and upscale['parent_id']==original['id']
        assert upscale['params']=={'resolution':1024,'steps':19,'seed':27}
        assert captured[-1]['source_latent']==str(folder/'latents.pt')
        assert captured[-1]['resolution']==1024
        assert (folder/'model.glb').read_bytes()==original_bytes
        assert client.get('/api/jobs/'+original['id']).json()['result']==original['result']
        assert len(client.get('/api/jobs/'+upscale['id']+'/versions').json()['versions'])==2
        assert client.post(f'/api/jobs/{upscale["id"]}/upscale',json={}).status_code==409
        # Refining the enlarged version keeps its newly generated PBR source.
        refined=client.post(f'/api/jobs/{upscale["id"]}/refine',json={'backend':'ultra'}).json()
        wait_job(client,refined['id'])
        assert captured[-1]['material_source']==str(tmp_path/'jobs'/upscale['id'])

def test_upscale_copies_prepared_reference_without_changing_alpha(tmp_path):
    source=tmp_path/'source.png';source.write_bytes(image_bytes())
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    out=tmp_path/'version';out.mkdir()
    spec={'kind':'upscale','image':str(source),'output_dir':str(out)}
    prepare_input(spec)
    assert Path(spec['image'])==out/'input.png'
    assert (out/'input.png').read_bytes()==source.read_bytes()
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before
