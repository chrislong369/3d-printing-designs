from pathlib import Path
import shutil
import re

DRY_RUN = False  # CHANGE TO FALSE AFTER PREVIEW

ROOT = Path(__file__).parent

DIR_FINAL = ROOT / "Final_Products"
DIR_INPROGRESS = ROOT / "In_Progress"
DIR_PERSONAL = ROOT / "Personal"
DIR_DOWNLOADED = ROOT / "Downloaded_Models"
DIR_REVIEW = ROOT / "Needs_Review"

BOX_FINAL = DIR_FINAL / "Boxes"
COSMETIC_FINAL = DIR_FINAL / "Cosmetic_Organizers"
UTILITY_INPROGRESS = DIR_INPROGRESS / "Utility_Designs"
COSMETIC_INPROGRESS = DIR_INPROGRESS / "Cosmetic_Organizers"
BOX_INPROGRESS = DIR_INPROGRESS / "Boxes"

ALL_TARGET_DIRS = [
    BOX_FINAL,
    COSMETIC_FINAL,
    UTILITY_INPROGRESS,
    COSMETIC_INPROGRESS,
    BOX_INPROGRESS,
    DIR_PERSONAL,
    DIR_DOWNLOADED,
    DIR_REVIEW,
]

EXTENSIONS = (".stl", ".3mf")

DOWNLOADED_PATTERNS = [
    "glock", "claymore", "middle_finger", "teabox", "washing",
    "cone", "darrieus", "cr2032", "左手版本"
]

PERSONAL_PATTERNS = [
    "silverado", "yeti", "cupholder", "cup_holder", "poop",
    "milwaukee", "gridfinity", "rod_holster", "fishing_rod",
    "fishing", "belt", "blower", "purge", "dust_cover",
    "glass_riser", "cleaner", "pet_water_bowl"
]

UTILITY_PATTERNS = [
    "longworks", "nameplate", "3d-text", "words_only", "words_thicker"
]

COSMETIC_PATTERNS = [
    "brow", "mascara", "inventory_tray", "retail_display",
    "compartment_tray", "holder_box", "brow_pen_holder",
    "brow_liner_holder", "brow_holders"
]

BOX_HINTS = [
    "open_bottom_box", "open.bottom.box", "box_", "upside_down",
    "open_bottom", "open bottom"
]


def log(msg):
    print(msg)


def norm(text: str) -> str:
    return text.lower().replace("-", "_").replace(" ", "_")


def ensure_dirs():
    for d in ALL_TARGET_DIRS:
        d.mkdir(parents=True, exist_ok=True)


def unique_path(dest: Path) -> Path:
    if not dest.exists():
        return dest
    i = 2
    while True:
        candidate = dest.with_name(f"{dest.stem}__dup{i}{dest.suffix}")
        if not candidate.exists():
            return candidate
        i += 1


def is_in_target_folder(path: Path) -> bool:
    target_names = {
        "Final_Products", "In_Progress", "Personal",
        "Downloaded_Models", "Needs_Review", ".git", "__pycache__"
    }
    return any(part in target_names for part in path.parts)


def gather_loose_files():
    files = []
    for f in ROOT.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix.lower() not in EXTENSIONS:
            continue
        if is_in_target_folder(f):
            continue
        files.append(f)
    return files


def gather_files_in(folder: Path):
    if not folder.exists():
        return []
    return [f for f in folder.glob("*") if f.is_file() and f.suffix.lower() in EXTENSIONS]


