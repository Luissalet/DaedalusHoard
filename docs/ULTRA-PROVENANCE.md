# Ultra refinement provenance

Weights: official project-linked Hugging Face repository `infinith/UltraShape`, pinned revision `5aeb21a7185d39f042d02b2695802f125a6f5159`. File `ultrashape_v1.pt`, 7,366,231,254 bytes, SHA256 `c96ae010c4169597fd0006dcb08056bf6104a1fca249b10fed7ddded324c3f0f`. The original checkpoint remains unchanged in the local model store. Safe tensor-only loading uses `weights_only=True`; no upstream pickled classes execute.

## License distinction

The published weight repository labels these weights Apache-2.0 and identifies a Hunyuan3D-2.1 base. Its model card and API metadata are preserved here. The separate code repository `PKU-YuanGroup/UltraShape-1.0`, reference revision `5e8dcef05df101ab00ab6cd5fdd0ed0c74fbca66`, carries the geographically restricted Tencent Hunyuan Community License. These are conflicting provenance signals, not proof that the entire project or its base weights are unrestricted. No legal clearance or unrestricted redistribution is claimed. The application does not bundle or redistribute these weights.

`ultra_model.py` and `ultra_refinement.py` are native tensor compositions using PyTorch, Hugging Face Transformers and Apache Diffusers primitives. They do not import, invoke, copy or package the reference repository's inference modules, pipeline, CUDA extensions or CLI. Architecture dimensions, tensor key layout, trained attention packing, Fourier features, scaling and Euler integration are implemented against the checkpoint contract. Reference source was inspected to understand that contract; this is not described as a clean-room validation.

## Implementation differences and limits

The native path samples 409,600 uniform surface positions for voxel anchors, rather than the reference sharp-edge/uniform mixture. Dense PyTorch attention and hierarchical 128/256/512 extraction replace reference accelerators. The full 21-block denoiser is split by parameter size across all four GPUs (13/4/2/2 blocks); the decoder's point queries run on all four. All checkpoints load strictly; only the VAE decoder is needed and loaded, not its unused encoder.

An aligned COPY of a parent is refined and the output is transformed back. A generated TRELLIS native model uses a -X front; Ultra's image conditioning expects +Z. Default Ultra alignment is +90 degrees Y. Legacy Detail jobs keep their historical no-rotation default; the UI allows the corrected alignment explicitly. Original files and prior failed trials remain.

One-versus-four FP32 numerical agreement validates partitioning of the native implementation, not equivalence to every upstream accelerator or benchmark. Quality claims must cite the actual generated comparison, including failures and settings. More faces, closed topology or proximity alone do not establish better detail.
