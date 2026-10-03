# Chris / LongWorks Studio — Persistent 3D Printing Context

Last updated: 2026-10-03

## Hardware
- Bambu Lab P1S
- Build volume: 256 × 256 × 256 mm
- Default nozzle assumption: 0.4 mm unless explicitly changed
- AMS 2 Pro available
- External spool holder available
- One physical plate currently assumed unless updated
- Historical AMS 2 Pro slot-2 rewind issue: verify before relying on that slot for a long unattended multicolor print

## Color strategy
There is NO standing rule that models must be single-color or no-AMS.

For each job choose the best of:
- AMS multicolor
- separate color-by-part assembly
- hybrid AMS + separately printed parts
- single-color
- single-color plus paint

Only enforce true no-AMS physical color separation when the task explicitly requests it.

## Known filament history
- Sunlu PLA+ gray
- Sunlu PLA+ red
- PLA 3.0
- PETG black
- silver
- green
- blue
- historically low on black PLA

Inventory changes. Confirm stock before a filament-heavy build where color/material affects the design.

## Default print-engineering baseline
- 0.20 mm layers
- 3 walls
- ~15% gyroid infill
- PLA/PLA+ for decorative parts
- PETG when toughness/heat/moisture justify it
- prefer 240–245 mm max part dimension when practical
- hidden seams
- keyed pegs/sockets and anti-rotation features for assemblies
- validate build volume, scale, normals, watertightness/manifold state, self-intersections, thin walls, fragile features, bed contact, supports, and assembly clearances

Starting connector clearance:
- snug fit: ~0.20–0.30 mm radial
- easier glue/hand fit: ~0.30–0.45 mm total
Adjust after test coupons or geometry-specific review.

## Design-routing rule

### Organic / characters / figurines / image-derived
Reference image(s)
→ image-to-3D candidate when useful
→ Blender sculpt/cleanup/remesh
→ visual comparison against references
→ color/material split strategy
→ connectors / assembly engineering
→ 3D-print validation
→ STL/3MF
→ Bambu Studio final validation

### Functional / dimensional parts
Measurements
→ CadQuery or FreeCAD
→ STEP/STL
→ fit/clearance validation
→ Bambu Studio

### Existing model
Inspect license and geometry
→ repair/remesh as required
→ modify
→ validate
→ Bambu project

## Definition of done
A job is NOT complete because a 3MF opens.

Done requires:
- real final geometry, not placeholders
- concept/reference match appropriate to the job
- correct physical size
- printable individual parts
- valid color/AMS strategy
- engineered connectors where assembly is required
- validated meshes
- sensible orientations and plate layouts
- final STL/STEP/etc. deliverables
- final 3MF opened/checked in Bambu Studio
- assembly / filament / plate summary
