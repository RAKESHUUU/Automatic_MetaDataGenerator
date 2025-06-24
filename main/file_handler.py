import os
import tempfile
import streamlit as st
from pathlib import Path
from config import Config

def handle_file_upload():
    """Handle file upload in Streamlit"""
    uploaded_file = st.file_uploader(
        "Upload your document",
        type=[ext.replace('.', '') for ext in Config.SUPPORTED_EXTENSIONS],
        help=f"Supported formats: {', '.join(Config.SUPPORTED_EXTENSIONS)} | Max size: {Config.MAX_FILE_SIZE_MB}MB"
    )
    
    return uploaded_file

def save_temporary_file(uploaded_file):
    """Save uploaded file to temporary location"""
    if not uploaded_file:
        return None
    
    try:
        # Create temp directory if it doesn't exist
        temp_dir = Path("temp_files")
        temp_dir.mkdir(exist_ok=True)
        
        # Create temporary file
        file_extension = Path(uploaded_file.name).suffix
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, 
            suffix=file_extension,
            dir=temp_dir
        )
        
        # Write file content
        temp_file.write(uploaded_file.read())
        temp_file.close()
        
        # Reset file pointer for further use
        uploaded_file.seek(0)
        
        return temp_file.name
    
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

def cleanup_temp_files():
    """Clean up temporary files"""
    try:
        temp_dir = Path("temp_files")
        if temp_dir.exists():
            for file_path in temp_dir.glob("*"):
                if file_path.is_file():
                    file_path.unlink()
    except Exception as e:
        print(f"Warning: Could not cleanup temp files: {e}")

def get_file_size_mb(file):
    """Get file size in MB"""
    if hasattr(file, 'size'):
        return round(file.size / (1024 * 1024), 2)
    return 0

def display_file_info(file):
    """Display file information in Streamlit"""
    if file:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("File Name", file.name)
        
        with col2:
            file_size = get_file_size_mb(file)
            st.metric("File Size", f"{file_size} MB")
        
        with col3:
            file_type = Path(file.name).suffix.upper()
            st.metric("File Type", file_type)

def validate_uploaded_file(file):
    """Validate uploaded file"""
    if not file:
        return False, "No file uploaded"
    
    # Check file size
    if get_file_size_mb(file) > Config.MAX_FILE_SIZE_MB:
        return False, f"File size exceeds {Config.MAX_FILE_SIZE_MB}MB limit"
    
    # Check file extension
    file_ext = Path(file.name).suffix.lower()
    if file_ext not in Config.SUPPORTED_EXTENSIONS:
        return False, f"Unsupported file format. Supported: {', '.join(Config.SUPPORTED_EXTENSIONS)}"
    
    return True, "File is valid"