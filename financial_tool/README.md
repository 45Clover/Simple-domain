# 📊 Financial Statement Decoder

This tool decodes **base64-encoded PDFs** containing embedded **JSON financial data**, then:

1. Decodes the PDF
2. Extracts the financial data
3. Parses and structures it (income, expenses, assets, liabilities)
4. Generates LaTeX code for an Income Statement and Balance Sheet
5. Inserts that into a LaTeX template
6. Outputs a final `.tex` file ready for PDF compilation

---

## 🔧 Manual Pipeline Steps

1. **Place Input File**  
   Add your `.b64` file here:  

