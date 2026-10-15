# Local model files

Default Windows store: `D:/LocalAI/HoardStorage/daedalus-models`.

Generator: Comfy-Org/TRELLIS2 revision `430a9d09b2416687018c8fe8edced2ad4858a439`.

- `generator/diffusion_models/trellis_2_bf16.safetensors`
- `generator/clip_vision/dino_v3_vit_l.safetensors`
- `generator/vae/trellis_2_shape_vae_bf16.safetensors`
- `generator/vae/trellis_2_texture_vae_bf16.safetensors`
- `generator/pipeline.json` (published model configuration)

Refiner: VAST-AI/DetailGen3D revision `ff2fac7768babe768bb73d03e998f80a397a3454`.

- `refiner/transformer/{config.json,diffusion_pytorch_model.safetensors}`
- `refiner/vae/{config.json,diffusion_pytorch_model.safetensors}`
- `refiner/image_encoder_1/{config.json,model.safetensors}`
- `refiner/feature_extractor_1/preprocessor_config.json`
- `refiner/scheduler/scheduler_config.json`
- `refiner/noise_scheduler/scheduler_config.json`

Alternative refiner: project-linked `infinith/UltraShape` revision `5aeb21a7185d39f042d02b2695802f125a6f5159`.

- `ultra/ultrashape_v1.pt` (7,366,231,254 bytes)
- `ultra/weights-proof.json` (revision, SHA256 and source)

The Ultra weight repository is tagged Apache-2.0 but names a Hunyuan3D-2.1 base, while the code repository has geographic restrictions. Preserve those distinct signals; see `ULTRA-PROVENANCE.md`. No unrestricted redistribution or legal clearance is claimed.

The tested local store keeps the upstream licenses and weight provenance proofs. Approximately 26 GB of files including Ultra, plus the Python/CUDA runtime. Preparing the original store used hardlinks when the immutable source and destination were on the same volume; Ultra is a separate hash-verified download. Runtime reads only this own store. Outputs and peak RAM usage depend strongly on resolution. Weights are not committed to the application repository.
