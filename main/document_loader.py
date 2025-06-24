import os
from pathlib import Path
from config import Config

def validate_file_size(file):
    """Validate if file size is within limits"""
    if hasattr(file, 'size'):
        return file.size <= Config.MAX_FILE_SIZE_BYTES
    return True

def get_file_type(filename):
    """Get file type from filename"""
    ext = Path(filename).suffix.lower()
    if ext in ['.pdf']:
        return 'pdf'
    elif ext in ['.docx', '.doc']:
        return 'docx'
    elif ext in ['.txt']:
        return 'txt'
    elif ext in ['.xlsx', '.xls']:
        return 'excel'
    elif ext in ['.md']:
        return 'markdown'
    elif ext in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp']:
        return 'image_ocr'
    return 'unknown'

def is_supported_format(filename):
    """Check if file format is supported"""
    ext = Path(filename).suffix.lower()
    return ext in Config.SUPPORTED_EXTENSIONS

def validate_document(file):
    """Complete document validation"""
    if not file:
        return False, "No file provided"
    
    if not is_supported_format(file.name):
        return False, f"Unsupported format. Supported: {', '.join(Config.SUPPORTED_EXTENSIONS)}"
    
    if not validate_file_size(file):
        return False, f"File too large. Max size: {Config.MAX_FILE_SIZE_MB}MB"
    
    return True, "Valid document"

def get_file_info(file):
    """Get basic file information"""
    return {
        'name': file.name,
        'size': getattr(file, 'size', 0),
        'type': get_file_type(file.name)
    }