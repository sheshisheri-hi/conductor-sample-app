# Refactored to use pypdf instead of PyPDF2
from pypdf import PdfReader
import sys

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python package_copyleft.py <pdf_path>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    text = extract_text_from_pdf(pdf_path)
    print(text)
