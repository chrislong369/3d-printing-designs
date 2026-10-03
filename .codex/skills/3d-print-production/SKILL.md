---
name: 3d-print-production
description: Route LongWorks Studio 3D-printing jobs through the best specialist stack—search, AI image-to-3D, Blender, CadQuery/FreeCAD, mesh validation, AMS/no-AMS engineering, and Bambu Studio—then deliver production geometry rather than placeholder meshes.
---

# LongWorks 3D Production Skill

Read `../../../3D_PRINTING_CONTEXT.md` and `../../../TOOLCHAIN_CATALOG.md`.
These paths resolve from this skill directory. Read `../../../LONGWORKS_3D_SOURCE_OF_TRUTH.md`
and `../../../docs/toolchain-setup.md` for canonical storage and the prepared local runtime.
Run tools with the isolated LongWorks Python interpreter; do not assume the system Python
has CAD/mesh packages. Do not install or configure paid generation providers during setup.

## Route the task
- Existing tested object → search MakerWorld/Printables first when licensing/use allows
- Organic character/reference image → image-to-3D candidate + Blender visual refinement
- Mechanical/functional → CadQuery or FreeCAD
- Existing STL/OBJ/GLB → inspect, repair, modify
- Bambu packaging only → use real validated meshes

## Organic-reference quality loop
1. Lock approved reference images.
2. Prefer front + side + 3/4/multiview references where possible.
3. Generate/reconstruct a candidate mesh.
4. Import to Blender.
5. Capture consistent preview views.
6. Compare silhouette, proportions, landmarks, negative space, and details to the reference.
7. Repair the largest mismatch first; repeat.
8. Only after visual match is acceptable: engineer print splits, colors, connectors and supports.
9. Validate.
10. Package into Bambu Studio.

Inspect actual images at the blockout and final checkpoints. Capture comparable front, side
and three-quarter views where reference fidelity matters. Fix the largest geometry mismatch
before changing cameras or materials. If a preview cannot be inspected, report visual
validation as incomplete. This strengthens the visual QA loop reviewed in the MIT-licensed
`CheshireJCat/create-3d-model-skill` playbook; its installation is optional to the core route.

## Color strategy
AMS is available. Choose AMS, no-AMS separate parts, hybrid, single color, or paint based on the job.
Never infer no-AMS from previous projects.

## Quality gates
- no placeholder geometry
- correct size and orientation
- visual reference match where relevant
- manifold/watertight as required
- wall/feature thickness
- no severe self-intersections
- connector fit
- build-volume compliance
- material strategy
- plate strategy
- actual final 3MF verified in Bambu Studio

## Commercial STL rule
Before a design is intended for sale:
- verify rights/license for every externally sourced model or asset
- prefer original LongWorks designs
- document AI/service commercial-use terms
- preserve editable source
- test-print before labeling production-ready
