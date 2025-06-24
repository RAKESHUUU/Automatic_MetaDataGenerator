import re
import json
from datetime import datetime
from pathlib import Path

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def format_timestamp(timestamp=None):
    """Format timestamp for display"""
    if timestamp is None:
        timestamp = datetime.now()
    
    if isinstance(timestamp, str):
        return timestamp
    
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def clean_text(text):
    """Clean and normalize text"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters that might cause issues
    text = re.sub(r'[^\w\s\.,!?;:\-\(\)\"\']+', '', text)
    
    return text.strip()

def truncate_text(text, max_length=100):
    """Truncate text with ellipsis"""
    if not text or len(text) <= max_length:
        return text
    
    return text[:max_length].rsplit(' ', 1)[0] + "..."

def format_number(number):
    """Format numbers with commas"""
    if isinstance(number, (int, float)):
        return f"{number:,}"
    return str(number)

def calculate_reading_time(word_count, wpm=200):
    """Calculate reading time from word count"""
    if word_count <= 0:
        return "0 min"
    
    minutes = word_count / wpm
    
    if minutes < 1:
        return f"{int(minutes * 60)} sec"
    elif minutes < 60:
        return f"{int(minutes)} min"
    else:
        hours = int(minutes // 60)
        mins = int(minutes % 60)
        return f"{hours}h {mins}min"

def safe_divide(numerator, denominator):
    """Safe division with zero check"""
    if denominator == 0:
        return 0
    return numerator / denominator

def export_metadata_json(metadata):
    """Export metadata as JSON string"""
    try:
        return json.dumps(metadata, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error exporting JSON: {str(e)}"

def get_file_extension(filename):
    """Get file extension from filename"""
    return Path(filename).suffix.lower()

def is_text_meaningful(text, min_length=10):
    """Check if text has meaningful content"""
    if not text:
        return False
    
    # Remove whitespace and check length
    clean = text.strip()
    if len(clean) < min_length:
        return False
    
    # Check if text has alphabetic characters
    if not re.search(r'[a-zA-Z]', clean):
        return False
    
    return True