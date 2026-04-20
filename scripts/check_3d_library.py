#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ALLOWED_TOP_LEVEL_DIRS = {
    'Final_Products',
    'In_Progress',
    'Personal',
    'Downloaded_Models',
    'Needs_Review',
    '.github',
    'scripts',
    'docs',
}

ALLOWED_MODEL_EXTENSIONS = {'.stl', '.3mf'}
ALLOWED_NON_MODEL_FILES = {
    '.md', '.txt', '.py', '.yml', '.yaml', '.gitignore', '.gitattributes', '.csv', '.json'
}


def run_git_diff(base: str, head: str) -> list[str]:
    cmd = ['git', 'diff', '--name-only', '--diff-filter=ACMR', base, head]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def all_tracked_files() -> list[str]:
    cmd = ['git', 'ls-files']
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def has_bad_filename_style(path: Path) -> list[str]:
    warnings: list[str] = []
    name = path.name
    stem = path.stem

    if '_' in stem:
        warnings.append('uses underscores in the filename; prefer readable names with spaces')
    if '  ' in stem:
        warnings.append('contains double spaces')
    if stem != stem.strip():
        warnings.append('has leading or trailing spaces in the filename')
    if any(ch in stem for ch in ['[', ']', '{', '}', '(', ')']):
        warnings.append('contains bracket characters; keep product filenames simple')

    return warnings


def validate_path(path_str: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = Path(path_str)
    parts = path.parts

    if not parts:
        errors.append('empty path')
        return errors, warnings

    top_level = parts[0]
    if top_level not in ALLOWED_TOP_LEVEL_DIRS:
        errors.append(
            f'top-level folder {top_level!r} is not allowed; use one of: {", ".join(sorted(ALLOWED_TOP_LEVEL_DIRS - {".github", "scripts", "docs"}))}'
        )
        return errors, warnings

    suffix = path.suffix.lower()
    if suffix in ALLOWED_MODEL_EXTENSIONS:
        if len(parts) < 2:
            warnings.append('model file is at repo root of its top-level folder; consider a product subfolder if this grows')
        warnings.extend(has_bad_filename_style(path))
        return errors, warnings

    if top_level in {'.github', 'scripts', 'docs'} and suffix in ALLOWED_NON_MODEL_FILES:
        return errors, warnings

    if suffix in ALLOWED_NON_MODEL_FILES:
        return errors, warnings

    warnings.append(f'non-model file type {suffix or "<no extension>"!r} found at {path_str}')
    return errors, warnings


def print_group(title: str, items: list[str]) -> None:
    if not items:
        return
    print(f'\n{title}')
    for item in items:
        print(f'- {item}')


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate STL/3MF library structure and naming.')
    parser.add_argument('--base', help='Base git SHA for changed-files scan')
    parser.add_argument('--head', help='Head git SHA for changed-files scan')
    parser.add_argument('--full', action='store_true', help='Scan all tracked files instead of only changed files')
    args = parser.parse_args()

    if args.full:
        files = all_tracked_files()
        mode = 'full repository scan'
    elif args.base and args.head:
        files = run_git_diff(args.base, args.head)
        mode = f'changed-files scan ({args.base[:7]}..{args.head[:7]})'
    else:
        files = all_tracked_files()
        mode = 'fallback full repository scan'

    print(f'Running {mode}')

    model_files = [
        f for f in files
        if Path(f).suffix.lower() in ALLOWED_MODEL_EXTENSIONS
    ]

    errors: list[str] = []
    warnings: list[str] = []

    for file_path in files:
        file_errors, file_warnings = validate_path(file_path)
        errors.extend([f'{file_path}: {msg}' for msg in file_errors])
        warnings.extend([f'{file_path}: {msg}' for msg in file_warnings])

    summary_lines = [
        '## 3D Library Check Summary',
        '',
        f'- Files scanned: {len(files)}',
        f'- Model files scanned: {len(model_files)}',
        f'- Errors: {len(errors)}',
        f'- Warnings: {len(warnings)}',
        '',
    ]

    step_summary = os.getenv('GITHUB_STEP_SUMMARY')
    if step_summary:
        with open(step_summary, 'a', encoding='utf-8') as fh:
            fh.write('\n'.join(summary_lines))
            if errors:
                fh.write('### Errors\n')
                for item in errors[:50]:
                    fh.write(f'- {item}\n')
            if warnings:
                fh.write('### Warnings\n')
                for item in warnings[:50]:
                    fh.write(f'- {item}\n')

    print_group('Errors', errors)
    print_group('Warnings', warnings)

    if errors:
        print('\nValidation failed.')
        return 1

    print('\nValidation passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
