# CAD and 3D-Printing Operating Rules

## Scope and equipment

- This repository supports functional CAD and 3D-printing work for Chris Long.
- Primary printer: **Bambu Lab P1S**.
- Multi-material system: **AMS 2 Pro**.
- Default materials are **PLA+** and **PETG**. Use another material only after Chris explicitly approves it.
- Use millimeters for all dimensions, drawings, parameters, filenames that include dimensions, and test results.

## Design priorities

For functional parts, prioritize in this order: dimensional accuracy, strength, heat resistance, printability, and real-world use. Treat appearance as secondary unless the task says otherwise.

Prefer parametric, editable source files. Do not provide only an STL when an editable source format can reasonably be produced. Keep the editable source, a Bambu-ready 3MF project when applicable, and derived exports together for each task.

## Measurements and assumptions

- Record every critical measurement, tolerance, and design assumption in the task brief or design notes.
- Clearly label each dimension as **confirmed** or **estimated**.
- Never silently invent a missing dimension. Ask for it, or document the estimate, why it is needed, and the risk it creates.
- Account for material shrinkage, heat exposure, wall thickness, layer orientation, support requirements, assembly clearances, and the expected load.
- When practical, use a coupon or a small fit-test section before starting a long final print.

## Revision and file safety

- Preserve prior revisions. Never overwrite an approved design.
- Before an approved design changes, retain the prior revision in `archive/` and increment the revision number.
- Do not move, rename, delete, or redesign existing repository files unless Chris explicitly approves that work.
- Existing folders such as `Final_Products/`, `In_Progress/`, `Personal/`, and `library/` are preserved legacy content. Do not migrate them during a new design task without explicit approval.

## Required workflow

1. For a new, changed, or repaired functional object, use the `functional-cad-design` skill and start from `tasks/TEMPLATE.md`.
2. For an assessment-only request, use `3d-print-design-qa`; it must not redesign or modify the object unless separately asked.
3. Save new task work under the repository workflow folders described in `README.md`.
4. Run available validations before declaring work complete. At minimum, run `python scripts/check_3d_library.py --full` after repository-structure changes.
5. Do not claim that a physical fit, load, or heat test passed unless it was actually performed and recorded.

## Completion report

Every completed CAD task must include a concise report with:

- files created or changed;
- confirmed measurements, estimates, and assumptions;
- validations and physical or virtual tests performed;
- unresolved risks, missing measurements, or recommended next tests.
