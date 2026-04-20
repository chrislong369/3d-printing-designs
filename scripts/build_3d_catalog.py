#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path('.')
OUTPUT_DIR = ROOT / 'docs'
MD_PATH = OUTPUT_DIR / '3d-catalog.md'
CSV_PATH = OUTPUT_DIR / '3d-catalog.csv'
JSON_PATH = OUTPUT_DIR / '3d-catalog.json'

MODEL_EXTS = {'.stl', '.3mf'}


def iter_model_files() -> list[Path]:
    return [p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in MODEL_EXTS]


def build_records(paths: list[Path]) -> list[dict]:
    records = []
    for p in paths:
        rel = p.relative_to(ROOT)
        parts = rel.parts
        category = parts[0] if parts else 'Unknown'
        size_mb = p.stat().st_size / (1024 * 1024)
        records.append({
            'path': str(rel),
            'name': p.name,
            'category': category,
            'extension': p.suffix.lower(),
            'size_mb': round(size_mb, 3),
        })
    return sorted(records, key=lambda r: (r['category'], r['name']))


def write_csv(records: list[dict]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['path', 'name', 'category', 'extension', 'size_mb'])
        writer.writeheader()
        writer.writerows(records)


def write_json(records: list[dict]) -> None:
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    with JSON_PATH.open('w', encoding='utf-8') as f:
        json.dump(records, f, indent=2)


def write_markdown(records: list[dict]) -> None:
    counts = Counter(r['category'] for r in records)

    lines = [
        '# 3D Model Catalog',
        '',
        f'Total models: {len(records)}',
        '',
        '## By Category',
    ]

    for cat, count in sorted(counts.items()):
        lines.append(f'- {cat}: {count}')

    lines.append('')
    lines.append('## Files')
    lines.append('')

    for r in records:
        lines.append(f"- **{r['name']}**  ")
        lines.append(f"  - Path: `{r['path']}`  ")
        lines.append(f"  - Category: {r['category']}  ")
        lines.append(f"  - Size: {r['size_mb']} MB  ")
        lines.append('')

    MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    MD_PATH.write_text('\n'.join(lines), encoding='utf-8')


def main() -> None:
    paths = iter_model_files()
    records = build_records(paths)
    write_csv(records)
    write_json(records)
    write_markdown(records)
    print(f'Catalog generated with {len(records)} models.')


if __name__ == '__main__':
    main()
