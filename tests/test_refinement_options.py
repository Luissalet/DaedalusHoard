import hashlib
import json
from pathlib import Path

import numpy as np
import pytest
import trimesh
from fastapi.testclient import TestClient

from daedalus.api import create_app
from daedalus.worker import align_refinement_input,restore_refinement_pose,attach_progress
from test_workflow import create_job,fake_runner,wait_job

def test_ultra_options_reach_same_worker_from_agent_api(tmp_path):
    captured=[]
    def runner(spec,event,cancel):
        captured.append(spec.copy())
        return fake_runner(spec,event,cancel)
    with TestClient(create_app(tmp_path,runner=runner),base_url='http://127.0.0.1') as client:
        original=create_job(client)
        token=(tmp_path/'mcp-token').read_text().strip()
        response=client.post('/api/agent/call',headers={'Authorization':'Bearer '+token},json={
            'name':'model_refine','arguments':{'job_id':original['id'],'backend':'ultra','tokens':32768,'steps':63}})
        assert response.status_code==200,response.text
        child=wait_job(client,response.json()['result']['id'])
        assert child['params']['alignment_degrees']==90
        spec=captured[-1]
        assert (spec['backend'],spec['tokens'],spec['steps'])==('ultra',32768,63)
        assert child['parent_id']==original['id']
        assert client.get('/api/jobs/'+original['id']).json()['result']==original['result']
        legacy=client.post(f'/api/jobs/{original["id"]}/refine',json={'tokens':2048}).json()
        assert legacy['params']['backend']=='detail' and legacy['params']['alignment_degrees']==0
        assert client.post(f'/api/jobs/{original["id"]}/refine',json={'backend':'detail','tokens':32768}).status_code==400

@pytest.mark.parametrize('degrees',[90,180,270])
def test_alignment_copies_input_and_restores_output_in_original_frame(tmp_path,degrees):
    source=tmp_path/'original.glb'
    mesh=trimesh.creation.box(extents=[1,2,3]);mesh.apply_translation([.2,.3,.4]);mesh.export(source)
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    output=tmp_path/'version';output.mkdir()
    spec={'kind':'refine','mesh':str(source),'output_dir':str(output),'alignment_degrees':degrees}
    transform=align_refinement_input(spec)
    aligned=trimesh.load(spec['mesh'],force='mesh',process=False)
    np.savez_compressed(output/'refined.npz',vertices=aligned.vertices,faces=aligned.faces)
    restore_refinement_pose(output,transform)
    restored=trimesh.load(output/'refined.glb',force='mesh',process=False)
    np.testing.assert_allclose(restored.bounds,mesh.bounds,atol=2e-7)
    assert hashlib.sha256(source.read_bytes()).hexdigest()==digest
    assert Path(spec['mesh']).parent==output
    assert json.loads((output/'alignment.json').read_text())['original_sha256']==digest

def test_ultra_scheduler_event_can_be_wrapped_for_progress():
    from types import SimpleNamespace
    events=[]
    engine=SimpleNamespace(event=lambda name,**data:events.append((name,data)))
    attach_progress(engine,'refine',512)
    engine.event('scheduler',scheduler='ascending rectified Euler',steps=50)
    assert events[0][1]['scheduler']=='ascending rectified Euler'
