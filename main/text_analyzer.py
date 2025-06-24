import re
import string
from collections import Counter

def count_words(text):
    """Count total words in text"""
    if not text:
        return 0
    return len(text.split())

def count_sentences(text):
    """Count sentences in text"""
    if not text:
        return 0
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_paragraphs(text):
    """Count paragraphs in text"""
    if not text:
        return 0
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)

def count_lines(text):
    """Count lines in text"""
    if not text:
        return 0
    return len([line for line in text.split('\n') if line.strip()])

def analyze_readability(text):
    """Basic readability analysis"""
    if not text:
        return "N/A"
    
    words = count_words(text)
    sentences = count_sentences(text)
    
    if sentences == 0:
        return "N/A"
    
    avg_words_per_sentence = words / sentences
    
    if avg_words_per_sentence < 15:
        return "Easy"
    elif avg_words_per_sentence < 20:
        return "Medium"
    else:
        return "Hard"

def get_most_common_words(text, top_n=10):
    """Get most common words (excluding common stop words)"""
    if not text:
        return []
    
    # Simple stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 
                  'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
                  'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'}
    
    # Clean and split text
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    return Counter(filtered_words).most_common(top_n)

def calculate_text_complexity(text):
    """Calculate text complexity metrics"""
    if not text:
        return {}
    
    words = count_words(text)
    sentences = count_sentences(text)
    characters = len(text.replace(' ', ''))
    
    return {
        'avg_word_length': round(characters / words, 1) if words > 0 else 0,
        'avg_sentence_length': round(words / sentences, 1) if sentences > 0 else 0,
        'readability': analyze_readability(text)
    }

def analyze_text_structure(text):
    """Complete text structure analysis"""
    if not text:
        return {}
    
    analysis = {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'paragraph_count': count_paragraphs(text),
        'line_count': count_lines(text),
        'character_count': len(text),
        'character_count_no_spaces': len(text.replace(' ', '')),
        'complexity': calculate_text_complexity(text),
        'top_words': get_most_common_words(text, 5)
    }
    
    return analysis