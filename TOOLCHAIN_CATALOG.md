# LongWorks 3D — Curated Toolchain Catalog

This catalog is intentionally opinionated. Use tools by job type instead of installing everything blindly.

## Tier 1 — Install / use first

### Bambu Studio AI skill
Repository: https://github.com/heyixuan2/bambu-studio-ai

Why it matters:
- purpose-built agent skill for Bambu printers including P1S
- searches MakerWorld and Printables first
- AI generation providers: Meshy, Tripo, Hyper3D Rodin
- parametric CAD route for exact parts
- checks mesh integrity, build volume, floating parts, overhangs, wall thickness, bed contact, and material suitability
- repairs models
- can convert textured models into AMS-ready multicolor projects
- previews models
- opens in Bambu Studio
- can read printer status and AMS filament state read-only
- current repository metadata on 2026-10-03: 215 stars, MIT, active in 2026

Recommended status: INSTALL.

### Blender MCP
Candidate: https://github.com/mackson/blender-mcp

Why:
- gives Codex direct control of Blender over MCP
- scene inspection, Python/bpy execution, sculpt tools, previews/renders, exports
- lets the agent SEE renders and iterate instead of blindly writing Blender scripts

Recommended status: INSTALL after review.

### FreeCAD MCP
Repository: https://github.com/neka-nat/freecad-mcp

Why:
- strong for dimensional/functional parts
- direct FreeCAD control and Python execution
- current repository metadata on 2026-10-03: ~2.6k stars, MIT, actively maintained

Recommended status: INSTALL for functional CAD work.

### CadQuery
Repository: https://github.com/CadQuery/cadquery

Why:
- mature Python parametric CAD
- excellent for brackets, organizers, enclosures, holders, replacement parts, hole patterns, snap fits
- current repository metadata on 2026-10-03: ~5.8k stars, actively maintained

Recommended status: USE as the code-first CAD engine.

## Tier 1.5 — High-value skill for visual modeling

### Create 3D Model skill
Repository: https://github.com/CheshireJCat/create-3d-model-skill

Why:
- Codex-native Blender skill
- specifically covers reference-image reconstruction, multiview fidelity, BlenderMCP, visual QA, repair and export
- valuable playbook even though it is a small/new repository

Recommended status: REVIEW and layer useful QA rules into the local LongWorks skill; do not trust popularity alone.

## Tier 2 — Image-to-3D engines

### Meshy
Official MCP: https://github.com/meshy-dev/meshy-mcp-server

Strength:
- direct MCP path from Codex to text/image/multi-image 3D generation
- remesh, retexture, UV unwrap, conversions, model downloads
- good Bambu/3MF workflow in Meshy's platform

Constraint:
- official MCP requires Meshy API key; Pro or higher required
- use only after intentional subscription/API setup

### TRELLIS / TRELLIS.2
Microsoft open 3D generation family.

Use:
- high-detail image-to-3D candidate generation
- strong option when local/cloud GPU route is available

Caution:
- review current model/project license and dependency terms before commercial STL sales.

### Hunyuan3D
Tencent image/text-to-3D family.

Use:
- organic geometry candidate, particularly when multiple reference views can be supplied

Caution:
- verify current license/model terms before commercial use.

### Stable Fast 3D / TripoSR
Use:
- rapid preview/base-mesh generation
- not the first choice for the highest 2026 sculpt fidelity

### Tripo / Rodin / Hi3D
Commercial generation alternatives.
Use as benchmarks rather than assuming one vendor wins every object.

## Tier 3 — Mesh repair / topology

### Blender 3D Print Toolbox
Use for:
- non-manifold checks
- wall thickness
- intersections
- geometry checks before print export

### Instant Meshes
https://github.com/wjakob/instant-meshes
Use when generated geometry needs retopology before further sculpt/editing.

### Manifold / manifold3d
Use for robust watertight boolean operations where appropriate.

## Bambu packaging

### Bambu Studio
https://github.com/bambulab/BambuStudio
Source of truth for final slicing/validation.

### bambu3mf
https://github.com/gstark/bambu3mf
Python library for Bambu-compatible multi-plate 3MF with printer/filament presets.

### bambu-3mf
https://github.com/Vivapercuore/bambu-3mf
Richer project packaging including multicolor/per-triangle painting, modifiers, support/seam/fuzzy-skin metadata, variable layer height, and multi-plate metadata.

## Operating principle

Do not ask “which one tool makes the model?”
Use:
CONCEPT → BEST GENERATOR/BASE → BLENDER/SCULPT → PRINT ENGINEERING → VALIDATION → BAMBU.

The image-to-3D output is never automatically trusted as the final sellable STL.
