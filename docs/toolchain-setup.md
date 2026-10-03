# LongWorks repository and toolchain setup — 2026-10-03

Canonical repository: https://github.com/chrislong369/3d-printing-designs

Working clone: `C:\Users\chris\Documents_Local\3D Printing\3d-printing-designs`

The repository instructions/context are authoritative. New external dependencies, caches,
diagnostics and integration sources stay under the local Tools folder, outside OneDrive
and outside the model checkout. The active Remi trophy remains at its existing location.

## Detected and installed components

| Component | Result | Version | Path / integration |
|---|---|---|---|
| Repository core instructions | PASS | Reviewed 2026-10-03 | AGENTS, context, catalog, source-of-truth document, production skill and quality-gates reference readable |
| Git | PASS | 2.55.0.windows.3 | `C:\Program Files\Git\cmd\git.exe`; GitHub CLI authentication and origin verified |
| Node.js | PASS | 24.14.1 | `C:\Program Files\nodejs\node.exe` |
| System Python | PASS | 3.14.3 | `C:\Python314\python.exe`; preserved |
| Isolated CAD Python | PASS | 3.12.15 | `Tools\longworks-python\Scripts\python.exe` |
| Blender | PASS | 4.5.3 LTS | `Tools\blender-4.5.3-windows-x64\blender.exe`; version executed |
| Bambu Studio | PASS | 02.08.03.66 | `C:\Program Files\Bambu Studio\bambu-studio.exe`; running process, file version, profiles and skill discovery verified |
| CadQuery | PASS | 2.8.0 | Isolated Python; OpenCascade kernel valid/volume smoke test passed; no design exported |
| FreeCAD | PASS | 1.1.4 / revision 20260928 | `Tools\FreeCAD-portable\FreeCAD_1.1.4-Windows-x86_64-py311\bin`; FreeCADCmd version and FreeCAD/Part imports passed |
| LongWorks production skill | PASS | Repository-managed | `.codex/skills/3d-print-production/SKILL.md`; paths and frontmatter checked; visual QA strengthened |
| Bambu Studio AI | PASS | 2.0.0 | `C:\Users\chris\.codex\skills\bambu-studio-ai`; all required and optional doctor dependencies passed |
| Create 3D Model skill | PASS | Reviewed installed source | `C:\Users\chris\.codex\skills\create-3d-model`; visual checkpoints reviewed |
| Manifold / PyMeshLab | PASS | 3.5.4 / 2025.7.post1 | Isolated Python; imports passed |
| bambu3mf / lib3mf | PASS | 0.1.0 / 2.5.0 | Installed from reviewed upstream source in isolated Python; imports passed |
| bambu-3mf | PASS | 0.1.0 | TypeScript/Node library in Tools; build and 92 tests passed; full dependency audit zero vulnerabilities |
| Blender MCP | PASS prepared / WARN inactive | MCP 2.0.0, connector 2.1.0 | Built Tools source; 17 tools enumerated; real read-only version query passed in temporary factory Blender; zero dependency vulnerabilities |
| FreeCAD MCP | PASS prepared / WARN inactive | 0.1.25 | Installed isolated Python server; MCP initialization and 17-tool enumeration passed; GUI RPC addon is not active |
| Blender 3D Print Toolbox | PASS prepared / WARN inactive | 1.4.1 | Official GPL extension source in `Tools\print3d-toolbox\source`; prepared package, persistent add-on not enabled |

All relative Tools paths above start at `C:\Users\chris\Documents_Local\3D Printing`.
GUI tools need not be on the global PATH: use explicit paths or dot-source
`Tools\Diagnostics\longworks-shell.ps1` for session-only discovery. Skills are discoverable
on the next turn; the repository production skill remains the workflow authority.

## Preparation boundaries and optional tools

`INSTALL_NEXT.md` reserves persistent Blender add-on/MCP changes for approval. Preparation
is complete under the user's "install or prepare" instruction. No active Codex MCP
configuration or user Blender/FreeCAD preferences were changed. The tested Blender bridge
used loopback port 19876 and was stopped. It did not attach to the user's open scene.
The prepared connector uses 127.0.0.1 instead of upstream's all-interface bind.

Review-only configuration: `Tools\Diagnostics\mcp-config.prepared.toml`.
Blender connector source: `Tools\blender-mcp\src\blender-addon\mcp_connector_v2.py`.
FreeCAD addon source: `Tools\freecad-mcp\addon\FreeCADMCP`.
These prepared items require activation before persistent interactive GUI control.

Bambu skill model is P1S. Generated output goes to local `Projects\LongWorks Outputs`.
Printer IP/serial/access code were not added; live printer/AMS status is unverified.
No paid Meshy, Tripo or Rodin access was configured, and no API secrets were created.
Tier-2 GPU generation engines and Instant Meshes are conditional routes, deferred until
a project actually needs them. This setup does not install every optional catalog item.

FreeCAD's machine installer was canceled at elevation. Its official portable archive was
downloaded instead, SHA-256 matched the release asset digest, and extraction completed
with native 7zr after Python's extractor rejected BCJ2 compression. No elevation is needed
to run the portable installation.

## Diagnostics and limitations

- Eight duplicate deletions proved against retained SHA-256-identical copies; 102 models retained.
- No exact remaining model duplicates or bad 3MF archives; uncertain versions left in place.
- Full repository structure check and four safe-intake/Unicode regression tests pass.
- Public catalog contains 12 Final_Products entries; filter/count/empty-state DOM checks pass.
- Internal full catalog and public website generation/deployment have distinct roles; no duplicate Pages deploy.
- Both Node tool sources were updated locally within their allowed dependency ranges, with
  a larger dev-only upgrade for the packaging library; full audit is clean and its tests pass.
- Evidence: `docs/cleanup-audit.json`, `docs/cleanup-review.md` and
  `Tools\Diagnostics\mcp-probe.json`. External source commits/installed packages are recorded
  in `Tools\Diagnostics\toolchain-inventory.json` and `requirements.lock.txt`.
- 27 of 48 legacy STL meshes are non-watertight in the inventory check. Review them before
  printing/selling; setup diagnostics do not certify existing designs or physical fit.
- Bambu Windows `--help` returned no console text. CLI/profile discovery passes; an actual
  slice, GUI model preview and physical print are intentionally outside this setup phase.

No Pumpkin Reaper work, new design, model export, print submission or paid API setup was started.
