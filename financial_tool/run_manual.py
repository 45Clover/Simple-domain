# run_manual.py
import subprocess

scripts = [
    "decode_pdf.py",
    "parse_data.py",
    "generate_latex.py",
    "insert_template.py"
]

def main():
    print("📦 Running full pipeline manually...")
    for script in scripts:
        print(f"\n➡️ Running {script}...")
        result = subprocess.run(["python3", script], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"❌ {script} failed:\n{result.stderr}")
            break
    else:
        print("\n✅ All steps completed. Final .tex ready in /output.")

if __name__ == "__main__":
    main()

