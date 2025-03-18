import os
import pytesseract
from PIL import Image
import pdf2image
import tempfile
from langchain_community.document_loaders import UnstructuredFileLoader

# Set Tesseract data path for Streamlit Cloud
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/5/tessdata/"

# Path to Tesseract executable (optional, uncomment if needed locally)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Linux/Streamlit Cloud default

def process_image_with_ocr(image_path):
    """Process a single image with OCR and return the extracted text"""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

def process_pdf_with_ocr(pdf_path, output_dir=None):
    """Process a PDF file with OCR and return the extracted text"""
    if output_dir is None:
        output_dir = tempfile.mkdtemp()
    
    try:
        # Convert PDF to images
        images = pdf2image.convert_from_path(pdf_path)
        
        # Process each page with OCR
        all_text = []
        for i, image in enumerate(images):
            # Save the image temporarily
            temp_image_path = os.path.join(output_dir, f"page_{i+1}.png")
            image.save(temp_image_path, 'PNG')
            
            # Extract text from the image
            text = process_image_with_ocr(temp_image_path)
            all_text.append(text)
            
            # Clean up temporary image file
            os.remove(temp_image_path)
        
        return "\n\n".join(all_text)
    except Exception as e:
        print(f"Error processing PDF {pdf_path} with OCR: {e}")
        return ""

def create_document_from_image(image_path, file_name):
    """Create a document object from an image file using OCR"""
    text = process_image_with_ocr(image_path)
    
    # Create a temporary text file to use with UnstructuredFileLoader
    temp_dir = tempfile.mkdtemp()
    temp_text_path = os.path.join(temp_dir, f"{os.path.splitext(file_name)[0]}.txt")
    
    with open(temp_text_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    # Use UnstructuredFileLoader to load the text file
    loader = UnstructuredFileLoader(temp_text_path)
    documents = loader.load()
    
    # Clean up temporary file
    os.remove(temp_text_path)
    os.rmdir(temp_dir)
    
    return documents