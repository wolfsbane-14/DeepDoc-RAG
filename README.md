# DeepDoc-RAG: Gen AI Document QA

Welcome to **DeepDoc-RAG** – a cutting-edge tool that lets you chat with your documents using the power of generative AI. With this project, you can upload a PDF, have it processed into a searchable vector database, and then ask questions about its content in a natural, conversational way.

## What Is DeepDoc-RAG?

DeepDoc-RAG is designed to make document analysis interactive and intuitive. By combining document processing, vector storage, and AI-powered retrieval, this project lets you extract meaningful answers from your PDFs with ease. Whether you're reviewing reports, research papers, or any long document, DeepDoc-RAG makes the process simple and engaging.

## Key Features

- **Easy PDF Upload:** Drag and drop your PDF file and let the magic begin.
- **Smart Document Processing:** The tool automatically extracts text and splits your document into manageable chunks.
- **Vector Database Storage:** Uses Chroma to store document embeddings for fast and accurate retrieval.
- **Conversational Q&A:** Ask questions about your document and receive context-aware answers.
- **Insight into AI Reasoning:** Check out the "Think" section to see a peek behind the scenes of how the AI processes your queries.
- **Customizable Interface:** Enjoy a sleek UI built with Streamlit and personalized with custom CSS.

## How It Works

1. **Upload & Process:**  
   Upload a PDF and the tool processes it, splitting the document and converting it into embeddings stored in a Chroma vector database.

2. **Ask Questions:**  
   Type your question about the document. The system retrieves relevant chunks using a retrieval chain and leverages a generative AI model to provide a precise answer.

3. **View Detailed Reasoning:**  
   For those curious about the inner workings, the "Think" section reveals insights into how the AI processed your question.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- Required Python packages:
  - `langchain_community`
  - `langchain_text_splitters`
  - `langchain_huggingface`
  - `langchain_chroma`
  - `langchain_groq`
- A valid API key for ChatGroq

### Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/deepdoc-rag.git
   cd deepdoc-rag
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install Dependencies:**  
   Ensure your `requirements.txt` is updated with all necessary packages, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Your API Key:**  
   Create a `config.json` file in the root directory with the following content:
   ```json
   {
     "GROQ_API_KEY": "your_groq_api_key_here"
   }
   ```
   Replace `your_groq_api_key_here` with your actual ChatGroq API key.

## Usage

1. **Run the Application:**  
   Launch the Streamlit app with:
   ```bash
   streamlit run your_script.py
   ```
   Replace `your_script.py` with the name of your main Python file.

2. **Upload a PDF:**  
   Use the provided file uploader to select your PDF. The document will be processed and its content stored for quick retrieval.

3. **Chat with Your Document:**  
   Type your questions in the text area and click "Send". The AI will fetch the relevant information and display a friendly, easy-to-read answer.

4. **Reset the Conversation:**  
   If you need to start over, simply click the "Clear Chat" button to reset the conversation history.

## Customization

### Interface Tweaks
Adjust the embedded CSS to change colors, animations, or layout elements to suit your style.

### Document Processing
Modify the `chunk_size` and `chunk_overlap` parameters in the code to better handle different document types.

### Model Settings
Fine-tune parameters like the `temperature` for the AI model to get varied responses.