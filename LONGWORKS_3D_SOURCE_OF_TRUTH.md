# LongWorks 3D — Source of Truth

This repository — `chrislong369/3d-printing-designs` — is the canonical shared workspace for LongWorks Studio 3D-printing work.

## Scope
Use this repository for:
- printer and AMS context
- filament/material notes relevant to design
- Codex skills and MCP/tool references
- 3D-printing workflows
- STL/3MF/STEP/OBJ/GLB design assets as appropriate
- Blender/CAD source files where practical
- project-specific print engineering and validation
- tooling/catalog updates

Do NOT use this repository as the canonical store for unrelated business data such as job tracking, customer financial records, or money trackers.

## Storage rule
- GitHub `main` is the shared source of truth.
- Local desktop copies are working copies and should sync to/from this repository.
- Do not create a second LongWorks 3D repository, cloud context pack, or desktop-only master.
- ChatGPT should update these shared context/workflow files here when GitHub write access is available.
- Codex should read and update the repository copies instead of inventing replacement structures.
- New project assets belong under the existing `In_Progress/`, `Final_Products/`, `Personal/`, `Downloaded_Models/`, `Needs_Review/`, or `3D_DROP/` structure.
- If a local-only tool produces files, move/sync the approved outputs back into the correct GitHub project folder.

## Canonical-rule principle
A durable fact or rule should have one authoritative home. Reference it elsewhere instead of copying divergent versions.

Core canonical files:
- `AGENTS.md` — routing and operating rules
- `3D_PRINTING_CONTEXT.md` — printer/material/design context
- `TOOLCHAIN_CATALOG.md` — approved/suggested tool routes
- `.codex/skills/3d-print-production/SKILL.md` — production workflow
- `.codex/skills/3d-print-production/references/quality-gates.md` — pass/fail criteria
- project-level `PROJECT.md` files — active project state

## Version rule
Keep the proven keeper plus useful editable source/recovery assets. Do not retain endless failed iterations just because they exist; however, do not delete nonidentical variants until the keeper is proven or the unique geometry/settings have been reviewed.

## Completion rule
No 3D project is production-complete merely because a file was generated or a 3MF opens. The real output must pass the documented quality gates, including final Bambu Studio inspection.

Last established: 2026-10-07
