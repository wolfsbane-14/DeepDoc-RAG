# Monkey patch sqlite3 with pysqlite3 for updated SQLite support.
import sys
try:
    import pysqlite3 as sqlite3
    sys.modules["sqlite3"] = sqlite3
except ImportError:
    pass

import os
import streamlit as st
from rag_utility import process_document_to_chroma_db, answer_question

# Set working directory
workingDirectory = os.getcwd()

st.title("🐋 DeepDoc-RAG")

# File uploader for PDF documents
uploadedFile = st.file_uploader("📂 Upload a PDF file", type=["pdf"])
if uploadedFile is not None:
    save_path = os.path.join(workingDirectory, uploadedFile.name)
    with open(save_path, "wb") as f:
        f.write(uploadedFile.getbuffer())
    process_document_to_chroma_db(uploadedFile.name)
    st.success("✅ Document Processed Successfully")

# Initialize chat session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    role, content, think_content = msg["role"], msg["content"], msg.get("think_content", "")
    bubble_class = "user-bubble" if role == "user" else "ai-bubble"
    st.markdown(f'<div class="bubble fade-in {bubble_class}">{content}</div>', unsafe_allow_html=True)

    if role == "ai" and think_content:
        with st.expander("🤔 **See How It Thinks**", expanded=False):
            st.info("This section shows how the system processes your question.")
            st.markdown(think_content)

# Text area for user input
userQuestion = st.text_area("💡 Ask your question about the document", height=100)

# Send button to process user questions
if st.button("🚀 Send"):
    if userQuestion:
        st.session_state.messages.append({"role": "user", "content": userQuestion})
        ans = answer_question(userQuestion)
        think_start = ans.find("<think>")
        think_end = ans.find("</think>")
        think_content = ans[think_start + 7 : think_end] if think_start != -1 and think_end != -1 else ""
        clean_answer = ans.replace(f"<think>{think_content}</think>", "")
        st.session_state.messages.append({
            "role": "ai",
            "content": clean_answer,
            "think_content": think_content
        })
        st.rerun()

# Clear chat button to reset the conversation
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Custom CSS styling for the chat interface
st.markdown("""
    <style>
        /* Chat container */
        div.stMarkdown {
            margin-bottom: 15px;
        }
        
        /* User message bubble */
        .user-bubble {
            background-color: rgb(30, 92, 207);
            color: white;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
            align-self: flex-end;
            margin-left: auto;
            animation: fadeInRight 0.5s ease-out;
        }
        
        /* AI message bubble */
        .ai-bubble {
            background-color: #333333;
            color: white;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
            align-self: flex-start;
            animation: fadeInLeft 0.5s ease-out;
        }
        
        /* Fade-in animation */
        .fade-in {
            opacity: 0;
            animation: fadeIn 0.5s ease-out forwards;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes fadeInRight {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        @keyframes fadeInLeft {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        /* Align the messages */
        div.css-1n76uvr {
            display: flex;
            flex-direction: column;
        }
        /* Page Title */
        .stApp {
            background-color: #1E1E1E;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        /* Expander for Think Section */
        details.stExpander {
            margin-top: 10px;
            border: 1px solid rgb(76, 86, 175);
            border-radius: 10px;
            overflow: hidden;
            animation: fadeIn 0.5s ease-out;
        }
    </style>
""", unsafe_allow_html=True)
