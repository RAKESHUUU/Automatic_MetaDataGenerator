from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

def detect_language(text):
    """Detect the primary language of text"""
    if not text or len(text.strip()) < 10:
        return "Unknown"
    
    try:
        lang_code = detect(text[:1000])  # Use first 1000 chars for efficiency
        return get_language_name(lang_code)
    except LangDetectException:
        return "Unknown"

def detect_language_with_confidence(text):
    """Detect language with confidence score"""
    if not text or len(text.strip()) < 10:
        return "Unknown", 0.0
    
    try:
        lang_probs = detect_langs(text[:1000])
        if lang_probs:
            top_lang = lang_probs[0]
            return get_language_name(top_lang.lang), round(top_lang.prob, 2)
    except LangDetectException:
        pass
    
    return "Unknown", 0.0

def get_language_name(lang_code):
    """Convert language code to language name"""
    lang_map = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'ja': 'Japanese',
        'ko': 'Korean',
        'zh-cn': 'Chinese (Simplified)',
        'zh-tw': 'Chinese (Traditional)',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'bn': 'Bengali',
        'ur': 'Urdu',
        'ta': 'Tamil',
        'te': 'Telugu',
        'mr': 'Marathi',
        'gu': 'Gujarati',
        'kn': 'Kannada',
        'ml': 'Malayalam',
        'pa': 'Punjabi',
        'ne': 'Nepali',
        'si': 'Sinhala',
        'th': 'Thai',
        'vi': 'Vietnamese',
        'id': 'Indonesian',
        'ms': 'Malay',
        'tl': 'Filipino',
        'nl': 'Dutch',
        'sv': 'Swedish',
        'da': 'Danish',
        'no': 'Norwegian',
        'fi': 'Finnish',
        'pl': 'Polish',
        'cs': 'Czech',
        'sk': 'Slovak',
        'hu': 'Hungarian',
        'ro': 'Romanian',
        'bg': 'Bulgarian',
        'hr': 'Croatian',
        'sr': 'Serbian',
        'sl': 'Slovenian',
        'et': 'Estonian',
        'lv': 'Latvian',
        'lt': 'Lithuanian',
        'tr': 'Turkish',
        'el': 'Greek',
        'he': 'Hebrew',
        'fa': 'Persian',
        'sw': 'Swahili',
        'af': 'Afrikaans'
    }
    
    return lang_map.get(lang_code, f"Unknown ({lang_code})")

def analyze_language(text):
    """Complete language analysis"""
    language, confidence = detect_language_with_confidence(text)
    
    return {
        'detected_language': language,
        'confidence': f"{confidence * 100:.1f}%",
        'is_reliable': confidence > 0.7
    }