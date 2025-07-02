# generate_latex.py
import json
from pathlib import Path
from typing import Dict

PARSED_DATA_PATH = Path("decoded/parsed_data.json")
OUTPUT_LATEX = Path("decoded/financial_report.tex")

def latex_escape(text: str) -> str:
    """Escape LaTeX special characters."""
    import re
    return re.sub(r'([#$%&_{}])', r'\\\1', text)

def generate_table_section(title: str, entries: Dict[str, float]) -> str:
    latex = f"\\section*{{{title}}}\n"
    latex += "\\begin{tabular}{l r}\n"
    latex += "\\toprule\n"
    latex += "Item & Amount (CAD) \\\\\n"
    latex += "\\midrule\n"
    for item, amount in entries.items():
        item_esc = latex_escape(item)
        latex += f"{item_esc} & {amount:.2f} \\\\\n"
    latex += "\\bottomrule\n"
    latex += "\\end{tabular}\n\n"
    return latex

def generate_summary_line(label: str, amount: float) -> str:
    latex = "\\begin{tabular}{l r}\n"
    latex += "\\toprule\n"
    latex += f"\\textbf{{{latex_escape(label)}}} & \\textbf{{{amount:.2f}}} \\\\\n"
    latex += "\\bottomrule\n"
    latex += "\\end{tabular}\n\n"
    return latex

def generate_report(parsed: Dict) -> str:
    income = parsed["details"].get("income", {})
    expenses = parsed["details"].get("expenses", {})
    assets = parsed["details"].get("assets", {})
    liabilities = parsed["details"].get("liabilities", {})

    income_total = sum(income.values())
    expenses_total = sum(expenses.values())
    assets_total = sum(assets.values())
    liabilities_total = sum(liabilities.values())

    net_income = income_total - expenses_total
    equity = assets_total - liabilities_total

    latex = ""

    # Income Statement
    latex += "\\section*{Income Statement}\n"
    latex += generate_table_section("Income", income)
    latex += generate_table_section("Expenses", expenses)
    latex += generate_summary_line("Net Income", net_income)

    # Balance Sheet
    latex += "\\section*{Balance Sheet}\n"
    latex += generate_table_section("Assets", assets)
    latex += generate_table_section("Liabilities", liabilities)
    latex += generate_summary_line("Equity", equity)

    return latex

def main():
    if not PARSED_DATA_PATH.exists():
        raise FileNotFoundError(f"Missing {PARSED_DATA_PATH}")

    with open(PARSED_DATA_PATH, 'r') as f:
        parsed = json.load(f)

    latex_content = generate_report(parsed)
    OUTPUT_LATEX.parent.mkdir(exist_ok=True, parents=True)
    with open(OUTPUT_LATEX, 'w') as f:
        f.write(latex_content)

    print(f"✓ LaTeX report generated at {OUTPUT_LATEX}")

if __name__ == "__main__":
    main()

