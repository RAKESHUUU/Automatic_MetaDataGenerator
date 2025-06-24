# 📄 Automatic Meta-Data Generation System

A comprehensive document analysis tool that automatically extracts and generates structured metadata from various document formats using AI-powered insights.

## 🚀 Features

- **Multi-format Support**: PDF, DOCX, DOC, TXT, XLSX, XLS, MD, and image files (JPG, PNG, TIFF, BMP)
- **Large File Handling**: Supports documents up to 300MB
- **AI-Powered Analysis**: Uses Mistral AI for intelligent document summarization and insights
- **Language Detection**: Automatic language identification with confidence scores
- **Comprehensive Metadata**: Extracts file details, text statistics, reading time, and document structure
- **Interactive Web Interface**: Built with Streamlit for easy document upload and processing
- **Export Options**: Download metadata as structured JSON files

## 🛠️ Technology Stack

### Core Processing
- **PyPDF2** & **pdfplumber** - Enhanced PDF processing
- **textract** - Multi-format document extraction
- **python-magic** - File type detection
- **openpyxl** & **xlrd** - Excel file support

### Language & Text Analysis
- **langdetect** - Language identification
- **polyglot** - Advanced language processing
- **spacy** - NLP processing
- **nltk** - Text analysis toolkit
- **textstat** - Reading statistics
- **readtime** - Reading time calculation

### AI Integration
- **LangChain** - AI workflow management
- **Mistral AI** - Document summarization and insights

### Web Interface
- **Streamlit** - Interactive web application
- **streamlit-extras** - Additional UI components
- **streamlit-option-menu** - Better navigation

### Image Processing
- **Pillow** - Image processing for OCR
- **pytesseract** - OCR text extraction

### File Handling
- **markdown** - Markdown file support

## 📋 Generated Metadata

The system extracts comprehensive metadata including:

- **Basic Information**: File name, extraction timestamp, file type, file size
- **Document Statistics**: Character count, word count, paragraph count, line count
- **Reading Metrics**: Estimated reading time, text complexity analysis
- **Language Analysis**: Detected language with confidence score
- **AI Insights**: 
  - Document summary
  - Key points extraction
  - Document type classification
- **Text Analysis**: Most common words, readability score, text structure

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd automatic-metadata-generation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "MISTRAL_API_KEY=your_mistral_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
main/
├── app.py                      # Main Streamlit application
├── .env                        # Environment variables (Mistral API key)
├── requirements.txt            # Dependencies
├── config.py                   # Configuration settings
├── document_loader.py          # Document loading and validation
├── text_extractor.py          # Text extraction from different formats
├── metadata_generator.py       # Core metadata generation logic
├── language_detector.py       # Language detection functionality
├── text_analyzer.py           # Text analysis (word count, paragraphs, etc.)
├── summary_generator.py       # Document summarization using Mistral
├── file_handler.py            # File upload and management
└── utils.py                   # Utility functions and helpers
```

## 🔑 Configuration

Make sure your `.env` file contains:
```
MISTRAL_API_KEY=your_mistral_api_key_here
```

## 📖 Usage

1. **Start the application**: Run `streamlit run app.py`
2. **Upload document**: Click "Upload your document" and select a file
3. **Wait for processing**: The system will extract text and generate metadata
4. **View results**: See comprehensive metadata displayed in the interface
5. **Download**: Export metadata as JSON file for further use

## 🔍 Supported File Formats

- **Documents**: PDF, DOCX, DOC, TXT, MD
- **Spreadsheets**: XLSX, XLS
- **Images**: JPG, JPEG, PNG, TIFF, BMP (with OCR)

## 🚦 System Requirements

- **File Size Limit**: 300MB maximum
- **Memory**: Recommended 4GB+ RAM for large documents
- **Python**: 3.7 or higher
- **Internet**: Required for Mistral AI API calls

## 🤖 AI Features

The system leverages **Mistral AI** for:
- Intelligent document summarization
- Key points extraction
- Document type classification
- Content analysis and insights

## 📊 Example Output

```json
{
  "file_name": "document.pdf",
  "extracted_on": "2024-06-25 10:30:15",
  "file_type": "PDF",
  "file_size": "2.3 MB",
  "document_length": "45,678 characters",
  "word_count": "7,892 words",
  "approx_reading_time": "32 min",
  "paragraphs": "45 paragraphs",
  "language_analysis": {
    "detected_language": "English",
    "confidence": "95.2%"
  },
  "ai_insights": {
    "summary": "This document discusses...",
    "key_points": ["Point 1", "Point 2", "Point 3"],
    "document_type": "Research Paper"
  }
}
```

## 🔄 Google Colab Integration

The system can also be run in Google Colab for cloud-based processing. See the notebook files for Colab-specific setup instructions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Future Enhancements

- [ ] Batch processing for multiple documents
- [ ] API endpoint for programmatic access
- [ ] Additional AI models integration
- [ ] Advanced text analytics
- [ ] Document comparison features
- [ ] Cloud storage integration

---

## 👨‍💻 Developer Information

**Name**: ALUMOLU RAKESH REDDY  
**Enrollment No**: 22117017  
**Email**: alumolu_rr@me.iitr.ac.in  
**Branch**: Mechanical Engineering  
**Institution**: Indian Institute of Technology Roorkee

---

⭐ **If you find this project helpful, please give it a star!** ⭐
