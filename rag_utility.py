import streamlit as st
import os
import json
import tempfile

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

from ocr_utility import process_pdf_with_ocr, create_document_from_image

# workingDirectory = os.path.dirname(os.path.abspath((__file__)))
# configData = json.load(open(f"{workingDirectory}/config.json"))
# GROQ_API_KEY = configData["GROQ_API_KEY"]
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

if "GROQ_API_KEY" not in st.secrets:
    raise ValueError("GROQ_API_KEY is missing in Streamlit secrets")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# loading the embedding model
embedding = HuggingFaceEmbeddings()

# load the llm form groq
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0
)

def is_image_file(file_name):
    """Check if the file is an image based on its extension"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif']
    _, ext = os.path.splitext(file_name.lower())
    return ext in image_extensions

def process_document_to_chroma_db(file_name):
    file_path = f"{workingDirectory}/{file_name}"
    _, extension = os.path.splitext(file_name.lower())
    
    # Process based on file type
    if extension == '.pdf':
        # Option to use OCR for PDFs with scanned content
        try:
            # First try with regular PDF loader
            loader = UnstructuredPDFLoader(file_path)
            documents = loader.load()
            
            # If no text was extracted, fall back to OCR
            if not documents or not documents[0].page_content.strip():
                print("No text extracted from PDF, falling back to OCR...")
                text = process_pdf_with_ocr(file_path)
                
                # Create temporary text file and load it
                with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
                    temp_file.write(text)
                    temp_path = temp_file.name
                
                loader = UnstructuredFileLoader(temp_path)
                documents = loader.load()
                os.unlink(temp_path)
        except Exception as e:
            print(f"Error processing PDF normally, trying OCR: {e}")
            text = process_pdf_with_ocr(file_path)
            
            # Create temporary text file and load it
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
                temp_file.write(text)
                temp_path = temp_file.name
            
            loader = UnstructuredFileLoader(temp_path)
            documents = loader.load()
            os.unlink(temp_path)
    
    elif is_image_file(file_name):
        # Process image files with OCR
        documents = create_document_from_image(file_path, file_name)
    
    else:
        raise ValueError(f"Unsupported file type: {extension}")
    
    # splitting the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=f"{workingDirectory}/doc_vectorstore"
    )
    return 0

def answer_question(user_question):
    # load the persistent vectordb
    vectordb = Chroma(
        persist_directory=f"{workingDirectory}/doc_vectorstore",
        embedding_function=embedding
    )
    # retriever
    retriever = vectordb.as_retriever()

    # create a chain to answer user question using DeepSeek-R1
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )
    
    # Add thinking steps to show the process
    thinking = "<think>\n"
    thinking += "1. Retrieving relevant document chunks from vector database\n"
    thinking += "2. Finding information related to the question\n"
    thinking += "3. Formulating a comprehensive answer based on retrieved context\n"
    thinking += "</think>"
    
    response = qa_chain.invoke({"query": user_question})
    answer = response["result"] + thinking
    
    return answer