"""Read-only asset audit; writes evidence, never moves or deletes models."""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args], cwd=ROOT)

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='origin/main')
    parser.add_argument('--geometry', action='store_true', help='Inspect STL meshes using trimesh')
    args = parser.parse_args()
    baseline = git('rev-parse', args.base).decode().strip()
    tracked = [p for p in git('ls-files', '-z').decode('utf-8').split('\0') if p]
    deleted = [p for p in git('diff', '--name-only', '-z', '--diff-filter=D', baseline).decode('utf-8').split('\0')
               if Path(p).suffix.lower() in {'.stl', '.3mf'}]
    deleted_hashes = {name: digest(git('show', baseline + ':' + name)) for name in deleted}
    models = [p for p in tracked if Path(p).suffix.lower() in {'.stl', '.3mf'} and (ROOT / p).exists()]
    by_hash = defaultdict(list)
    by_geometry = defaultdict(list)
    records = []
    for name in models:
        path = ROOT / name
        file_hash = digest(path.read_bytes())
        by_hash[file_hash].append(name)
        record = {'path': name, 'sha256': file_hash, 'bytes': path.stat().st_size}
        if path.suffix.lower() == '.3mf':
            try:
                with zipfile.ZipFile(path) as archive:
                    record['bad_zip_member'] = archive.testzip()
                    geometry = [(n, digest(archive.read(n))) for n in sorted(archive.namelist()) if n.lower().endswith('.model')]
                    record['geometry_members'] = len(geometry)
                    if geometry:
                        by_geometry[digest(json.dumps(geometry).encode())].append(name)
            except zipfile.BadZipFile:
                record['bad_zip_member'] = 'invalid ZIP'
        elif args.geometry:
            import trimesh
            try:
                mesh = trimesh.load_mesh(path, process=True)
                record.update(bounds_assuming_mm=mesh.bounds.tolist(), watertight=bool(mesh.is_watertight), triangles=len(mesh.faces))
            except Exception as error:
                record['mesh_error'] = str(error)
        records.append(record)
    proof = []
    for name in deleted:
        file_hash = deleted_hashes[name]
        proof.append({'deleted': name, 'sha256': file_hash, 'retained_identical': by_hash.get(file_hash, [])})
    report = {'baseline': baseline, 'models': records, 'deletion_proof': proof,
              'exact_duplicate_groups': [v for v in by_hash.values() if len(v) > 1],
              'same_3mf_geometry_review_groups': [v for v in by_geometry.values() if len(v) > 1]}
    output = ROOT / 'docs' / 'cleanup-audit.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    missing_keeper = [r for r in proof if not r['retained_identical']]
    bad_archives = [r['path'] for r in records if r.get('bad_zip_member')]
    print(json.dumps({'models': len(models), 'proved_duplicate_deletions': len(proof),
                      'unproved_deletions': missing_keeper, 'exact_duplicate_groups': report['exact_duplicate_groups'],
                      'same_3mf_geometry_review_groups': report['same_3mf_geometry_review_groups'],
                      'bad_archives': bad_archives, 'evidence': str(output)}, indent=2))
    if missing_keeper or bad_archives:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
