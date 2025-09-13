# 🤖 Conversational RAG Q&A with PDF Uploads & Chat History  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/LangChain-Orchestration-orange?logo=chainlink" />
  <img src="https://img.shields.io/badge/Groq-LLM-black?logo=groq" />
  <img src="https://img.shields.io/badge/HuggingFace-Embeddings-yellow?logo=huggingface" />
  <img src="https://img.shields.io/badge/Chroma-VectorDB-green?logo=redis" />
</p>  

<p align="center">
  <img src="https://img.shields.io/github/stars/kanhaiya-98/GenAI-Lab?style=social" />
  <img src="https://img.shields.io/github/forks/kanhaiya-98/GenAI-Lab?style=social" />
</p>  

---

## 🚀 What is this?

An **AI-powered Research Assistant** that allows you to:  

✨ Upload **PDFs** 📑  
✨ Ask **conversational questions** 💬  
✨ Receive **context-aware answers** ⚡  
✨ Keep **chat history** persistent 🔄  

✅ Built on **Streamlit + LangChain + Groq + HuggingFace + ChromaDB**  

<p align="center">
  <img src="assets/application1.png" width="45%" />
  <img src="assets/application2.png" width="45%" />
</p>

---

## ✨ Features  

✅ **PDF Upload** – Single or multiple files  
✅ **Conversational Chat** – Natural dialogue with your docs  
✅ **Persistent Memory** – Session-based chat history  
✅ **RAG Pipeline** – Retrieval before generation for accuracy  
✅ **Groq LLM** – Lightning-fast inference  
✅ **Secure Keys** – `.env` for Hugging Face & Groq  

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,streamlit,git,github,vscode" />
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/langchain.svg" height="48" title="LangChain"/>
  <img src="https://avatars.githubusercontent.com/u/150010367?s=200&v=4" height="48" title="Groq"/>
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/huggingface.svg" height="48" title="HuggingFace"/>
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/docker.svg" height="48" title="Docker"/>
</p>  

---

## ⚙️ How It Works  

```mermaid
flowchart TD
    A[📂 PDF Upload] --> B[🔎 Chunking & Embedding]
    B --> C[🗄️ Vector Store - ChromaDB]
    C --> D[📜 Query Reformulation - History Aware]
    D --> E[🔍 Similarity Search]
    E --> F[⚡ Groq LLM (Gemma-9b-it)]
    F --> G[🤖 Answer Generated]
