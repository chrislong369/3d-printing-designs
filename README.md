# LongWorks 3D Printing Designs

This repository is the shared source of truth for LongWorks Studio 3D-printing work used by ChatGPT and Codex.

## Working folders

- `Final_Products/` — finished LongWorks designs that are ready to keep, print, or potentially publish/sell
- `In_Progress/` — active LongWorks design work and iterations
- `Personal/` — personal-use prints and customized models
- `Downloaded_Models/` — downloaded/reference models that are not LongWorks originals
- `Needs_Review/` — files that still need classification, cleanup, license review, or validation
- `3D_DROP/` — temporary inbox for new files that have not been sorted yet

## Codex / production context

- `AGENTS.md`
- `3D_PRINTING_CONTEXT.md`
- `TOOLCHAIN_CATALOG.md`
- `LONGWORKS_3D_SOURCE_OF_TRUTH.md`
- `.codex/skills/3d-print-production/`

Codex should read these before substantial 3D work.

## Website

The optional static website is generated from `Final_Products/`.
Only finished products should appear there.

## Rules

- Keep downloaded third-party files separate from original LongWorks work.
- Verify licenses before selling or redistributing third-party models.
- Do not treat a concept image or placeholder mesh as a finished printable product.
- Use GitHub as the canonical shared 3D workspace; local desktop copies should sync with `main`.
