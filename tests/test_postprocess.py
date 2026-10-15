import hashlib
from pathlib import Path

import numpy as np
from PIL import Image
import pytest
import trimesh
from fastapi.testclient import TestClient

from daedalus.api import create_app
from daedalus.geometry.postprocess import Appearance,run
from test_workflow import create_job,fake_runner,wait_job


def test_repair_closes_boundaries_preserves_parts_and_original(tmp_path):
    first=trimesh.creation.icosphere(subdivisions=2)
    second=first.copy();second.apply_translation([3,0,0])
    first.update_faces(np.arange(len(first.faces))<len(first.faces)-2)
    source=trimesh.util.concatenate([first,second]);path=tmp_path/'source.glb';source.export(path)
    before=hashlib.sha256(path.read_bytes()).hexdigest()
    output=tmp_path/'repaired';output.mkdir()
    result=run({'kind':'repair','mesh':str(path),'source_folder':str(tmp_path),
        'output_dir':str(output),'detail_faces':None},lambda *args:None)
    assert result['processing']['closure_verified']
    assert result['processing']['before']['boundary_edges']>0
    assert result['processing']['after']['boundary_edges']==0
    assert result['processing']['after']['components']==2
    assert hashlib.sha256(path.read_bytes()).hexdigest()==before
    largest=tmp_path/'largest';largest.mkdir()
    kept=run({'kind':'repair','mesh':str(path),'source_folder':str(tmp_path),'output_dir':str(largest),
        'detail_faces':None,'method':'volume','voxel_resolution':128,'remove_small_components':True},lambda *args:None)
    assert kept['processing']['after']['components']==1
    repaired=trimesh.load(output/'model.glb',force='mesh',process=True)
    assert repaired.is_watertight and repaired.is_volume
    assert result['execution']=='CPU' and result['gpu_leases']==0


def test_game_budget_and_materials_use_generated_coordinate_frame(tmp_path):
    source=trimesh.creation.icosphere(subdivisions=2);source.export(tmp_path/'source.glb')
    coords=np.array([[3,10,20],[20,10,3]],dtype=np.int32)
    attrs=np.array([[1,0,0,.3,.6,1],[0,0,1,.3,.6,1]],dtype=np.float32)
    np.savez(tmp_path/'pbr-voxels.npz',coords=coords,attributes=attrs,resolution=32)
    appearance=Appearance(source,tmp_path)
    raw=(coords+.5)/32-.5
    assert np.allclose(appearance.sample(raw[:,[1,2,0]]),attrs)
    # Constant six-channel material makes atlas pixels and GLB PBR independently checkable.
    np.savez(tmp_path/'pbr-voxels.npz',coords=coords,attributes=np.tile(attrs[0],(2,1)),resolution=32)
    output=tmp_path/'game';output.mkdir()
    result=run({'kind':'optimize','mesh':str(tmp_path/'source.glb'),'source_folder':str(tmp_path),
        'output_dir':str(output),'material_source':str(tmp_path),'target_faces':100,'texture_size':512},lambda *args:None)
    model=trimesh.load(output/'model.glb',force='mesh',process=False)
    assert len(model.faces)<=100 and len(model.vertices)<len(model.faces)*3
    assert result['processing']['budget_met']
    assert model.visual.kind=='texture' and len(model.visual.uv)==len(model.vertices)
    assert Image.open(output/'base-color.png').size==(512,512)
    mr=np.asarray(Image.open(output/'metallic-roughness.png'))
    assert abs(int(mr[256,256,1])-153)<=1 and abs(int(mr[256,256,2])-76)<=1
    assert model.visual.material.metallicFactor==1


