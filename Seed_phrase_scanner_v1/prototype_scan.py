import os
import re
from pathlib import Path 
import shutil
import zipfile

# ---CONFIG---

TARGET_DIR = Path("test_targets")  # Folder to scan
FOUND_DIR = Path("found")           # Where to move suspicious files
ARCHIVE_NAME = "Found.zip"          # Compressed output
MIN_WORD_COUNT = 12
MAX_WORD_COUNT = 24


# ---SETUP---
FOUND_DIR.mkdir(exist_ok=True) # CREATES found/ if not exists

# REGEX PATTERN: 12-24 lowercase words, each 3+ letters , separated by spaces
seed_pattern = re.compile(r'\b(?:[a-z]{3,}\s+){11,23}[a-z]{3,}\b')

# --- SCAN ---

for file_path in TARGET_DIR.glob("*.txt"):
    with file_path.open("r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        if seed_pattern.search(content):
            print(f"[!] Possible seed phrase in: {file_path.name}")
            shutil.copy(file_path, FOUND_DIR)

# --- COMPRESS ---
with zipfile.ZipFile(ARCHIVE_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file_path in FOUND_DIR.glob("*.txt"):
        zipf.write(file_path, arcname=file_path.name)

print(f"\n✅ Scan complete. Results saved in: {FOUND_DIR}/ and {ARCHIVE_NAME}")

