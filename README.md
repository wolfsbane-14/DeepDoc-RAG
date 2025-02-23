# 🐋 DeepDoc-RAG: Gen AI Document QA

Welcome to **[DeepDoc-RAG](https://github.com/wolfsbane-14/DeepDoc-RAG)** – an advanced AI tool that enables you to interact with your documents using state-of-the-art generative AI. With DeepDoc-RAG, you can upload a PDF, have it processed into a searchable vector database, and ask natural language questions about its content. It leverages **DeepSeek-R1 Distill Llama 70B**, Groq, and LangChain to deliver fast, context-aware responses.

---

## 🚀 Features

✅ **PDF Upload & Processing:** Quickly upload and process PDF documents.  
💾 **Vector Database Storage:** Stores document embeddings using **Chroma** for fast retrieval.  
💬 **Conversational Q&A:** Ask questions and get clear, contextually accurate answers.  
🧠 **"Think" Section:** View the AI's reasoning behind each response.  
💡 **Modern Chat Interface:** Enjoy a sleek, bubble-style chat UI with smooth animations and a fixed bottom input bar.  
⚡ **Fast & Lightweight:** Powered by **DeepSeek-R1 Distill Llama 70B** via **Groq API** for lightning-fast inference.

---

## 🖼️ Screenshots

![Upload PDF](img/img1.png)
*Upload and process your PDF files easily.*

![Ask Questions](img/img2.png)
*Ask questions and receive accurate, context-aware answers.*

![AI Reasoning](img/img3.png)
*See the AI's internal reasoning in the expandable "Think" section.*

---

## 📋 Tech Stack

- **Frameworks:** Streamlit, LangChain, Chroma  
- **LLM:** DeepSeek-R1 Distill Llama 70B (via Groq API)  
- **PDF Processing:** Unstructured for text extraction and chunking  
- **Vector Storage:** Chroma for storing and retrieving embeddings  
- **Frontend:** Custom-styled chat UI with CSS animations  

---

## 💾 Installation

### ✅ Prerequisites
- Python 3.8 or higher
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (required for PDF processing)

Install Tesseract:  
**Ubuntu:**  
```bash
sudo apt update
sudo apt install tesseract-ocr
```
**macOS (Homebrew):**  
```bash
brew install tesseract
```

---

### 📦 Install Dependencies

1. **Clone the Repository:**
```bash
git clone https://github.com/wolfsbane-14/DeepDoc-RAG.git
cd DeepDoc-RAG
```

2. **Create a Virtual Environment:**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python Packages:**  
```bash
pip install -r requirements.txt
```

**`requirements.txt`** includes:  
```plaintext
langchain-community==0.3.16
langchain==0.3.16
langchain-huggingface==0.1.2
langchain-text-splitters==0.3.5
unstructured==0.16.16
unstructured[pdf]==0.16.16
langchain-unstructured==0.1.6
langchain-chroma==0.2.1
langchain-groq==0.2.3
streamlit==1.41.1
```

---

## 🔑 Configuration

1. **Set Up API Key:**  
Create a `config.json` file in the root directory:
```json
{
  "GROQ_API_KEY": "your_deepseek_api_key_here"
}
```
Replace `"your_deepseek_api_key_here"` with your actual **Groq API key** for **DeepSeek-R1 Distill Llama 70B**.

---

## 💻 Usage

1. **Run the Application:**  
```bash
streamlit run main.py
```

2. **Upload and Process PDF:**  
Use the file uploader to select your PDF. The document will be processed and stored as embeddings in the Chroma vector database.

3. **Chat with Your Document:**  
Type your questions in the input field and click **"Send"**. The AI will retrieve relevant information from the vector database and respond conversationally.

4. **View AI Reasoning:**  
Click on **"See How It Thinks"** to reveal the AI’s internal reasoning.

5. **Reset the Conversation:**  
Click **"Clear Chat"** to start a new session.

---

## 📁 Project Structure

```
├── main.py                 # Streamlit frontend with chat UI
├── rag_utility.py          # Utility functions for document processing and QA chain
├── config.json             # Configuration file with Groq API key
├── README.md               # Project documentation (this file)
└── requirements.txt        # Python dependencies
```

---

## 🧩 Customization

### Chat Interface  
- Modify CSS in `main.py` to customize bubble styles, animations, and layout.

### Document Processing  
- Adjust `chunk_size` and `chunk_overlap` in `rag_utility.py` for different document types.

### LLM Configuration  
- Fine-tune parameters like `temperature` in the `llm` object for different response styles.

---

## 💡 How It Works

1. **Document Processing:**  
   - Uploaded PDFs are processed using **UnstructuredPDFLoader**.
   - Text is split into chunks using **RecursiveCharacterTextSplitter**.

2. **Vector Embedding:**  
   - Text chunks are embedded using **HuggingFaceEmbeddings**.
   - Embeddings are stored in **Chroma** for quick retrieval.

3. **Conversational Retrieval:**  
   - User queries are matched with document chunks using **Chroma’s** retriever.
   - **DeepSeek-R1 Distill Llama 70B** (via **Groq API**) generates contextually accurate answers.

4. **Chat Interface:**  
   - Streamlit displays chat messages in bubbles with fade animations.
   - The fixed input bar mimics the ChatGPT-style user experience.

---

## 🛠️ Troubleshooting

- **Tesseract Not Found:** Ensure Tesseract is installed and added to your PATH.
- **API Key Error:** Double-check your `config.json` and verify the Groq API key is correct.
- **Slow Response:** Reduce `chunk_size` or increase `chunk_overlap` for better performance.

--