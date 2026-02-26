import sys
from PyPDF2 import PdfReader

def extract_pdf_range(file_path, start_page, end_page):
    try:
        reader = PdfReader(file_path)
        total_pages = len(reader.pages)
        output = []
        
        # Notion of page numbering: 1-indexed for users, 0-indexed for code
        start_idx = max(0, start_page - 1)
        end_idx = min(total_pages, end_page)
        
        for i in range(start_idx, end_idx):
            page_text = reader.pages[i].extract_text()
            output.append(f"--- Page {i+1} ---")
            output.append(page_text)
            output.append("\n")
            
        return "\n".join(output)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    result = extract_pdf_range('2026.2.5PPT.pdf', 31, 75)
    print(result)
