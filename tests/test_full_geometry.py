import hashlib
import io

import trimesh

from test_workflow import client,create_job


def test_full_clay_preserves_source_faces_and_uses_cached_derivative(client):
    job=create_job(client)
    folder=client.app.state.config.jobs/job['id']
    source=folder/'model.glb'
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    response=client.get(job['result']['urls']['full_clay'])
    assert response.status_code==200
    mesh=trimesh.load(io.BytesIO(response.content),file_type='glb',force='mesh',process=False)
    assert len(mesh.faces)==job['result']['metrics']['faces']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before
    derivative=folder/'model-clay-full.glb'
    modified=derivative.stat().st_mtime_ns
    assert client.get(job['result']['urls']['full_clay']).content==response.content
    assert derivative.stat().st_mtime_ns==modified
    refined=client.post('/api/jobs/'+job['id']+'/refine',json={}).json()
    assert refined['full_comparison_url']==refined['comparison_url']+'&full=1'
