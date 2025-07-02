# decode_pdf.py
"""
Step 1 of your manual pipeline:
• Read a base64‑encoded PDF file
• Decode it to a normal PDF
• Extract the embedded JSON financial data
"""
import base64
import json
import re
from pathlib import Path

from pdfminer.high_level import extract_text        # pip install pdfminer.six


# ---------- Paths (edit if your folders differ) ----------
INPUT_B64      = Path("input/encoded_statement.pdf.b64")
DECODED_PDF    = Path("decoded/statement.pdf")
OUTPUT_JSON    = Path("decoded/statement.json")


# ---------- Helpers ----------
def decode_base64_file(b64_path: Path, pdf_path: Path) -> None:
    """Decode base64 file → binary PDF."""
    pdf_bytes = base64.b64decode(b64_path.read_bytes())
    pdf_path.parent.mkdir(exist_ok=True, parents=True)
    pdf_path.write_bytes(pdf_bytes)
    print(f"✓ Decoded PDF written to {pdf_path}")


def extract_json_from_pdf(pdf_path: Path, json_path: Path) -> None:
    """
    Pull text from the PDF and locate the first valid JSON object.
    The JSON can span multiple lines; we look for the first {...}
    that `json.loads()` accepts.
    """
    text = extract_text(str(pdf_path))

    # ❶  Grab every {...} block greedily (DOTALL = cross‑line)
    brace_blocks = re.finditer(r"\{.*?\}", text, re.DOTALL)
    for match in brace_blocks:
        snippet = match.group(0)
        try:
            data = json.loads(snippet)
            json_path.parent.mkdir(exist_ok=True, parents=True)
            json_path.write_text(json.dumps(data, indent=4))
            print(f"✓ JSON extracted to {json_path}")
            return
        except json.JSONDecodeError:
            continue

    # ❷  If we get here, nothing parsed
    raise ValueError(
        "No valid JSON object found in the PDF. "
        "Check that the PDF really contains JSON or adjust the regex."
    )


# ---------- Main ----------
def main() -> None:
    if not INPUT_B64.exists():
        raise FileNotFoundError(f"Expected base64 file at {INPUT_B64}")

    decode_base64_file(INPUT_B64, DECODED_PDF)
    extract_json_from_pdf(DECODED_PDF, OUTPUT_JSON)


if __name__ == "__main__":
    main()

