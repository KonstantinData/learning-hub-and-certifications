
#!/usr/bin/env python3
"""
organize_certificates_by_topic.py
Reorganize certificates into topic folders for the repo 'learning-hub-and-certifications'.

- Creates topic folders if missing
- Moves known certificate files into the corresponding topic folder
- Skips .git and leaves non-matching files untouched
- Safe: only moves files that exist

Usage:
  python organize_certificates_by_topic.py
"""

import os
import shutil
from pathlib import Path

# Root: current working directory (run this from your repo root)
ROOT = Path(".")

# Where the files currently are (adjust if your files are elsewhere, e.g., in "./certificates")
SEARCH_DIRS = [ROOT, ROOT / "certificates"]

# Topic folders to create
TOPIC_DIRS = {
    "01_AI_and_Prompt_Engineering": [
        "Coursera Advanced Prompt Engineering FK0CK21OLAY4.pdf",
        "Coursera M2YMZQK1THQA GOOGLE Introduction to AI.pdf",
        "Coursera DT0XYZO56DNL Google AI Essentials.pdf",
        "ai_python_for_beginners_id2457.png",
        "agentic_ai_id2601.png",
        "Konstantin_Milonas_Data_Science_Fundamentals_english.pdf",
    ],
    "02_Data_Analytics_and_Tableau": [
        "Datacamp Analyzing Data in Tableau.pdf",
        "Datacamp Calculations in Tableau.pdf",
        "Datacamp Statistical Techniques in Tableau.pdf",
        "Coursera Data Ecosystem 1FBABXJDT2JH.pdf",
        "Konstantin_Milonas_Data_Science_Fundamentals_german.pdf",
    ],
    "03_Python_and_Tools": [
        "Datacamp Intermediate Python.pdf",
        "Datacamp introduction to GitHub Concepts.pdf",
        "Coursera Getting started with Python 65VKNHGM21R2.pdf",
        "Coursera Manage Git Versions D9T3WRHTLBHR.pdf",
    ],
    "04_Productivity_and_AI_Workflows": [
        "Coursera 28G90KJ018BR Maximize Productivity With AI Tools.pdf",
    ],
}

EXCLUDE_DIRS = {".git", ".github", "__pycache__"}

def ensure_dirs():
    for topic in TOPIC_DIRS.keys():
        Path(topic).mkdir(parents=True, exist_ok=True)

def find_file_anywhere(fname: str) -> Path | None:
    for base in SEARCH_DIRS:
        if not base.exists():
            continue
        for root, dirs, files in os.walk(base):
            # prune excluded dirs
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            if fname in files:
                return Path(root) / fname
    return None

def move_files():
    moved = []
    missing = []
    for topic, files in TOPIC_DIRS.items():
        for fname in files:
            src = find_file_anywhere(fname)
            if src and src.is_file():
                dest = Path(topic) / fname
                # Skip if already in place
                if src.resolve() == dest.resolve():
                    continue
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
                moved.append((str(src), str(dest)))
            else:
                missing.append(fname)
    return moved, missing

def main():
    ensure_dirs()
    moved, missing = move_files()

    print("=== Summary ===")
    if moved:
        print(f"Moved {len(moved)} file(s):")
        for s, d in moved:
            print(f"  - {s} -> {d}")
    else:
        print("No files moved.")

    if missing:
        print(f"\nMissing {len(missing)} file(s) (not found):")
        for m in missing:
            print(f"  - {m}")

if __name__ == "__main__":
    main()
