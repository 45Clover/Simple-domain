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








Ask ChatGPT
You said:
i made a swp file of  stego_embed.py how do i delete it


ChatGPT said:
A .swp file is a temporary swap file created by editors like vim or nano to prevent data loss. You can safely delete it if:

You've closed the editor

You no longer need the backup or have saved your changes

🧹 To delete the .swp file:
✅ Terminal Command:
bash
Copy
Edit
rm stego_embed.py.swp
🧠 Extra Tips
If you're unsure whether vim is still using it, you can type:

bash
Copy
Edit
ps aux | grep vim
If no active vim session shows, you're clear.

You can also use:

bash
Copy
Edit
ls -a
To see all hidden swap/temp files in the folder.

Let me know if it keeps reappearing — that could mean the editor crashed or is still running in the background.








You said:
raceback (most recent call last):
  File "/home/tangunyasha/stego_bird_hash/stego_embed.py", line 1, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'


ChatGPT said:
That error means the Python Imaging Library (PIL) — specifically the modern fork called Pillow — is not installed on your system.

✅ Solution: Install Pillow
You can install it using pip:

bash
Copy
Edit
pip install Pillow
If you're using Python 3 (which you are), and pip defaults to Python 2, use:

bash
Copy
Edit
pip3 install Pillow
🧪 Test it
After installation, run this in Python:

python
Copy
Edit
from PIL import Image
print("Pillow is working!")
🧠 Why This Happens
PIL is the original library (now outdated)

Pillow is its maintained fork

When you import PIL, you're actually importing Pillow, which still uses the PIL name for compatibility

Once Pillow is installed, you’re good to go. Let me know if you want me to rewrite the code to avoid any dependencies, even Pillow.








You said:
how do i active the environment


ChatGPT said:
To activate a Python virtual environment, follow these steps based on your operating system and environment setup.

✅ 1. If You Already Created a Virtual Environment
Let’s say you created it with:

bash
Copy
Edit
python3 -m venv venv
You can now activate it:

🐧 On Linux/macOS:
bash
Copy
Edit
source venv/bin/activate
🪟 On Windows (CMD):
cmd
Copy
Edit
venv\Scripts\activate
🪟 On Windows (PowerShell):
powershell
Copy
Edit
venv\Scripts\Activate.ps1
📦 2. Then Install Dependencies (e.g., Pillow)
Once you're inside the virtual environment, your shell will usually show something like (venv) at the start of your prompt.

Now install Pillow:

bash
Copy
Edit
pip install Pillow
🔒 3. To Exit the Environment
When you’re done:

bash
Copy
Edit
deactivate
🧠 Not Sure If You Created a Virtual Env?
If venv or any virtual env folder isn’t present in your project directory, just create one:

bash
Copy
Edit
python3 -m venv venv
Then activate it using the steps above.

Let me know if you need to set this up from scratch or want to include a requirements.txt file.