def test_processing_mcp_api_versions_and_no_gpu_reservation(tmp_path,monkeypatch):
    with TestClient(create_app(tmp_path,runner=fake_runner),base_url='http://127.0.0.1') as client:
        original=create_job(client)
        before=(tmp_path/'jobs'/original['id']/'model.glb').read_bytes()
        manager=client.app.state.manager;manager.runner=manager.run_native
        def forbidden_lease(*args,**kwargs):raise AssertionError('CPU postprocessing must not reserve a GPU')
        monkeypatch.setattr('daedalus.jobs.lease',forbidden_lease)
        token=(tmp_path/'mcp-token').read_text().strip()
        response=client.post('/api/agent/call',headers={'Authorization':'Bearer '+token},json={
            'name':'model_repair','arguments':{'job_id':original['id'],'detail_faces':None,'voxel_resolution':128}})
        repaired=wait_job(client,response.json()['result']['id'],timeout=30)
        assert repaired['kind']=='repair' and repaired['parent_id']==original['id']
        assert repaired['result']['processing']['method']=='voxel volume reconstruction'
        assert repaired['result']['processing']['closure_verified']
        response=client.post('/api/jobs/'+repaired['id']+'/optimize',json={'target_faces':100,'texture_size':512})
        game=wait_job(client,response.json()['id'],timeout=30)
        assert game['kind']=='optimize' and game['parent_id']==repaired['id']
        assert game['result']['execution']=='CPU' and game['result']['gpu_leases']==0
        assert len(client.get('/api/jobs/'+game['id']+'/versions').json()['versions'])==3
        assert (tmp_path/'jobs'/original['id']/'model.glb').read_bytes()==before
        assert client.post('/api/jobs/'+original['id']+'/optimize',json={'target_faces':0}).status_code==422


def test_discarded_materials_stay_discarded_through_processing_chain(tmp_path):
    def fixture(spec,event,cancel):
        folder=Path(spec['output_dir']);mesh=trimesh.creation.icosphere(subdivisions=1)
        mesh.visual.vertex_colors=[102,102,102,255];mesh.export(folder/'model.glb')
        if spec['kind']=='generate':
            np.savez(folder/'pbr-voxels.npz',coords=np.array([[0,0,0]]),
                attributes=np.array([[1,0,0,.5,.1,1]]),resolution=1)
        return {'files':{'glb':'model.glb','full_glb':'model.glb'},
                'materials':'generated' if spec['kind']=='generate' else 'none'}
    with TestClient(create_app(tmp_path,runner=fixture),base_url='http://127.0.0.1') as client:
        original=create_job(client)
        refined=wait_job(client,client.post('/api/jobs/'+original['id']+'/refine',
            json={'transfer_materials':False}).json()['id'])
        manager=client.app.state.manager;manager.runner=manager.run_native
        parent=refined
        for kind,params in [('repair',{'detail_faces':None,'method':'surface'}),
                            ('optimize',{'target_faces':100,'texture_size':512}),
                            ('optimize',{'target_faces':100,'texture_size':512})]:
            parent=wait_job(client,client.post('/api/jobs/'+parent['id']+'/'+kind,json=params).json()['id'],timeout=30)
            assert parent['result']['materials']=='none'
        pixels=np.asarray(Image.open(tmp_path/'jobs'/parent['id']/'base-color.png'))
        assert np.allclose(pixels[:,:,:3],102,atol=1)
        assert parent['result']['processing']['material_method']=='nearest source vertex color'


def test_volume_reconstruction_preserves_large_hole_parts_and_coordinate_frame(tmp_path):
    torus=trimesh.creation.torus(major_radius=.6,minor_radius=.2)
    torus.update_faces(np.arange(len(torus.faces))<len(torus.faces)-3)
    part=trimesh.creation.icosphere(subdivisions=1,radius=.1);part.apply_translation([2,0,0])
    source=trimesh.util.concatenate([torus,part]);path=tmp_path/'source.glb';source.export(path)
    before=hashlib.sha256(path.read_bytes()).hexdigest();output=tmp_path/'volume';output.mkdir()
    result=run({'kind':'repair','mesh':str(path),'source_folder':str(tmp_path),'output_dir':str(output),
        'detail_faces':None,'method':'volume','voxel_resolution':128},lambda *args:None)
    model=trimesh.load(output/'model.glb',force='mesh',process=True)
    assert model.is_watertight and model.is_volume and model.is_winding_consistent
    assert len(model.split())==2
    # Torus plus sphere retain one tunnel: Euler0 + Euler2.
    assert model.euler_number==2
    pitch=result['processing']['voxel_pitch_normalized']
    assert np.max(np.abs(model.bounds-source.bounds))<3*pitch
    assert hashlib.sha256(path.read_bytes()).hexdigest()==before
