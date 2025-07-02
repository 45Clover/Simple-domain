# parse_data.py
import json
from pathlib import Path
from typing import Dict, Any

INPUT_JSON = Path("decoded/statement.json")
OUTPUT_PARSED = Path("decoded/parsed_data.json")  # Optional: save parsed summary for debugging

def parse_financial_data(json_path: Path) -> Dict[str, Any]:
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Validate required keys
    for key in ["income", "expenses", "assets", "liabilities"]:
        if key not in data:
            data[key] = {}  # Fill missing categories with empty dict

    # Calculate totals
    totals = {k: sum(v.values()) if isinstance(v, dict) else 0 for k, v in data.items()}

    parsed = {
        "details": data,
        "totals": totals
    }

    # Optional: save parsed summary
    OUTPUT_PARSED.parent.mkdir(exist_ok=True, parents=True)
    with open(OUTPUT_PARSED, 'w') as f:
        json.dump(parsed, f, indent=4)

    print(f"✓ Parsed data saved to {OUTPUT_PARSED}")
    return parsed


def main():
    parsed_data = parse_financial_data(INPUT_JSON)
    print("Summary of parsed data:")
    for section, total in parsed_data["totals"].items():
        print(f"  {section.title()}: {total:.2f}")

if __name__ == "__main__":
    main()

