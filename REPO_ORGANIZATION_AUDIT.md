# Repo Organization Audit

This audit was created after the bulk upload so the repository can be normalized without guessing.

## Current Situation

The repository currently contains:
- the new standard folders: `Final_Products/`, `In_Progress/`, `Personal/`, `Needs_Review/`
- an older folder scheme that conflicts with the new structure:
  - `01_FINAL_PRODUCTS/`
  - `02_GRID_SYSTEM/`
  - `03_IN_PROGRESS/`
  - `04_ARCHIVE/`
  - `05_PRINT_PROFILES/`
- a catch-all dump folder: `Bulk files need organizing/`

## Obvious Personal Files

These should ultimately live under `Personal/`:
- `Bulk files need organizing/2019 silverado_yeti_46oz_final.3mf`
- `Bulk files need organizing/silverado_yeti_46oz_final_v1.stl`
- `Bulk files need organizing/silverado_yeti_46oz_final_v2_connected.stl`
- `Bulk files need organizing/silverado_yeti_46oz_final_v3_stepwall_10275.stl`
- `Bulk files need organizing/silverado_yeti_46oz_final_v4_connected_step_10275.stl`
- `Bulk files need organizing/silverado_yeti_46oz_final_v5_tapered_base_695_to_78.stl`
- `Bulk files need organizing/yeti_cup_holder_adapter.stl`
- `Bulk files need organizing/test_puck_cupholder_78mm_OD_5mm_tall.stl`
- `Bulk files need organizing/test_ring_bottle_103mm_ID_3mm_tall.stl`
- `Bulk files need organizing/Poop_Bag_Dispenser_Set_3MF.3mf`
- `Bulk files need organizing/poop_bag_dispenser_extra_roll_right_side_v2.stl`
- `Bulk files need organizing/poop_bag_dispenser_final_rebuild.stl`
- `Bulk files need organizing/poop_bag_dispenser_v3_rebuilt.stl`
- `Bulk files need organizing/poop_bag_dispenser_with_extra_roll_holder.stl`

## Obvious Open-Bottom Box Files

These appear to be part of the user-created box series and should ultimately be renamed into the detailed naming format and split between `Final_Products/` and `In_Progress/` based on the latest working version.

Candidate files:
- `Bulk files need organizing/box_6_9in_x_6_9in_x_5in_open_bottom_shell.3mf`
- `Bulk files need organizing/open_bottom_box_3x3x1_upside_down.3mf`
- `Bulk files need organizing/open_bottom_box_4x4x1_upside_down_0p15in_thick.3mf`
- `Bulk files need organizing/open_bottom_box_4x4x2_upside_down_0p15in_thick.3mf`
- `Bulk files need organizing/open_bottom_box_4x4x2_upside_down_0p15in_thick.stl`
- `Bulk files need organizing/open_bottom_box_4p9x4p9x3_upside_down_0p15in_thick.3mf`
- `Bulk files need organizing/open_bottom_box_5p9x5p9x4_upside_down_0p15in_thick.3mf`
- `Bulk files need organizing/open_bottom_box_5p9x5p9x4_upside_down_0p15in_thick.stl`
- `Bulk files need organizing/open_bottom_box_7p9x7p9x6in.3mf`
- `Bulk files need organizing/open_bottom_box_7p9x7p9x6in.stl`
- `Bulk files need organizing/open_bottom_box_7p9x7p9x6in_upside_down_print.stl`
- `Bulk files need organizing/open_bottom_box_8p8x8p8x6p5_upside_down_0p15in_thick.stl`
- `Bulk files need organizing/open_bottom_box_9p8x9p8x7_upside_down_0p15in_thick.stl`

## Obvious Cosmetic / Product Tray Files

These look like user-created or user-relevant sellable product families and should be reviewed for `Final_Products/` vs `In_Progress/`:
- brow holder files
- brow liner holder files
- brow pen holder files
- mascara inventory tray files
- compartment tray files
- tray rib / tile variants

## Obvious Workshop / Utility Files

These are not clearly personal, but they also are not yet confirmed as product-ready. They likely belong in `Needs_Review/` unless the user confirms otherwise:
- Milwaukee holder / battery mount files
- Gridfinity / tray / insert press files
- fishing rod holder / rod holster files
- LongWorks Studio text and nameplate files
- printer accessories like belt dust cover, glass riser hole covers, purge strip bin, blower mount

## Obvious Downloaded / Generic Files That Need Review

These appear to be outside the user-created product line and should not be mixed into final product folders without review:
- `Claymore_Mine.3mf`
- `Glock_19__Business_Card_Holder.3mf`
- `Ovetto_Middle_Finger_Textured.3mf`
- `washing_bowl.3mf`
- `CR2032.3mf`
- `ConeStand.3mf`
- `Darrieus_V5.3mf`
- `Clean-Dirty_Dishwasher_Sign.3mf`
- `Teabox_Stackable.3mf`
- `左手版本-p1s.3mf`
- other generic downloaded models under `Bulk files need organizing/`

## Immediate Cleanup Priorities

1. Eliminate the old legacy folder structure in favor of the new standard folders.
2. Move obvious personal files into `Personal/`.
3. Rename the box series into the detailed naming format.
4. Separate likely sellable cosmetic / tray designs from generic downloaded files.
5. Put everything uncertain into `Needs_Review/` instead of guessing.
