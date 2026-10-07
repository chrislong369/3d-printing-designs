# Quality Gates

Report each item as PASS / WARN / FAIL / NOT CHECKED.

A PASS must be based on inspection or deterministic evidence from the actual candidate output. Do not mark PASS because a workflow was supposed to perform the step.

- Reference fidelity
- Dimensions / mm scale
- Build volume
- Mesh manifold/watertight status
- Normals
- Self intersections
- Minimum wall / detail thickness
- Fragility
- Bed contact / orientation
- Support burden
- Assembly connectors / clearances
- AMS/no-AMS/hybrid strategy validity
- Plate packing
- Filament assignments
- Editable/source file preserved when applicable
- Export files reopen correctly
- Final 3MF opens in Bambu Studio
- Final plate/object layout inspected in Bambu Studio
- No placeholder geometry
- No unresolved blocker hidden behind a SUCCESS/COMPLETE label

## Completion
Production status may be COMPLETE only when the required gates for the job are PASS or explicitly accepted WARN. If Bambu Studio cannot be launched/inspected, final Bambu validation remains NOT CHECKED and the project is not production-complete.