def move_file(src: Path, dest_dir: Path, new_name: str = None):
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (new_name if new_name else src.name)
    dest = unique_path(dest)

    if DRY_RUN:
        log(f"[MOVE] {src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
    else:
        shutil.move(str(src), str(dest))


def delete_file(path: Path):
    if DRY_RUN:
        log(f"[DELETE] {path.relative_to(ROOT)}")
    else:
        path.unlink(missing_ok=True)


def classify_loose_file(name: str):
    n = norm(name)

    if any(x in n for x in DOWNLOADED_PATTERNS):
        return "downloaded"

    if any(x in n for x in PERSONAL_PATTERNS):
        return "personal"

    if any(x in n for x in UTILITY_PATTERNS):
        return "utility"

    if any(x in n for x in COSMETIC_PATTERNS):
        return "cosmetic"

    if any(x in n for x in BOX_HINTS):
        return "box"

    if "test" in n:
        return "review"

    return "review"


def sort_loose_files():
    loose = gather_loose_files()
    for f in loose:
        category = classify_loose_file(f.name)
        if category == "downloaded":
            move_file(f, DIR_DOWNLOADED)
        elif category == "personal":
            move_file(f, DIR_PERSONAL)
        elif category == "utility":
            move_file(f, UTILITY_INPROGRESS)
        elif category == "cosmetic":
            move_file(f, COSMETIC_INPROGRESS)
        elif category == "box":
            move_file(f, BOX_INPROGRESS)
        else:
            move_file(f, DIR_REVIEW)


def extract_box_dimensions(name: str):
    n = norm(name)
    match = re.search(r'(\d+[p\.]?\d*)x(\d+[p\.]?\d*)x(\d+[p\.]?\d*)', n)
    if not match:
        return None
    dims = [g.replace("p", ".") for g in match.groups()]
    return dims


def score_box(name: str):
    n = norm(name)
    score = 0
    if "final" in n:
        score += 8
    if "v5" in n:
        score += 6
    if "v4" in n:
        score += 5
    if "v3" in n:
        score += 4
    if "taper" in n or "tapered" in n:
        score += 3
    if "connected" in n:
        score += 2
    if "step" in n:
        score += 2
    if "upside" in n:
        score += 1
    if n.endswith(".3mf"):
        score += 2
    return score


def finalize_boxes():
    files = gather_files_in(BOX_INPROGRESS)
    groups = {}

    for f in files:
        dims = extract_box_dimensions(f.name)
        if not dims:
            move_file(f, DIR_REVIEW)
            continue
        key = "x".join(dims)
        groups.setdefault(key, []).append(f)

    for dims, group in groups.items():
        best = max(group, key=lambda f: score_box(f.name))
        new_name = f"Box {dims} Open Bottom{best.suffix}"
        move_file(best, BOX_FINAL, new_name)

        for f in group:
            if f == best:
                continue
            delete_file(f)


def cosmetic_family(name: str):
    n = norm(name)
    if "mascara" in n:
        return "Mascara"
    if "brow_liner" in n:
        return "Brow Liner"
    if "brow_pen" in n:
        return "Brow Pen"
    if "brow" in n:
        return "Brow"
    if "tray" in n:
        return "Tray"
    return "Cosmetic"


def cosmetic_is_final_candidate(name: str):
    n = norm(name)
    positive = ["final", "production", "retail_display_enclosed", "top_holes_fixed", "strong_light_v2", "v3", "v4", "v5"]
    negative = ["test", "__dup", "one_plate"]
    if any(x in n for x in negative):
        return False
    return any(x in n for x in positive)


def safe_cosmetic_name(name: str):
    family = cosmetic_family(name)
    ext = Path(name).suffix
    return f"{family} Organizer{ext}"


def finalize_cosmetics():
    files = gather_files_in(COSMETIC_INPROGRESS)
    for f in files:
        if cosmetic_is_final_candidate(f.name):
            move_file(f, COSMETIC_FINAL, safe_cosmetic_name(f.name))
        else:
            # keep non-final cosmetic files in progress, but normalize if needed
            pass


def utility_is_english_problem(name: str):
    return any(ord(ch) > 127 for ch in name)


def finalize_utilities():
    files = gather_files_in(UTILITY_INPROGRESS)
    for f in files:
        n = norm(f.name)
        if utility_is_english_problem(f.name):
            new_name = f"Utility Design Untranslated{f.suffix}"
            move_file(f, DIR_REVIEW, new_name)
            continue

        if "longworks" in n and "nameplate" in n:
            move_file(f, UTILITY_INPROGRESS, f"LongWorks Studio Nameplate{f.suffix}")
        elif "longworks" in n and "words_only" in n:
            move_file(f, UTILITY_INPROGRESS, f"LongWorks Studio Words Only{f.suffix}")
        elif "longworks" in n and "words_thicker" in n:
            move_file(f, UTILITY_INPROGRESS, f"LongWorks Studio Words Thicker{f.suffix}")
        elif "3d_text" in n or "3d-text" in n:
            move_file(f, UTILITY_INPROGRESS, f"LongWorks Studio 3D Text{f.suffix}")


def remove_empty_legacy_dirs():
    legacy = [
        ROOT / "01_FINAL_PRODUCTS",
        ROOT / "02_GRID_SYSTEM",
        ROOT / "03_IN_PROGRESS",
        ROOT / "04_ARCHIVE",
        ROOT / "05_PRINT_PROFILES",
        ROOT / "Bulk files need organizing",
    ]
    for d in legacy:
        if d.exists():
            try:
                if DRY_RUN:
                    log(f"[REMOVE DIR IF EMPTY] {d.relative_to(ROOT)}")
                else:
                    d.rmdir()
            except OSError:
                # not empty, leave it alone
                pass


def main():
    ensure_dirs()
    sort_loose_files()
    finalize_boxes()
    finalize_cosmetics()
    finalize_utilities()
    remove_empty_legacy_dirs()
    log("\nDONE")
    if DRY_RUN:
        log("Preview only. If this looks right, change DRY_RUN = False and run again.")


if __name__ == "__main__":
    main()