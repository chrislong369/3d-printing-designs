# File Organizer Tool

This tool helps automatically organize your 3D printing files into a clean folder structure.

## What it does
- Scans a folder you point it to
- Sorts files based on rules (STL, 3MF, naming keywords, etc.)
- Moves them into your repo structure

## Example Use

Preview (safe):
```
python tools/file_organizer/organizer.py --source "C:/your/downloads" --dry-run
```

Run for real:
```
python tools/file_organizer/organizer.py --source "C:/your/downloads"
```

## How to Customize
Edit `rules.json` to change:
- where files go
- what keywords trigger sorting
- what extensions get moved

## Typical Workflow
1. Download or export files from Bambu Studio
2. Drop them into a temp folder
3. Run organizer
4. Files get sorted into your repo automatically

## Why this exists
To eliminate manual file dragging and keep your 3D printing business clean and scalable.
