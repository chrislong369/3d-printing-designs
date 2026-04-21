#!/usr/bin/env python3
"""Custom file organizer for the 3D printing repo.

Usage examples:
  python tools/file_organizer/organizer.py --source "/path/to/drop-folder"
  python tools/file_organizer/organizer.py --source "/path/to/drop-folder" --dry-run
  python tools/file_organizer/organizer.py --source "/path/to/drop-folder" --config tools/file_organizer/rules.json

What it does:
- Walks a source folder recursively
- Skips excluded folders
- Moves files into configured destination folders based on rules
- Supports extension-based and filename-keyword-based routing
- Adds numeric suffixes to avoid overwriting existing files

This script uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class MatchRule:
    name: str
    destination: str
    extensions: list[str]
    name_contains: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MatchRule":
        return cls(
            name=str(data.get("name", "unnamed-rule")),
            destination=str(data["destination"]),
            extensions=[str(x).lower() for x in data.get("extensions", [])],
            name_contains=[str(x).lower() for x in data.get("name_contains", [])],
        )

    def matches(self, file_path: Path) -> bool:
        suffix = file_path.suffix.lower()
        stem = file_path.stem.lower()

        extension_match = bool(self.extensions) and suffix in self.extensions
        keyword_match = bool(self.name_contains) and any(keyword in stem for keyword in self.name_contains)

        if self.extensions and self.name_contains:
            return extension_match and keyword_match
        if self.extensions:
            return extension_match
        if self.name_contains:
            return keyword_match
        return False


def load_config(config_path: Path) -> dict[str, Any]:
    with config_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def should_skip(path: Path, source_root: Path, excluded_dirs: set[str]) -> bool:
    try:
        relative_parts = path.relative_to(source_root).parts
    except ValueError:
        return True

    return any(part in excluded_dirs for part in relative_parts[:-1])


def resolve_target_path(destination_dir: Path, original_name: str) -> Path:
    destination_dir.mkdir(parents=True, exist_ok=True)
    candidate = destination_dir / original_name

    if not candidate.exists():
        return candidate

    stem = Path(original_name).stem
    suffix = Path(original_name).suffix
    counter = 1

    while True:
        candidate = destination_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_files(source: Path, config: dict[str, Any], dry_run: bool) -> tuple[int, int]:
    repo_root = Path(config.get("repo_root", ".")).resolve()
    excluded_dirs = set(config.get("excluded_directories", []))
    rules = [MatchRule.from_dict(item) for item in config.get("rules", [])]
    default_destination = config.get("default_destination")

    moved = 0
    inspected = 0

    for file_path in source.rglob("*"):
        if not file_path.is_file():
            continue
        if should_skip(file_path, source, excluded_dirs):
            continue

        inspected += 1
        matched_rule: MatchRule | None = None

        for rule in rules:
            if rule.matches(file_path):
                matched_rule = rule
                break

        if matched_rule is not None:
            destination = repo_root / matched_rule.destination
        elif default_destination:
            destination = repo_root / str(default_destination)
        else:
            print(f"SKIP  {file_path} -> no rule matched")
            continue

        target_path = resolve_target_path(destination, file_path.name)
        print(f"MOVE  {file_path} -> {target_path}")

        if not dry_run:
            shutil.move(str(file_path), str(target_path))

        moved += 1

    return inspected, moved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Organize files into repo folders based on JSON rules.")
    parser.add_argument("--source", required=True, help="Folder to scan and organize")
    parser.add_argument(
        "--config",
        default="tools/file_organizer/rules.json",
        help="Path to the JSON config file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without moving files",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    config_path = Path(args.config).expanduser().resolve()

    if not source.exists() or not source.is_dir():
        raise SystemExit(f"Source folder does not exist or is not a directory: {source}")

    if not config_path.exists() or not config_path.is_file():
        raise SystemExit(f"Config file does not exist: {config_path}")

    config = load_config(config_path)
    inspected, moved = organize_files(source, config, dry_run=args.dry_run)

    mode = "DRY RUN" if args.dry_run else "LIVE RUN"
    print("-" * 60)
    print(f"{mode} complete")
    print(f"Files inspected: {inspected}")
    print(f"Files moved: {moved}")


if __name__ == "__main__":
    main()
