# 🕊️ Bird Hash Cloak — Steganography Project

This project hides a SHA-256 hash of a `.txt` file about bird migration inside a `bird.png` image using **pure Python**, no extra stego libraries.

## 📁 File Structure

stego_bird_hash/
├── bird.png # Source image of a bird
├── bird_hashed.png # Output with hidden hash
├── bird_migration.txt # Text file used for hashing
├── stego_embed.py # Embeds SHA-256 hash into image
├── stego_extract.py # Extracts hash from image

markdown
Copy
Edit

## 🧠 What it does

1. Reads a `.txt` file
2. Generates a SHA-256 hash
3. Converts that hash to binary
4. Replaces the least-significant bit of red pixels in the image
5. Allows full recovery of the hash later

## 🚀 Usage

### 🔐 Embed

```bash
python3 stego_embed.py
🔎 Extract
bash
Copy
Edit
python3 stego_extract.py
✅ Example Output
bash
Copy
Edit
✅ Hash embedded into bird_hashed.png
🔍 Recovered hash: 8d6e2a29cba7b5e1510e4d8e27ef3e12de03eb13d195adf44e3d27f49c3b4e4d
🛡️ Security Tip
To make this more covert:

Hide multiple hashes across RGB channels

Add XOR encryption before embedding

Combine this with image watermarking

🧑‍💻 Built by Lebo
This is just the beginning of your stego-cyber toolkit 😎

vbnet
Copy
Edit

---

## ✅ Next Steps (optional)
- Want me to add **XOR encryption** to the embedded hash?
- Want the output image to include a **magic header** to detect presence of a hash?
- Want this all zipped into a GitHub-ready project?

Let me know and I’ll prep the next upgrades.

