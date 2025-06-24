from datetime import datetime
import re

def get_extraction_timestamp():
    """Get current timestamp for extraction"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_document_length(text):
    """Calculate document length in characters"""
    return len(text) if text else 0

def count_words(text):
    """Count words in text"""
    if not text:
        return 0
    return len(text.split())

def count_paragraphs(text):
    """Count paragraphs in text"""
    if not text:
        return 0
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)

def calculate_reading_time(text, wpm=200):
    """Calculate approximate reading time in minutes"""
    if not text:
        return "0 min"
    
    word_count = count_words(text)
    minutes = word_count / wpm
    
    if minutes < 1:
        return f"{int(minutes * 60)} sec"
    elif minutes < 60:
        return f"{int(minutes)} min"
    else:
        hours = int(minutes // 60)
        mins = int(minutes % 60)
        return f"{hours}h {mins}min"

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def generate_basic_metadata(file, text, file_type):
    """Generate comprehensive metadata for document"""
    file_size = getattr(file, 'size', 0)
    
    metadata = {
        'file_name': file.name,
        'extracted_on': get_extraction_timestamp(),
        'file_type': file_type.upper(),
        'file_size': format_file_size(file_size),
        'document_length': f"{calculate_document_length(text):,} characters",
        'word_count': f"{count_words(text):,} words",
        'approx_reading_time': calculate_reading_time(text),
        'paragraphs': f"{count_paragraphs(text)} paragraphs"
    }
    
    return metadata

def clean_text_for_analysis(text):
    """Clean text for better analysis"""
    if not text:
        return ""
    
    # Remove extra whitespace and normalize
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text