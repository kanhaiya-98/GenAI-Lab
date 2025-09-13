# 🤖 Conversational RAG Q\&A with PDF Uploads & Chat History

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

An **AI-powered Q\&A assistant** that lets you:

* Upload **PDFs** 📑
* Ask **conversational questions** 💬
* Get **context-aware answers** ⚡
* Keep **chat history** persistent 🔄

Built with **Streamlit + LangChain + Groq + Hugging Face + Chroma DB**.

---

## ✨ Features

✅ **PDF Upload** – Single or multiple files.
✅ **Conversational Chat** – Natural dialogue with your docs.
✅ **Persistent Memory** – Session-based chat history.
✅ **RAG Pipeline** – Retrieval before generation for accuracy.
✅ **Groq LLM** – Lightning-fast inference.
✅ **Secure Keys** – `.env` for Hugging Face & Groq.

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,streamlit,azure,git,github" />
</p>  

---

## ⚙️ How It Works

```mermaid
flowchart TD
    A[📂 PDF Upload] --> B[🔎 Chunking & Embedding]
    B --> C[🗄️ Vector Store - Chroma]
    C --> D[📜 Query Reformulation - History Aware]
    D --> E[🔍 Similarity Search]
    E --> F[⚡ Groq LLM (Gemma-9b-it)]
    F --> G[🤖 Answer Generated]
```

---

## 🛠️ Tech Stack

* **UI** → Streamlit
* **Orchestration** → LangChain
* **LLM** → Groq (Gemma2-9b-It)
* **Embeddings** → Hugging Face (all-MiniLM-L6-v2)
* **Vector Store** → Chroma DB
* **Loader** → PyPDFLoader
* **Env Mgmt** → python-dotenv

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,docker" />  
</p>  

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python **3.8+**
* `pip`

### ⚡ Setup

```bash
# 1. Clone
git clone https://github.com/kanhaiya-98/GenAI-Lab.git
cd GenAI-Lab

# 2. Virtual Environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install Dependencies
pip install -r RAG-Q&A-WITH-PDF-&-CHAT-HISTORY/requirements.txt

# 4. Configure .env
HF_TOKEN="your_hugging_face_api_token"

# 5. Run
streamlit run RAG-Q&A-WITH-PDF-&-CHAT-HISTORY/app.py
```

---

## 📖 Usage

1. 🔑 Enter **Groq API key** (get from [Groq Console](https://console.groq.com/))
2. 🆔 Set a **Session ID** (optional, keeps chats separate)
3. 📂 Upload PDFs
4. 💬 Ask questions → Get AI answers with history

---

## 📸 Screenshots

