from langchain_mistralai import ChatMistralAI
from config import Config

def initialize_mistral():
    """Initialize Mistral AI client"""
    try:
        return ChatMistralAI(
            mistral_api_key=Config.MISTRAL_API_KEY,
            model=Config.MISTRAL_MODEL,
            temperature=0.3
        )
    except Exception as e:
        print(f"Error initializing Mistral: {e}")
        return None

def generate_summary(text, max_words=200):
    """Generate document summary using Mistral AI"""
    if not text or len(text.strip()) < Config.MIN_TEXT_FOR_SUMMARY:
        return "Text too short for summary generation"
    
    mistral = initialize_mistral()
    if not mistral:
        return "Error: Could not initialize Mistral AI"
    
    # Truncate text if too long (keep first 3000 chars for efficiency)
    text_sample = text[:3000] if len(text) > 3000 else text
    
    prompt = f"""
    Please provide a concise summary of the following document in approximately {max_words} words. 
    Focus on the main points, key findings, and important information.
    
    Document text:
    {text_sample}
    
    Summary:
    """
    
    try:
        response = mistral.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def extract_key_points(text, num_points=5):
    """Extract key points from document"""
    if not text or len(text.strip()) < Config.MIN_TEXT_FOR_SUMMARY:
        return []
    
    mistral = initialize_mistral()
    if not mistral:
        return ["Error: Could not initialize Mistral AI"]
    
    text_sample = text[:3000] if len(text) > 3000 else text
    
    prompt = f"""
    Extract the {num_points} most important key points from this document. 
    Present them as a numbered list, each point should be concise and informative.
    
    Document text:
    {text_sample}
    
    Key Points:
    """
    
    try:
        response = mistral.invoke(prompt)
        points = response.content.strip().split('\n')
        return [point.strip() for point in points if point.strip()][:num_points]
    except Exception as e:
        return [f"Error extracting key points: {str(e)}"]

def generate_document_insights(text):
    """Generate comprehensive document insights"""
    if not text or len(text.strip()) < Config.MIN_TEXT_FOR_SUMMARY:
        return {
            'summary': "Text too short for analysis",
            'key_points': [],
            'document_type': "Unknown"
        }
    
    summary = generate_summary(text)
    key_points = extract_key_points(text)
    doc_type = classify_document_type(text)
    
    return {
        'summary': summary,
        'key_points': key_points,
        'document_type': doc_type
    }

def classify_document_type(text):
    """Classify document type based on content"""
    if not text:
        return "Unknown"
    
    mistral = initialize_mistral()
    if not mistral:
        return "Unknown"
    
    text_sample = text[:1000]
    
    prompt = f"""
    Classify this document type in one or two words (e.g., Report, Research Paper, Manual, Letter, Article, etc.):
    
    {text_sample}
    
    Document Type:
    """
    
    try:
        response = mistral.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return "Unknown"