import os
import json

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

workingDirectory = os.path.dirname(os.path.abspath(__file__))
configData = json.load(open(os.path.join(workingDirectory, "config.json")))
GROQ_API_KEY = configData["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Load the embedding model
embedding = HuggingFaceEmbeddings()

# Load the LLM from Groq
llm = ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0)

def process_document_to_chroma_db(file_name):
    loader = UnstructuredPDFLoader(os.path.join(workingDirectory, file_name))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    # Store document embeddings in Chroma
    Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=os.path.join(workingDirectory, "doc_vectorstore"))
    return 0

def answer_question(user_question):
    vectordb = Chroma(persist_directory=os.path.join(workingDirectory, "doc_vectorstore"), embedding_function=embedding)
    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    response = qa_chain.invoke({"query": user_question})
    return response["result"]
