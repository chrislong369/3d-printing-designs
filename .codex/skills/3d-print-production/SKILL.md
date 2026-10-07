---
name: 3d-print-production
description: Route LongWorks Studio 3D-printing jobs through the best specialist stack—search, AI image-to-3D, Blender, CadQuery/FreeCAD, mesh validation, AMS/no-AMS engineering, and Bambu Studio—then deliver production geometry rather than placeholder meshes.
---

# LongWorks 3D Production Skill

Read `../../../LONGWORKS_3D_SOURCE_OF_TRUTH.md` and `../../../3D_PRINTING_CONTEXT.md` first.
Read `../../../TOOLCHAIN_CATALOG.md` only when tool choice matters.
Read `../../../docs/toolchain-setup.md` for the prepared local runtime.
Run tools with the isolated LongWorks Python interpreter; do not assume system Python has CAD/mesh packages.
Do not install or configure paid generation providers unless Chris explicitly approves it.

## Project-state rule
For an active project, use its project folder as the working context. Maintain one `PROJECT.md` (or equivalent) containing the objective, approved measurements/inputs, current keeper candidate, unresolved decisions, next action, and validation status. Update that state instead of forcing Chris to restate the project each session.

## Route the task
- Existing tested object → search MakerWorld/Printables first when licensing/use allows
- Organic character/reference image → image-to-3D candidate + Blender visual refinement
- Mechanical/functional → CadQuery or FreeCAD
- Existing STL/OBJ/GLB → inspect, repair, modify
- Bambu packaging only → use real validated meshes

## Tool split
Use model judgment for interpretation, design decisions, visual comparison and choosing the next step.
Use deterministic tools/scripts for measurements, geometry checks, conversions, file handling, repeatable QA and packaging whenever possible.

## Organic-reference quality loop
1. Lock approved reference images.
2. Prefer front + side + 3/4/multiview references where possible.
3. Generate/reconstruct a candidate mesh.
4. Import to Blender.
5. Capture consistent preview views.
6. Compare silhouette, proportions, landmarks, negative space, and details to the reference.
7. Repair the largest mismatch first; repeat.
8. Only after visual match is acceptable: engineer print splits, colors, connectors and supports.
9. Validate the actual export files.
10. Package into Bambu Studio.
11. Open and inspect the final Bambu project.

Inspect actual images at the blockout and final checkpoints. Capture comparable front, side and three-quarter views where reference fidelity matters. Fix the largest geometry mismatch before changing cameras or materials. If a preview cannot be inspected, report visual validation as incomplete.

## Color strategy
AMS is available. Choose AMS, no-AMS separate parts, hybrid, single color, or paint based on the job.
Never infer no-AMS from previous projects.

## Quality gates
Use `references/quality-gates.md`. Each gate must be PASS, WARN, FAIL, or NOT CHECKED.
A verbal statement that something “should work” is not evidence of a PASS.

## Commercial STL rule
Before a design is intended for sale:
- verify rights/license for every externally sourced model or asset
- prefer original LongWorks designs
- document AI/service commercial-use terms
- preserve editable source
- test-print before labeling production-ready
