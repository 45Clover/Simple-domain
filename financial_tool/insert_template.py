# insert_template.py
from pathlib import Path

TEMPLATE_PATH = Path("templates/report_template.tex")
GENERATED_LATEX_PATH = Path("decoded/financial_report.tex")
FINAL_OUTPUT_PATH = Path("output/final_report.tex")

def insert_into_template(template_path: Path, latex_code_path: Path, output_path: Path) -> None:
    template = template_path.read_text()
    latex_code = latex_code_path.read_text()

    if "%PLACEHOLDER" not in template:
        raise ValueError("Template must contain %PLACEHOLDER to insert the report")

    final_content = template.replace("%PLACEHOLDER", latex_code)
    output_path.parent.mkdir(exist_ok=True, parents=True)
    output_path.write_text(final_content)
    print(f"✓ Final LaTeX report saved to {output_path}")

def main():
    insert_into_template(TEMPLATE_PATH, GENERATED_LATEX_PATH, FINAL_OUTPUT_PATH)

if __name__ == "__main__":
    main()

