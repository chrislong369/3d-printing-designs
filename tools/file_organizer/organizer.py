"""Preview model intake; use --apply to move into Needs_Review. Never delete."""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = Path(__file__).with_name('rules.json')

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--config', type=Path, default=DEFAULT_CONFIG)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true')
    mode.add_argument('--dry-run', action='store_true', help='Default behavior; retained for compatibility')
    args = parser.parse_args()
    source = Path(args.source).expanduser().resolve()
    if not source.is_dir():
        parser.error('Source must be an existing folder')
    if source == ROOT or source in ROOT.parents:
        parser.error('Source must not be the repository or one of its parents')
    if ROOT in source.parents and source != ROOT / '3D_DROP':
        parser.error('Only 3D_DROP may be scanned inside this repository')
    config = json.loads(args.config.read_text(encoding='utf-8'))
    destination = (ROOT / config['destination']).resolve()
    if destination != ROOT / 'Needs_Review':
        parser.error('Intake destination must be Needs_Review; classification requires review')
    extensions = set(config['extensions'])
    files = sorted(p for p in source.iterdir() if p.is_file() and not p.is_symlink()
                   and p.suffix.lower() in extensions)
    reserved = set()
    for path in files:
        target = destination / path.name
        if target.exists() and hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(target.read_bytes()).digest():
            print(f'SKIP identical retained file; source preserved: {path.name}')
            continue
        counter = 2
        while target.exists() or target in reserved:
            target = destination / f'{path.stem}__intake{counter}{path.suffix}'
            counter += 1
        reserved.add(target)
        print(f'{"MOVE" if args.apply else "PREVIEW"} {path} -> {target}')
        if args.apply:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(target))
    print(f'{len(files)} models inspected; {"applied" if args.apply else "no files changed"}')

if __name__ == '__main__':
    main()
