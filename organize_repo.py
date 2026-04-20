from pathlib import Path
import shutil

# =========================
# SETTINGS
# =========================
DRY_RUN = False  # CHANGE TO FALSE AFTER PREVIEW

ROOT = Path(__file__).parent

TARGETS = {
    "personal": ROOT / "Personal",
    "boxes": ROOT / "In_Progress" / "Boxes",
    "cosmetic": ROOT / "In_Progress" / "Cosmetic_Organizers",
    "utility": ROOT / "In_Progress" / "Utility_Designs",
    "downloaded": ROOT / "Downloaded_Models",
    "review": ROOT / "Needs_Review",
}

EXTENSIONS = (".stl", ".3mf")

# =========================
# CLASSIFICATION
# =========================
def classify(name):
    n = name.lower()

    # PERSONAL
    if any(x in n for x in [
        "silverado", "yeti", "cupholder", "cup_holder", "poop",
        "milwaukee", "gridfinity", "rod", "fishing",
        "belt", "blower", "purge", "dust", "cover",
        "glass_riser", "cleaner"
    ]):
        return "personal"

    # BOXES
    if any(x in n for x in [
        "open_bottom_box", "open.bottom.box", "box_", "upside_down"
    ]):
        return "boxes"

    # COSMETIC PRODUCTS
    if any(x in n for x in [
        "brow", "mascara", "tray", "holder_box"
    ]):
        return "cosmetic"

    # LONGWORKS / UTILITY DESIGNS
    if "longworks" in n:
        return "utility"

    # DOWNLOADED MODELS (junk / not yours)
    if any(x in n for x in [
        "glock", "claymore", "middle_finger",
        "teabox", "washing", "cone", "darrieus",
        "cr2032"
    ]):
        return "downloaded"

    return "review"


# =========================
# MOVE LOGIC
# =========================
def move_file(file):
    category = classify(file.name)
    target_dir = TARGETS[category]
    target_dir.mkdir(parents=True, exist_ok=True)

    dest = target_dir / file.name

    # avoid overwrite
    counter = 2
    while dest.exists():
        dest = target_dir / f"{file.stem}__dup{counter}{file.suffix}"
        counter += 1

    if DRY_RUN:
        print(f"[DRY RUN] {file} → {dest}")
    else:
        shutil.move(str(file), str(dest))
        print(f"MOVED {file} → {dest}")


# =========================
# MAIN
# =========================
def main():
    files = [f for f in ROOT.rglob("*") if f.suffix.lower() in EXTENSIONS]

    for f in files:
        if any(x in f.parts for x in [
            "Final_Products", "In_Progress", "Personal",
            "Downloaded_Models", "Needs_Review", ".git"
        ]):
            continue

        move_file(f)


if __name__ == "__main__":
    main()