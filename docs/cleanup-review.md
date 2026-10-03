# Cleanup review — 2026-10-03

## Confirmed safe cleanup

PR #2's eight deleted STL/3MF files each have a byte-identical retained copy; SHA-256 proof
and the exact pre-cleanup main commit are in `cleanup-audit.json`. No model was deleted
because its filename said old, test, draft, v1, v2, v3 or final. No uncertain asset was moved.
Git history remains the recovery point for removed scripts, placeholder folders and duplicates.

Removed `static.yml`: it duplicated Pages deployment and uploaded the entire repository.
Removed `build-site-data.yml`: public data is now generated within `deploy-site.yml`, avoiding
a second bot commit, a race with the internal catalog bot, and suppressed follow-up events.
The internal catalog workflow remains separate because it inventories all design files.

Removed `finalize_boxes.py`, `master_finalize_repo.py`, `organize_repo.py`: obsolete migration
scripts; the first two chose keepers and deleted alternatives based on names/dimensions,
without verifying unique geometry or slicer settings. They have no active workflow caller.
Preserved and repaired the unique intake utility and launcher; preview has no write side effects,
root/destination paths are bounded, all intake goes to review, and collisions cannot overwrite.

## Retained uncertain versions — do not delete by name

| Family / location | Items to compare | Evidence needed before retiring older files |
|---|---|---|
| `Personal/silverado_yeti*`, `yeti_cup_holder_adapter.stl` | v1–v5, final 3MF, original adapter | Identify tested keeper; compare tapered/connected/step-wall geometry and 3MF settings |
| `Personal/test_puck_cupholder_78mm_OD_5mm_tall.stl` | Fit coupon | Recorded fit result or confirmation no longer useful |
| `Personal/poop_bag_dispenser*`, `Poop_Bag_Dispenser_Set_3MF.3mf` | extra-roll, v2, v3, final rebuild | Compare assembly parts and extra-roll geometry; identify proven working final |
| `Personal/milwaukee_holder*`, `3D_DROP/MILWAUKEE BATTERY HOLDER.stl(1).stl` | clean flush, flat v3, mild flush, imported original | Confirm final fit and whether older variants preserve useful dimensions/geometry; duplicate v3 copy already removed |
| `In_Progress/Cosmetic_Organizers/brow*`, `Final_Products/Cosmetic_Organizers/Brow*`, `Needs_Review/brow*` | tubes, retail, enclosed, centered, special, 7/11 holes, one-plate project | Compare product dimensions, hole arrangements and slicer project; labels alone do not prove equivalence |
| `In_Progress/Cosmetic_Organizers/compartment_tray*`, `mascara_inventory_tray*`, `tray5x5*` | tile, gusset, socket, honeycomb, ledge, ultrafast variants | Determine which structures/assemblies are unique and which final was physically tested |
| `In_Progress/Utility_Designs/LongWorks Studio*` | nameplate, words only, thicker words, 3D text | Compare lettering/body thickness and intended mounting |
| `Personal/Gridfinity_3x3x5U_center_split*` | original and smooth 3MF | Compare meshes, placement, materials and slicer settings |
| `Needs_Review/Favorite_Filament_Sample*` | custom slicer copies, PETG/blank, holder v7 | Byte-distinct remaining projects may preserve different materials/settings; identical copies already removed |
| `Personal/P1S_Glass_Riser_Hole_Covers_Debossed_Letters_V2.3mf`, `Downloaded_Models/Darrieus_V5.3mf`, `Needs_Review/Skull_Wall_Mount_v6.3mf` | Named version with no older sibling in this repository | Keep: version suffix alone is not evidence of abandonment |

`cleanup-audit.json` also lists shared raw 3MF geometry groups. Shared meshes do not prove
the complete slicer projects are duplicates; transforms, plates, materials, painted colors,
presets and assembly information can differ. Preserve them until reviewed.

## Remaining folder / provenance issues

- Mesh inventory loaded all 48 STL files without parse errors. After trimesh vertex merging,
  27 are non-watertight, including five under Final_Products. See per-file flags in
  `cleanup-audit.json`. This is a legacy model-quality warning, not cleanup damage; all retained
  model bytes are unchanged. Do not call these files production-ready without repair/slicer review.
- STL bounds in the audit assume millimeters; STL does not encode units. The audit is not a
  physical-fit, self-intersection, minimum-wall, assembly, slicing or print acceptance test.

- `Needs_Review` has a real purpose; it is not an unused folder. Unnamed UUID STL needs identification.
- `3D_DROP` contains an imported battery-holder original; retain its recovery/provenance context.
- `website/assets/product-images` is an empty placeholder file, not an image directory; no
  caller currently uses it. Retained as a review item, because the intended future image structure is unclear.
- All tracked model assets are STL/3MF. Editable sources and proof of physical testing are
  absent from this repository; seek originals before treating any existing export as sale-ready.
- Third-party models need original URLs/licenses. File/folder names do not establish rights.
- Original PR's organization audit described folders no longer present; its deletion is sensible.
- Remaining underscore/bracket naming warnings are cosmetic. Keep established filenames to
  avoid breaking historical links and slicer references during this setup.

## Retention decision

The user prefers only a clearly newer/proven final plus useful unique geometry/recovery points.
No additional nonidentical variant has sufficient working-final evidence to authorize its deletion
in this audit. The review list records those uncertainties without retaining new duplicate archives.
