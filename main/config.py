import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_MODEL = "mistral-large-latest"
    
    # File limits
    MAX_FILE_SIZE_MB = 300
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
    
    # Supported formats
    SUPPORTED_EXTENSIONS = ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.md', '.jpg', '.jpeg', '.png', '.tiff', '.bmp']
    
    # Text analysis
    DEFAULT_READING_SPEED_WPM = 200
    MIN_TEXT_FOR_SUMMARY = 100
    
    # App config
    PAGE_TITLE = "Automatic Meta-Data Generation"
    PAGE_ICON = "📄"
    
    @classmethod
    def validate(cls):
        if not cls.MISTRAL_API_KEY:
            raise ValueError("MISTRAL_API_KEY not found in .env file")
        return True