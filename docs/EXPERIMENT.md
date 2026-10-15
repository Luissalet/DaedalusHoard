# Four-GPU generation and refinement, 2026-10-15

Research task619 preceded this product. TRELLIS.2 generated the same mechanical reference at512 and1024 across all four local NVIDIA GPUs. Full basic generation took93.659s and198.201s respectively, excluding startup/download. Full meshes had3,060,288 and12,529,836 faces.

The selected learned refiner was DetailGen3D with MIT weights, using an independent composition of Apache Diffusers primitives, the separately licensed scheduler and image encoder. We did not execute its upstream transformer modules carrying the Tencent geographic restriction. Strict state loading, attention-layout controls and four-GPU FP32 comparisons are retained in the evidence. Mixed Ada/Blackwell reduced precision is not bit-identical.

The correct rectified-flow update is `sample + (sigma - sigma_next) * velocity`. Earlier generic-Euler refinements were invalid quality evidence and were discarded as comparisons. Correct runs at2048 latents and a higher8192-latent run partially recovered their own VAE conversion loss but visually lost holes, thin tubes and sharp gear details against the original. The8192 case restored more detail yet did not beat the original. No valid final refinement was watertight. This is one controlled mechanical example, not a universal model ranking or a ground-truth quality score.

Mean symmetric sampled-surface distance as a percentage of the original bounding-box diagonal:512 VAE0.9324%, refined0.6058%;1024 VAE0.8667%, refined0.6319%;8192 VAE0.8590%, refined0.5483%. This measures preservation, not subjective quality or correctness of the generated object.

Correct1024 refinement took63.569s, including9.116s in the DiT and37.021s decoding; its diagnostic VAE result was reused. The8192 research run took165.292s including a separate diagnostic VAE decode. These are research timings, not product latency promises. Native product execution has its own receipts.

Full evidence, source revisions, hashes, configurations, invalid attempts and browser screenshots: `D:/LocalAI/research-inbox/3d-refine-4gpu-20261015/RESULTADO.txt`. Actual browser comparison: http://127.0.0.1:63619/comparison.html while the private preview is running. Product validation uses separate data stores `daedalus-qa622-20261015` and `daedalus-qa622b-20261015`.
