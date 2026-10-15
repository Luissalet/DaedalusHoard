# Daedalus's Hoard

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Python/FastAPI, SQLite, a directly authored HTML/CSS/JavaScript client, and a local WebGL model viewer. Luis explicitly confirmed building directly on the real viewer and functions, without a preliminary mockup.

## Users

Luis, working locally with four NVIDIA GPUs, creating 3D models from images. He confirmed both printing and scenes/games, preserving originals and versions.

## Product Purpose

An independent Hoard for local image-to-3D generation, followed by an optional learned refinement pass. The user explicitly requested the four-GPU experiment first and the Hoard afterward. Research619 completed that prerequisite.

## Positioning

Generate locally across the user's four GPUs, retain each result, compare original and refined geometry, and export the chosen version. No claim that refinement automatically improves a model.

## Operating Context

Windows PC, three RTX5060Ti16GB and one RTX4070Ti12GB. Hoard Hub coordinates GPU leases. Faustus and all text-model reasoning use the global Sparks service. The generator must not stop those models or invoke an external application CLI as its engine.

## Capabilities and Constraints

The authorized implementation scope is image import, generation at tested512/1024 resolutions, optional refinement, persistent jobs and versions, cancellation, a3D viewer, exports and matching API/MCP operations. These are implementation targets until validated and documented in the README.
TRELLIS.2 generates geometry and PBR attributes. Research619 found that DetailGen3D partially restores its own VAE conversion loss but does not exceed the original TRELLIS mechanical example, including an8192-token test. Preserve both versions and make comparison central.
Generated meshes are not guaranteed watertight, print-ready, rigged or retopologized. No hidden units or implied real-world dimensions: export scale is explicit.

## Brand Commitments

Luis explicitly requested the existing Hoard family style and icon. Use its shared charcoal theme, Cinzel headings, Source Sans 3 controls, a turquoise accent and the curled dragon surrounding a gold 3D cube and caliper. Spanish operating copy, no slogans, and the shared Faustus launcher mark for copilot access. Daedalus is an implementation name chosen for this build, not a user-approved naming preference.

## Evidence on Hand

Real generated/refined files, timings, per-GPU execution traces, licensing notes, numerical checks, actual MCP calls and browser screenshots are preserved in the research619 report. They are evidence of the tested case, not universal benchmarks or product screenshots.

## Product Principles

- Keep generated originals and every later variant.
- Expose real progress and completed files; do not substitute demonstrations for model execution.
- Help the user compare shape before selecting a refined version.
- Share GPU resources through the existing Hub and keep the global text-model service available.
- Product API, MCP and browser use the same persisted jobs and artifacts.
