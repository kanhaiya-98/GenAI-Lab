
# 🔍 AI Research Assistant With Search Engine  

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=36BCF7&center=true&vCenter=true&width=900&lines=Blazingly-fast+AI+Research+Assistant;Search-+Web+%7C+Explore+Wikipedia+%7C+Fetch+ArXiv+Papers;Powered+by+LangChain+%2B+Groq+LPU+Engine" alt="Typing SVG" />
</p>  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/LangChain-Agents-orange?logo=chainlink" />
  <img src="https://img.shields.io/badge/Groq-LPU-black?logo=groq" />
  <img src="https://img.shields.io/github/stars/kanhaiya-98/GenAI-Lab?style=social" />
  <img src="https://img.shields.io/github/forks/kanhaiya-98/GenAI-Lab?style=social" />
</p>  

A **blazingly-fast AI Research Assistant** built with **LangChain Agents** and **Groq’s LPU Engine**.  
This tool can **search the web**, **explore Wikipedia**, and **fetch academic papers from ArXiv** to deliver **research-grade answers in real-time**.  

💡 Designed for **students, researchers, and developers** who need an instant research sidekick.  

---



## ✨ Features

* 🖥️ **Interactive Chat Interface** – Modern Streamlit UI
* 🧠 **Autonomous ReAct Agent** – Thinks, reasons, and acts
* 🛠️ **Multi-Tool Power** – DuckDuckGo, Wikipedia, ArXiv
* ⚡ **Insanely Fast** – Powered by Groq’s LPU inference engine
* 📜 **Memory Support** – Keeps conversation context
* 🔄 **Switch Models Live** – Llama 3.1, Mixtral & more
* 🚀 **Agent Trace Mode** – Watch reasoning in real-time

---

## 🛠 Tech Stack

* **Framework:** Streamlit
* **Orchestration:** LangChain Agents
* **LLM Provider:** Groq LPU Engine
* **Tools:** DuckDuckGo Search, Wikipedia, ArXiv
* **Language:** Python

---

## 🌈 User Interface Highlights

<p align="center">
  <img src="assets/app1.png" width="80%" />
</p>  

<p align="center">
  <img src="assets/app2.png" width="80%" />
</p>  

---

## ⚡ Prerequisites

* Python 3.8+
* A **Groq API Key** (get free from [GroqCloud](https://groq.com/))

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kanhaiya-98/GenAI-Lab.git
cd "GenAI-Lab/AI RESEARCH ASSISTANT WITH SEARCH ENGINE"
```

### 2️⃣ Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment

Create a `.env` file and add:

```bash
GROQ_API_KEY="your_groq_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Access at 👉 [http://localhost:8501](http://localhost:8501)

---

## ⚙️ How It Works

```mermaid
flowchart TD
    A["💬 User Query"] --> B["🧠 LangChain ReAct Agent"]
    B --> C["🛠 Selects Tool"]
    C --> D["🌐 DuckDuckGo"]
    C --> E["📚 Wikipedia"]
    C --> F["📄 ArXiv"]
    D --> G["⚡ Groq LPU Engine"]
    E --> G
    F --> G
    G --> H["🤖 AI Response"]
    H --> I["🖥️ Streamlit Chat UI"]

    classDef step fill:#f3f4f6,stroke:#333,stroke-width:1px,rx:10,ry:10,font-size:12px;
    class A,B,C,D,E,F,G,H,I step;
```

---


