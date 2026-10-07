# LongWorks 3D — Codex Project Instructions

This repository is the single authoritative GitHub workspace for LongWorks 3D work. Do not create a replacement repo, alternate context pack, or parallel folder tree unless Chris explicitly asks for one.

For any 3D-printing, STL, 3MF, Blender, CAD, Bambu Studio, AMS, mesh-repair, or image-to-3D task:

1. Read `LONGWORKS_3D_SOURCE_OF_TRUTH.md`.
2. Read `3D_PRINTING_CONTEXT.md`.
3. Read `TOOLCHAIN_CATALOG.md` only as needed for tool choice.
4. Use `.codex/skills/3d-print-production/SKILL.md`.
5. Read the relevant project folder only; do not load unrelated projects into context.
6. Use the strongest specialist route for the job; do not default to primitive scripted geometry.
7. A concept image is a visual target, not a printable mesh.
8. Never call a job complete until the REAL production geometry is validated and the final Bambu project is opened and checked.
9. AMS is available. Do not assume AMS or no-AMS; choose based on the current job unless Chris explicitly specifies a strategy.
10. Prefer updating the existing project and canonical files over creating duplicate versions.

## Working-state rule
Every active project should have one human-readable `PROJECT.md` (or equivalent status file) that records:
- objective
- current approved design/state
- authoritative inputs and measurements
- unresolved decisions
- next action
- validation status
- final keeper filenames when known

Do not treat filenames such as `final`, `v7`, `production`, or `latest` as proof that a file is the keeper.

## Completion rule
A job may be marked COMPLETE only when the quality gates are evidenced against the actual output files. If Bambu Studio cannot be opened or inspected, mark Bambu validation as INCOMPLETE rather than assuming success.

## Tool responsibility
Use model judgment for interpretation, visual comparison, design choices, and routing. Use deterministic tools/scripts for measurements, file operations, geometry checks, conversions, packaging, and repeatable validation whenever available.
