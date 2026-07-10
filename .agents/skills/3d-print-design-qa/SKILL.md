---
name: 3d-print-design-qa
description: Review an existing 3D-print design for functional, print, and file-readiness risks without automatically changing it. Use for design reviews, pre-print checks, and acceptance assessments. Do not use to create, modify, or repair geometry; use functional-cad-design for that work.
---

# 3D-Print Design QA

Use this skill to assess an existing design, export, or project. This is a review-only workflow: inspect and report; do not redesign, rename, move, or overwrite files unless Chris separately authorizes an implementation task.

## Review workflow

1. Identify the exact file, revision, intended material, printer, and use case. If the editable source or dimensions are missing, say so.
2. Review the task brief, source notes, slicer/project settings, and relevant references when available.
3. Inspect the following areas and distinguish verified evidence from assumptions:

| Area | What to inspect |
| --- | --- |
| Dimensions | Overall size, critical interfaces, units, and documented measurements |
| Clearances and tolerances | Sliding, press, snap, fastener, threaded, and assembly interfaces |
| Wall thickness | Minimum walls, local thin areas, top/bottom thickness, and consistency |
| Weak features | Sharp corners, cantilevers, narrow necks, unsupported tabs, and stress risers |
| Layer orientation | Load direction, likely fracture planes, bed contact, and anisotropy risk |
| Material suitability | PLA+/PETG fit for the actual environment, moisture, UV, heat, and chemicals |
| Heat and load exposure | Continuous load, impact, cyclic use, vehicle/interior heat, and safety margin |
| Support requirements | Overhangs, bridging, support damage risk, and accessibility for removal |
| Print time and waste | Unnecessary support, excessive infill, inefficient orientation, and avoidable retries |
| Assembly and fit risks | Part interference, insertion force, hardware access, and tolerance stack-up |
| File completeness | Task brief, references, print settings, export, revision label, and test evidence |
| Editable-source availability | Parametric/native source present, understandable, and aligned with the export |

4. Do not infer missing geometry or measurements as facts. State the missing evidence and the smallest test or measurement that would reduce the risk.
5. Issue exactly one final status:

   - **PASS** - no material functional, print, fit, or file-completeness issue is found within the available evidence.
   - **PASS WITH WARNINGS** - printable or usable as reviewed, but one or more risks, estimates, or evidence gaps remain.
   - **FAIL** - a likely functional, safety, fit, printability, or required-file problem must be addressed before release or printing.

## Required report format

```markdown
# QA: <product and revision>

## Status: PASS | PASS WITH WARNINGS | FAIL

## Evidence reviewed
- Files and revisions:
- Measurements and material:
- Print settings or orientation:

## Findings
| Area | Status | Evidence | Risk / reason |
| --- | --- | --- | --- |

## Required actions
- Only for FAIL items.

## Recommended follow-up tests
- Smallest useful coupon, measurement, or print test.

## Unverified assumptions
- Explicitly list every evidence gap.
```

The QA result is not approval to alter the design. If a change is wanted, hand the findings to `functional-cad-design` in a separate implementation request.
