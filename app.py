import streamlit as st
import sys
from pathlib import Path

# Add main folder to Python path
main_folder = Path(__file__).parent / "main"
sys.path.append(str(main_folder))

# Import modules from main folder
from main.config import Config
from main.document_loader import validate_document, get_file_info
from main.text_extractor import extract_text
from main.metadata_generator import generate_basic_metadata, clean_text_for_analysis
from main.language_detector import analyze_language
from main.text_analyzer import analyze_text_structure
from main.summary_generator import generate_document_insights
from main.file_handler import handle_file_upload, display_file_info, validate_uploaded_file, cleanup_temp_files
from main.utils import format_file_size, export_metadata_json, is_text_meaningful

def main():
    """Main Streamlit application"""
    
    # Page configuration
    st.set_page_config(
        page_title=Config.PAGE_TITLE,
        page_icon=Config.PAGE_ICON,
        layout="wide"
    )
    
    # Header
    st.title("📄 Automatic Meta-Data Generation")
    st.markdown("Upload your document and get comprehensive metadata analysis instantly!")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Supported Formats")
        st.write("• PDF (.pdf)")
        st.write("• Word (.docx, .doc)")
        st.write("• Text (.txt)")
        st.write("• Excel (.xlsx, .xls)")
        st.write("• Markdown (.md)")
        st.write("• Images (.jpg, .png, .tiff) - OCR")
        
        st.header("⚙️ Settings")
        st.write(f"Max file size: {Config.MAX_FILE_SIZE_MB} MB")
        st.write(f"Reading speed: {Config.DEFAULT_READING_SPEED_WPM} WPM")
    
    # Main content
    uploaded_file = handle_file_upload()
    
    if uploaded_file:
        # Validate file
        is_valid, message = validate_uploaded_file(uploaded_file)
        
        if not is_valid:
            st.error(f"❌ {message}")
            return
        
        # Display file info
        st.success(f"✅ File uploaded successfully!")
        display_file_info(uploaded_file)
        
        # Process button
        if st.button("🚀 Process Document", type="primary"):
            with st.spinner("Processing document..."):
                process_document(uploaded_file)
    
    else:
        st.info("👆 Please upload a document to get started")
        

def process_document(uploaded_file):
    """Process uploaded document and generate metadata"""
    
    try:
        # Get file info
        file_info = get_file_info(uploaded_file)
        file_type = file_info['type']
        
        # Extract text
        st.write("🔍 Extracting text...")
        text = extract_text(uploaded_file, file_type)
        
        if not is_text_meaningful(text):
            st.error("❌ Could not extract meaningful text from the document")
            return
        
        # Clean text
        cleaned_text = clean_text_for_analysis(text)
        
        # Generate metadata sections
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Basic Metadata")
            
            # Basic metadata
            basic_metadata = generate_basic_metadata(uploaded_file, cleaned_text, file_type)
            
            for key, value in basic_metadata.items():
                st.metric(key.replace('_', ' ').title(), value)
        
        with col2:
            st.subheader("🌐 Language Analysis")
            
            # Language detection
            lang_analysis = analyze_language(cleaned_text)
            st.metric("Detected Language", lang_analysis['detected_language'])
            st.metric("Confidence", lang_analysis['confidence'])
            
            reliability = "✅ High" if lang_analysis['is_reliable'] else "⚠️ Low"
            st.metric("Reliability", reliability)
        
        # Text structure analysis
        st.subheader("📊 Text Structure Analysis")
        text_analysis = analyze_text_structure(cleaned_text)
        
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.metric("Sentences", f"{text_analysis['sentence_count']:,}")
            st.metric("Lines", f"{text_analysis['line_count']:,}")
        
        with col4:
            st.metric("Characters (no spaces)", f"{text_analysis['character_count_no_spaces']:,}")
            st.metric("Avg Word Length", f"{text_analysis['complexity']['avg_word_length']}")
        
        with col5:
            st.metric("Avg Sentence Length", f"{text_analysis['complexity']['avg_sentence_length']}")
            st.metric("Readability", text_analysis['complexity']['readability'])
        
        # Top words
        if text_analysis['top_words']:
            st.subheader("🔤 Most Common Words")
            top_words_df = st.columns(len(text_analysis['top_words'][:5]))
            for i, (word, count) in enumerate(text_analysis['top_words'][:5]):
                top_words_df[i].metric(word.title(), count)
        
        # AI-powered insights
        st.subheader("🤖 AI-Powered Insights")
        
        with st.spinner("Generating AI insights..."):
            insights = generate_document_insights(cleaned_text)
        
        # Document type
        st.write(f"**Document Type:** {insights['document_type']}")
        
        # Summary
        st.write("**Summary:**")
        st.write(insights['summary'])
        
        # Key points
        if insights['key_points']:
            st.write("**Key Points:**")
            for i, point in enumerate(insights['key_points'], 1):
                if point.strip():
                    st.write(f"{i}. {point}")
        
        # Complete metadata for export
        complete_metadata = {
            **basic_metadata,
            'detected_language': lang_analysis['detected_language'],
            'language_confidence': lang_analysis['confidence'],
            'document_type': insights['document_type'],
            'summary': insights['summary'],
            'key_points': insights['key_points'],
            'readability': text_analysis['complexity']['readability'],
            'avg_word_length': text_analysis['complexity']['avg_word_length'],
            'avg_sentence_length': text_analysis['complexity']['avg_sentence_length']
        }
        
        # Export options
        st.subheader("📤 Export Metadata")
        
        col6, col7 = st.columns(2)
        
        with col6:
            json_data = export_metadata_json(complete_metadata)
            st.download_button(
                label="📄 Download as JSON",
                data=json_data,
                file_name=f"{Path(uploaded_file.name).stem}_metadata.json",
                mime="application/json"
            )
        
        with col7:
            if st.button("🗑️ Clear Results"):
                cleanup_temp_files()
                st.rerun()
    
    except Exception as e:
        st.error(f"❌ Error processing document: {str(e)}")
        st.write("Please try uploading a different document or check the file format.")

if __name__ == "__main__":
    try:
        Config.validate()
        main()
    except Exception as e:
        st.error(f"❌ Configuration Error: {str(e)}")
        st.write("Please check your .env file and ensure MISTRAL_API_KEY is set.")