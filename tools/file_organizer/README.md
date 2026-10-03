# Model intake

The maintained organizer previews immediate model files in a drop folder. It never deletes,
never overwrites, never scans linked subfolders, and never infers final status from a filename.
All incoming models go to Needs_Review for classification and license/geometry review.
Paths resolve against this repository regardless of the shell's working directory.

Preview: python tools/file_organizer/organizer.py --source "C:/your/drop-folder"

Apply reviewed moves: add --apply. --dry-run is also accepted and creates no directories.
An identical existing destination is skipped; the source is preserved.
Within this repository only 3D_DROP is accepted as an intake source.
