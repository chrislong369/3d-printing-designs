---
name: functional-cad-design
description: Design, modify, or repair a functional 3D-printable object for this repository. Use for fitment parts, organizers, mounts, adapters, brackets, and other real-world prints that need an editable, print-ready result. Do not use for assessment-only reviews; use 3d-print-design-qa instead.
---

# Functional CAD Design

Use this skill for requests that create, modify, or repair a functional printable object. Follow `AGENTS.md` and preserve existing designs unless the request explicitly authorizes a change.

## 1. Extract requirements

Read the request and create or update `tasks/<task-id>-<product>.md` from `tasks/TEMPLATE.md`. Capture the problem, required outputs, acceptance criteria, printer, material, environment, and approval status. Identify every unknown that could affect fit, strength, temperature, or safety.

## 2. Build a measurement table

Record dimensions in millimeters and label each one:

| Feature | Value (mm) | Status | Source or method | Tolerance / note |
| --- | ---: | --- | --- | --- |
| Example opening width | 69.5 | Confirmed | Caliper measurement | Measure at three points |

Use **Confirmed** only for supplied, measured, or reliably documented values. Mark all other values **Estimated** and explain the effect if the estimate is wrong. Never silently fill a gap.

## 3. Review constraints and environment

Check intended load, direction of force, mounting method, contact surfaces, moving parts, number of cycles, indoor/outdoor use, UV exposure, moisture, chemicals, vehicle heat, and required appearance. Identify restrictions from the P1S build volume, available nozzle, AMS 2 Pro, and requested color changes.

## 4. Recommend material

Default to PLA+ or PETG. Explain the recommendation in terms of heat, stiffness, toughness, moisture, and intended use. Do not select another material unless Chris explicitly approves it. State any material-specific print or tolerance assumptions.

## 5. Define a tolerance strategy

Specify target clearances for each interface: sliding, press fit, threaded insert, snap fit, fastener, or nested part. Account for printer calibration, material shrinkage, first-layer expansion, and orientation. Where the fit is uncertain, plan an adjustable or stepped coupon rather than pretending a nominal dimension is proven.

## 6. Create editable parametric source

Place editable source and notes in `designs/<task-id>/`. Use named parameters for critical dimensions, clearances, wall thicknesses, radii, and key pattern counts. Prefer a source format that Chris can edit later, such as OpenSCAD, FreeCAD, Fusion 360, or another appropriate native parametric format. Do not make an STL the sole source when an editable file is reasonable.

## 7. Review print orientation, support, and strength

Before export, state the preferred orientation and why. Review:

- layer direction relative to load and likely fracture planes;
- wall count, top/bottom thickness, ribs, fillets, and weak thin features;
- overhangs, bridges, support contact surfaces, and support removability;
- multi-part assembly, fasteners, inserts, and AMS color boundaries when relevant;
- build volume, print time, and avoidable material waste.

## 8. Plan and evaluate fit tests

For a fit-critical or long print, create a small coupon, interface section, or stepped-clearance test in `tests/<task-id>/`. Record the expected result, print material, orientation, and measured result. Do not promote an estimate to confirmed without evidence.

## 9. Export and name deliverables

Use the naming format `<task-id>_<product>_<artifact>_rNN.<extension>` with lowercase kebab-case words inside each field. Examples:

- `cad-042_truck-cup-insert_source_r01.scad`
- `cad-042_truck-cup-insert_print_r01.3mf`
- `cad-042_truck-cup-insert_print_r01.stl`

Store editable source in `designs/<task-id>/`, printable exports in `exports/<task-id>/`, fit-test files and results in `tests/<task-id>/`, source photos and specifications in `references/<task-id>/`, and superseded approved revisions in `archive/<product>/`.

## 10. Final QA checklist

Before completion, confirm or explicitly flag:

- [ ] Requirements and acceptance criteria are traceable to the task brief.
- [ ] Critical measurements, tolerances, and assumptions are recorded and status-labeled.
- [ ] Material and environmental suitability are explained.
- [ ] Editable source is present when reasonably possible.
- [ ] Orientation, supports, strength, and assembly have been reviewed.
- [ ] A fit test was used or a reason for not using one is recorded.
- [ ] Exports are named, revisioned, and located correctly.
- [ ] Prior approved revisions were preserved.
- [ ] Available repository validation has passed.
- [ ] The completion report lists files, assumptions, tests, and unresolved risks.

Use `3d-print-design-qa` for an independent review when the task asks for one. Do not present a QA review as a redesign unless Chris asks to implement the recommendations.
