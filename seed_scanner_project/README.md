# 🧼 Seed Phrase Scanner & Sanitizer

A secure Python tool to scan, detect, and sanitize **cryptocurrency seed phrases** (BIP39 mnemonics) from files or folders. Built for developers, sysadmins, and pentesters to **prevent sensitive data leaks**.

---

## 📦 Features

- 🔎 Detects valid 12–24 word BIP39 phrases
- 🔐 Redacts or hashes seed phrases irreversibly
- 🧠 Uses SHA-256 cryptographic hashing
- 📁 Works on individual files or whole directories
- 📄 Supports `.txt`, `.log`, `.json`, `.csv`, `.md`, `.py`, etc.
- 🔁 Non-destructive by default (creates `.sanitized` copies)
- 🧷 Option to keep or skip file backups

---

## 🗃️ File Structure

seed_scanner_project/
├── seed_scanner.py # Main Python script
├── bip39_wordlist.txt # 2048-word BIP39 dictionary
├── sample_data/ # Folder with test files
│ └── test1.txt # Example input file
├── README.md # You're reading it



---

## 🔐 How SHA-256 Hashing Works

Each valid seed phrase is **irreversibly transformed** using the SHA-256 algorithm.

### 🧪 Python Example

```python
import hashlib

phrase = "abandon ability able about above absent absorb abstract abuse access accident account"
hashed = hashlib.sha256(phrase.encode()).hexdigest()
print(hashed)

