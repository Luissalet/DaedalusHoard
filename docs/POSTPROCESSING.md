# Optional mesh preparation

Both passes create a child job in the existing queue. The parent GLB is read-only and its SHA-256 is checked before and after processing. Original geometry, previous versions and materials remain in their own folders. Cancellation stops only the owned worker. These operations use CPU and reserve no GPU; generation and learned refinement retain their existing four-GPU scheduling.

## Printing

`POST /api/jobs/{id}/repair`, MCP `model_repair`.

- `detail_faces`: default 1,000,000; an explicit working triangle budget before repair, or null for all source detail.
- `remove_small_components`: false by default. True explicitly retains only the largest component before repair.
- `method`: `volume` (default) reconstructs the voxel volume; `surface` retains classic MeshFix cleanup. Saved jobs without a method keep the historical surface algorithm.
- `voxel_resolution`: 128, 256 (default), or 384 cells along the longest dimension. Used by volume reconstruction.

Volume reconstruction voxelizes the working surface, closes one-cell gaps with a full 3D neighbourhood, fills enclosed space and extracts a new surface. Its report records the pitch and resolution. Details below the cell size can be smoothed or lost; nearby parts can merge. This is an explicit geometry approximation. For a 100mm longest dimension at256 cells, nominal cell size is about0.39mm before any preprocessing budget loss.

Classic native mesh cleanup, boundary filling and intersection cleanup use MeshFix through its in-process Python binding. It can be slow on severely nonmanifold surfaces. The output includes GLB with transferred vertex color, STL and PLY. The report measures boundary/nonmanifold edges, connected components, consistent winding, watertightness and positive-volume status. `closure_verified` requires a watertight positive-volume result. A failed closure remains visible as such; completion alone is not a printable-solid certificate. Both algorithms can change small features. Inspect walls, supports, scale and slicer settings separately.

## Games

`POST /api/jobs/{id}/optimize`, MCP `model_optimize`.

- `target_faces`: default 50,000, minimum 100.
- `texture_size`: 512, 1024, 2048 (default) or 4096.

Quadric mesh simplification is followed by packed UV charts and native CPU texture baking. The self-contained GLB includes base color/alpha and metallic/roughness. Source PBR voxels retain their coordinate frame during sampling; otherwise vertex color is transferred. If materials were explicitly discarded upstream, later preparation passes keep that choice. UV seams duplicate vertices where necessary. Topology is measured on the welded working geometry before seam duplication.

The report records requested and actual face counts, `budget_met`, texture dimensions, GLB sizes and source SHA. Some meshes cannot meet the requested reduction without further geometry changes; the UI reports that outcome. This is a static triangle asset with no automatic rigging, animation topology, collision hulls or LOD chain.

## Inspection and export

Use Versions to select any saved source or child, and Compare to inspect a child against its original generation. Download the processing report from the preparation panel or the job's `processing_report` result URL. Scale is explicit: GLB metres, STL/PLY millimetres. Exporting never changes the saved model. CPU library licenses and pinned provenance are in THIRD_PARTY.md and postprocessing-provenance.json.
