# 🐋 DeepDoc-RAG: Gen AI Document QA

Welcome to **[DeepDoc-RAG](https://github.com/wolfsbane-14/DeepDoc-RAG)** – an AI-powered tool for interacting with PDF documents using natural language. DeepDoc-RAG processes PDFs into a vector database and delivers fast, context-aware responses via **DeepSeek-R1 Distill Llama 70B** using the **Groq API**.

---

## 🚀 Features

✅ **PDF Upload & Processing:** Quick and secure PDF uploads.
💾 **Vector Database Storage:** Stores embeddings using **Chroma**.
💬 **Conversational Q&A:** Clear, contextually accurate responses.
🧠 **"Think" Section:** Understand the AI's reasoning.
💡 **Modern Chat Interface:** Sleek chat UI with smooth animations.
⚡ **Fast & Lightweight:** Powered by **DeepSeek-R1 Distill Llama 70B** via **Groq API**.

---

## 🖼️ Screenshots

![Upload PDF](img/img1.png)  
*Upload and process PDF files easily.*

![Ask Questions](img/img2.png)  
*Ask questions and get instant responses.*

![AI Reasoning](img/img3.png)  
*View the AI’s reasoning in the "Think" section.*

---

## 📋 Tech Stack

- **Frontend:** Streamlit
- **LLM:** DeepSeek-R1 Distill Llama 70B (via Groq API)
- **PDF Processing:** Unstructured for text extraction
- **Vector Storage:** Chroma for embeddings
- **Backend:** LangChain

---

## 💾 Installation

### ✅ Prerequisites
- Python 3.8 or higher

---

### 📦 Install Dependencies

1. Clone the Repository:
```bash
git clone https://github.com/wolfsbane-14/DeepDoc-RAG.git
cd DeepDoc-RAG
```

2. Create a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install Packages:
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

1. Set Up API Key:
Create `config.json` in the root directory:
```json
{
  "GROQ_API_KEY": "your_deepseek_api_key_here"
}
```
Replace with your **Groq API key**.

---

## 💻 Usage

1. **Run the App:**
```bash
streamlit run main.py
```

2. **Upload PDF:** Upload your PDF for processing.

3. **Chat with the Document:** Ask questions, and get context-aware answers.

4. **View AI Reasoning:** Expand **"See How It Thinks"** to view the AI’s thought process.

5. **Reset Chat:** Click **"Clear Chat"** to start over.

---

## 📁 Project Structure

```
├── main.py                 # Streamlit frontend
├── rag_utility.py          # Document processing and QA chain
├── config.json             # Groq API key
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## 🧩 Customization

- **Chat Interface:** Modify CSS in `main.py` for different styles.
- **Document Processing:** Adjust `chunk_size` and `chunk_overlap` in `rag_utility.py`.
- **LLM Configuration:** Change `temperature` in the `llm` object.

---

## 🧠 How It Works

1. **Document Processing:**
   - PDFs are processed using **UnstructuredPDFLoader**.
   - Text is split into chunks using **RecursiveCharacterTextSplitter**.

2. **Vector Embedding:**
   - Text chunks are embedded using **HuggingFaceEmbeddings**.
   - Embeddings are stored in **Chroma**.

3. **Conversational Retrieval:**
   - User queries are matched with document chunks using **Chroma**.
   - **DeepSeek-R1 Distill Llama 70B** generates responses.

4. **Chat Interface:**
   - Streamlit displays messages in animated chat bubbles.

---

## 🛠️ Troubleshooting

- **API Key Error:** Verify `config.json` and your **Groq API key**.
- **Slow Response:** Adjust `chunk_size` or increase `chunk_overlap`.

---

