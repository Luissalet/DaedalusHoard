def tool(name,description,properties=None,required=None):
    return {'name':name,'description':description,'inputSchema':{'type':'object','properties':properties or {},'required':required or []}}

JOB={'job_id':{'type':'string','description':'ID of a job returned by this Hoard'}}
TOOLS=[
 tool('image_import','Import a local reference image into Daedalus.',{'path':{'type':'string'}},['path']),
 tool('model_generate','Queue real image-to-3D generation distributed across four GPUs. Returns a job ID; inspect its status.',
      {'image_id':{'type':'string'},'title':{'type':'string'},'resolution':{'type':'integer','enum':[512,1024],'default':512},
       'seed':{'type':'integer','default':42},'remove_background':{'type':'boolean','default':True}},['image_id']),
 tool('model_refine','Create a separate refined version of a completed model. Improvement is not guaranteed; compare with the original.',
      {**JOB,'tokens':{'type':'integer','enum':[2048,8192],'default':2048},'seed':{'type':'integer','default':42},
       'transfer_materials':{'type':'boolean','default':True}},['job_id']),
 tool('jobs_list','List persisted jobs and their actual results.'),
 tool('job_get','Read generation/refinement progress, files and geometry measurements.',JOB,['job_id']),
 tool('job_cancel','Cancel this queued or running job; never stops another model service.',JOB,['job_id']),
 tool('model_versions','List originals and later versions for the same reference image.',JOB,['job_id']),
 tool('model_rename','Rename a saved job.',{**JOB,'title':{'type':'string'}},['job_id','title']),
 tool('model_export','Export GLB (meters), STL or PLY (millimeters), with an explicit longest-side size.',
      {**JOB,'format':{'type':'string','enum':['glb','stl','ply'],'default':'glb'},'size_mm':{'type':'number','default':100},
       'full':{'type':'boolean','default':False}},['job_id']),
 tool('models_status','Read local weight availability and the actual four GPU inventory.'),
 tool('models_configure','Set the folder containing the generator/ and refiner/ weights; does not download or load a model.',
      {'model_dir':{'type':'string'}},['model_dir'])]
