import os
import re
from pathlib import Path
import shutil
import zipfile
import csv

# --- CONFIG ---
TARGET_DIR = Path("test_targets")
FOUND_DIR = Path("found")
ARCHIVE_NAME = "found2.zip"
WORDLIST_PATH = Path("bip39_english.txt")
RESULT_LOG = Path("results.csv")
MIN_WORDS = 12
MAX_WORDS = 24

# --- LOAD BIP39 WORDLIST ---
with WORDLIST_PATH.open("r", encoding="utf-8") as f:
    bip39_words = set(word.strip() for word in f if word.strip())

# --- FUNCTION: Get first matching 12–24-word BIP39 chunk ---
def find_bip39_seed(text):
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    for i in range(len(words) - MIN_WORDS + 1):
        for length in range(MIN_WORDS, min(MAX_WORDS, len(words) - i) + 1):
            chunk = words[i:i + length]
            if all(word in bip39_words for word in chunk):
                return ' '.join(chunk)
    return None

# --- SETUP ---
FOUND_DIR.mkdir(exist_ok=True)
RESULT_LOG.write_text("filename,matched_seed_phrase\n")  # Reset CSV on each run

# --- SCAN FILES ---
for file_path in TARGET_DIR.glob("*.txt"):
    with file_path.open("r", encoding="utf-8", errors="ignore") as file:
        content = file.read()
        matched_seed = find_bip39_seed(content)
        if matched_seed:
            print(f"\n[✅] Valid seed in: {file_path.name}")
            print(f"     ↳ Matched: \033[92m{matched_seed}\033[0m")  # Green highlight
            shutil.copy(file_path, FOUND_DIR)
            with RESULT_LOG.open("a", encoding="utf-8", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_path.name, matched_seed])
        else:
            print(f"[ ] No valid seed in: {file_path.name}")

# --- COMPRESS RESULTS ---
with zipfile.ZipFile(ARCHIVE_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file_path in FOUND_DIR.glob("*.txt"):
        zipf.write(file_path, arcname=file_path.name)

print(f"\n🎉 Done. Matches logged to: {RESULT_LOG}")
print(f"📦 Flagged files stored in: {FOUND_DIR}/ and {ARCHIVE_NAME}")

