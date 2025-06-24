import PyPDF2
import pytesseract
from PIL import Image
from docx import Document
import pandas as pd
from io import BytesIO

def extract_from_pdf(file):
    """Extract text from PDF file"""
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

def extract_from_docx(file):
    """Extract text from DOCX file"""
    try:
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"

def extract_from_txt(file):
    """Extract text from TXT file"""
    try:
        content = file.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        return content.strip()
    except Exception as e:
        return f"Error extracting TXT: {str(e)}"

def extract_from_excel(file):
    """Extract text from Excel file"""
    try:
        df = pd.read_excel(file, sheet_name=None)
        text = ""
        for sheet_name, sheet_df in df.items():
            text += f"Sheet: {sheet_name}\n"
            text += sheet_df.to_string(index=False) + "\n\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting Excel: {str(e)}"

def extract_from_image_ocr(file):
    """Extract text from image using OCR"""
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error extracting OCR: {str(e)}"

def extract_from_markdown(file):
    """Extract text from Markdown file"""
    try:
        content = file.read()
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        return content.strip()
    except Exception as e:
        return f"Error extracting Markdown: {str(e)}"

def extract_text(file, file_type):
    """Main text extraction function"""
    extractors = {
        'pdf': extract_from_pdf,
        'docx': extract_from_docx,
        'txt': extract_from_txt,
        'excel': extract_from_excel,
        'image_ocr': extract_from_image_ocr,
        'markdown': extract_from_markdown
    }
    
    extractor = extractors.get(file_type)
    if not extractor:
        return f"Unsupported file type: {file_type}"
    
    # Reset file pointer
    if hasattr(file, 'seek'):
        file.seek(0)
    
    return extractor(file)