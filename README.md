# 3D Printing Designs

Chris Long's working repository for functional CAD, printable exports, fit tests, and product history. The standard is simple: solve the real-world problem with an editable, measurable, print-ready design.

## Start a new CAD task

1. Create `tasks/<task-id>-<product>.md` from `tasks/TEMPLATE.md` and fill in confirmed dimensions before modeling.
2. In Codex, invoke the design workflow with a short request such as:

   ```text
   $functional-cad-design Create cad-042 truck cup insert from tasks/cad-042-truck-cup-insert.md.
   ```

3. Keep the task brief, editable source, exports, fit tests, references, and archived approved revisions in their assigned folders below.

Use millimeters. Mark unknown dimensions as estimated, do not silently guess, and preserve approved revisions.

## Review an existing design

Use the review-only QA workflow when you want an assessment without a redesign:

```text
$3d-print-design-qa Review exports/cad-042/cad-042_truck-cup-insert_print_r01.3mf. Do not modify files.
```

The result is **PASS**, **PASS WITH WARNINGS**, or **FAIL**, with evidence and specific risks.

## Repository layout

| Path | Purpose |
| --- | --- |
| `.agents/skills/` | Reusable Codex design and QA workflows |
| `tasks/` | Task briefs, measurements, constraints, and approvals |
| `designs/` | Editable parametric/native CAD source and design notes |
| `exports/` | Print-ready 3MF projects and derived STL exports |
| `tests/` | Fit coupons, test sections, measured results, and print notes |
| `archive/` | Preserved superseded approved revisions |
| `references/` | Photos, sketches, specifications, and measurement references |
| `Final_Products/`, `In_Progress/`, `Personal/`, `Downloaded_Models/`, `Needs_Review/`, `library/` | Existing legacy content; preserved in place until an explicitly approved migration |
| `website/`, `docs/`, `scripts/`, `tools/` | Existing catalog, website, and automation support |

No migration is included in this setup. If legacy files should move into the workflow folders, first make a separate, reviewed migration plan that updates all references.

## Naming and revisions

Use `<task-id>_<product>_<artifact>_rNN.<extension>` for new task files. Use lowercase kebab-case words inside the fields.

```text
cad-042_truck-cup-insert_source_r01.scad
cad-042_truck-cup-insert_print_r01.3mf
cad-042_truck-cup-insert_fit-coupon_r01.stl
```

Increment `rNN` for every design revision. Before changing an approved revision, copy it to `archive/<product>/`; never overwrite it. An STL is an export, not the only deliverable when editable source is reasonably possible.

## Validation

Run the repository check after structural changes or before a pull request:

```powershell
python scripts/check_3d_library.py --full
```

`AGENTS.md` contains the permanent design, measurement, material, print-readiness, revision, and completion-report rules.
