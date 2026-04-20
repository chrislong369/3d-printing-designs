from pathlib import Path
import shutil
import re

DRY_RUN = False  # CHANGE TO FALSE AFTER PREVIEW

ROOT = Path(__file__).parent
BOX_DIR = ROOT / "In_Progress" / "Boxes"
FINAL_DIR = ROOT / "Final_Products" / "Boxes"

FINAL_DIR.mkdir(parents=True, exist_ok=True)

EXTENSIONS = (".stl", ".3mf")

def extract_dimensions(name):
    name = name.lower()

    # match patterns like 6p9x6p9x5 OR 6.9x6.9x5
    match = re.search(r'(\d+[p\.]?\d*)x(\d+[p\.]?\d*)x(\d+[p\.]?\d*)', name)

    if not match:
        return None

    dims = []
    for g in match.groups():
        dims.append(g.replace('p', '.'))

    return dims  # [L, W, H]

def score_file(name):
    n = name.lower()

    score = 0

    if "final" in n:
        score += 5
    if "v5" in n or "v4" in n:
        score += 3
    if "taper" in n:
        score += 2
    if "connected" in n:
        score += 2
    if "upside" in n:
        score += 1

    return score

def main():
    files = [f for f in BOX_DIR.glob("*") if f.suffix.lower() in EXTENSIONS]

    groups = {}

    # group files by dimensions
    for f in files:
        dims = extract_dimensions(f.name)
        if not dims:
            continue

        key = "x".join(dims)

        if key not in groups:
            groups[key] = []

        groups[key].append(f)

    for dims, group_files in groups.items():
        best = max(group_files, key=lambda f: score_file(f.name))

        new_name = f"Box {dims} Open Bottom{best.suffix}"
        dest = FINAL_DIR / new_name

        if DRY_RUN:
            print(f"[KEEP] {best.name} → {new_name}")
        else:
            shutil.move(str(best), str(dest))
            print(f"MOVED {best.name} → {new_name}")

        # delete others
        for f in group_files:
            if f == best:
                continue

            if DRY_RUN:
                print(f"[DELETE] {f.name}")
            else:
                f.unlink()

    print("\nDONE")

if __name__ == "__main__":
    main()