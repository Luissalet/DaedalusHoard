# Four-GPU generation and refinement, 2026-10-15

Research task619 preceded this product. TRELLIS.2 generated the same mechanical reference at512 and1024 across all four local NVIDIA GPUs. Full basic generation took93.659s and198.201s respectively, excluding startup/download. Full meshes had3,060,288 and12,529,836 faces.

The selected learned refiner was DetailGen3D with MIT weights, using an independent composition of Apache Diffusers primitives, the separately licensed scheduler and image encoder. We did not execute its upstream transformer modules carrying the Tencent geographic restriction. Strict state loading, attention-layout controls and four-GPU FP32 comparisons are retained in the evidence. Mixed Ada/Blackwell reduced precision is not bit-identical.

The correct rectified-flow update is `sample + (sigma - sigma_next) * velocity`. Earlier generic-Euler refinements were invalid quality evidence and were discarded as comparisons. Correct runs at2048 latents and a higher8192-latent run partially recovered their own VAE conversion loss but visually lost holes, thin tubes and sharp gear details against the original. The8192 case restored more detail yet did not beat the original. No valid final refinement was watertight. This is one controlled mechanical example, not a universal model ranking or a ground-truth quality score.

Mean symmetric sampled-surface distance as a percentage of the original bounding-box diagonal:512 VAE0.9324%, refined0.6058%;1024 VAE0.8667%, refined0.6319%;8192 VAE0.8590%, refined0.5483%. This measures preservation, not subjective quality or correctness of the generated object.

Correct1024 refinement took63.569s, including9.116s in the DiT and37.021s decoding; its diagnostic VAE result was reused. The8192 research run took165.292s including a separate diagnostic VAE decode. These are research timings, not product latency promises. Native product execution has its own receipts.

Full evidence, source revisions, hashes, configurations, invalid attempts and browser screenshots: `D:/LocalAI/research-inbox/3d-refine-4gpu-20261015/RESULTADO.txt`. Actual browser comparison: http://127.0.0.1:63619/comparison.html while the private preview is running. Product validation uses separate data stores `daedalus-qa622-20261015` and `daedalus-qa622b-20261015`.


## Native alternatives and learned high-resolution pass, task627 (15–16 October)

All runs used physical GPUs1/2/3/0 with individual Hub leases. The global text model remained on the Sparks. These are preserved versions in isolated stores; no original generation was overwritten.

| Object / stage | Full faces | Engine seconds | Worker total seconds |
| --- | ---: | ---: | ---: |
| Mechanical original512 | 4,227,310 | 71.270 | 154.566 |
| Mechanical Detail8192, aligned90 | 5,150,912 | 129.904 | 247.854 |
| Mechanical Ultra8192, aligned90 | 3,567,536 | 255.194 | 336.602 |
| Mechanical Ultra32768, aligned90 | 3,994,384 | 1498.456 | 1561.545 |
| Owl original512 | 1,514,230 | 66.686 | 111.025 |
| Owl Ultra8192, aligned90 | 1,456,020 | 216.895 | 260.303 |
| Mechanical native512→1024 | 17,486,120 | 295.323 | 661.683 |
| Owl native512→1024 | 6,038,376 | 142.050 | 234.359 |

Worker totals include mesh/material preparation and exclude queue time, downloads and model installation. Larger face counts alone are not a quality score. All meshes remain open.

Ultra is a native independent tensor composition using its published checkpoint; loading is strict and its four-GPU FP32 partition has relative L2 error8.9657578e-7 against one device. The input copy rotates90° aboutY to align TRELLIS's -X front to the image-guided refiner's +Z front; output is rotated back. Original files stay unchanged. Its weights label/base-code licensing discrepancy is preserved in ULTRA-PROVENANCE.md; no unrestricted redistribution claim is made.

Ultra8192 expands mechanical depth substantially (0.35754→0.63118). Ultra32768 preserves overall dimensions much better (depth0.35777), but its lighter preview smooths away small screws/reliefs; the owl preview cleans eye outlines while fusing and simplifying feather detail. Those preview observations are not full-mesh certification. It is an optional alternative, with no demonstrated global quality win.

The additional native high-resolution pass uses the stored normalized512 shape latent, verifies its SHA and executes only the trained1024 geometry stage, then newly generated PBR materials. It does not resample the coarse structure/512 shape or reuse old texture latents. An independent CPU control verified this actual control flow. Two real jobs traversed8/8/8/6 blocks on all four GPUs. Mechanical source model SHA427cdc905be89e43e8d5b012ef37772e63c648ce45d0a07c5ded7cb16deb1fdb and saved latent SHA2640bb5b6b417eb61316ca66ef6b2ef063b769976bedbd2076978e1c8af9d1f8 are unchanged; both source SHA pairs are in the MCP receipts.

Full geometry inspection is now available through the normal API/MCP-linked viewer, as a cached common clay derivative. The preview stays the default; millions of full triangles use more browser memory. It never replaces full originals or their materials.

Evidence: D:/LocalAI/research-inbox/daedalus-refiners627-20261015, including failed initial Ultra event-name collision (retained), corrected scheduling test, partition proof, per-job MCP receipts, preservation SHA inventory and actual browser screenshots. Private final comparison URLs use port63625; old private63622 and63624 are idle because automatic approval review rejected their stop actions. No retry through another mechanism was made.

Full-mesh browser comparison of the learned1024 versions shows more defined mechanical grilles/raised details and owl eye striations/feather edges than each saved512 original. Front and three-quarter captures use matching clay and linked cameras (upscale-*-full.png). This is a visually useful improvement on these two examples, not evidence of universal reconstruction accuracy or print-readiness. Microgeometry changes and both sources remain available for judgement. The learned second pass is the preferred optional enhancement in this comparison; Ultra remains a separate alternative with mixed preview results.

Full-mesh linked-clay browser comparison shows more defined grilles/raised mechanical details and owl eye striations/feather edges after the learned1024 stage. This is useful visual improvement on these two examples, not a universal quality or printing guarantee. Ultra32768 full geometry also cleans broad surfaces, while changing reliefs; the high-resolution native version retains more fine structure.

During final review an external cleanup removed the active isolated source/evidence and older QA stores. The exact functional checkpoint a0aa53f was recovered from Main refs/rescue/research-inbox-daedalus-refiners627-20261015-product/main. All13jobs survived in the newest independent copy daedalus-qa627b-20261016. Original mechanical model/latent matched pre-cleanup SHA; both upscale source latents match their recorded engine SHA. Current jobs/engine logs, reconstructed receipts and recaptured browser images are retained. Older deleted proof files are not claimed to remain available. Main was not changed by cleanup.
