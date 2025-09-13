Conversational RAG Q&A with PDF Uploads and Chat History

This project is a sophisticated Question-Answering (Q&A) application that leverages a Retrieval-Augmented Generation (RAG) pipeline. It allows users to upload PDF documents, ask questions about their content, and receive contextually-aware answers, all while maintaining a persistent chat history for conversational follow-ups.
The application is built with Streamlit for the user interface and powered by the LangChain framework, using Groq for high-speed LLM inference and Hugging Face embeddings.
✨ Features
PDF Document Upload: Supports single or multiple PDF file uploads.
Conversational Interface: Chat with your documents in a natural, conversational way.
Persistent Chat History: Remembers previous turns in the conversation for contextual understanding, managed by session IDs.
Retrieval-Augmented Generation (RAG): Provides accurate answers by retrieving relevant text chunks from the uploaded documents before generating a response.
High-Performance LLM: Utilizes the Groq API for fast and efficient language model inference.
Secure API Key Handling: Uses a .env file and password input for managing API keys securely.
📸 Screenshots
Here is a preview of the application in action.

⚙️ How It Works
The application follows a modern RAG pipeline to answer user queries based on the content of the uploaded PDFs.
Document Ingestion: The user uploads one or more PDF files through the Streamlit interface.
Document Loading & Chunking: PyPDFLoader loads the content, which is then split into smaller, manageable chunks by RecursiveCharacterTextSplitter. This is crucial for the embedding model's context window and for effective retrieval.
Embedding & Vectorization: Each text chunk is converted into a numerical vector (embedding) using the all-MiniLM-L6-v2 model from Hugging Face.
Vector Storage: These embeddings are stored in a Chroma in-memory vector store, which allows for efficient similarity searches.
History-Aware Retrieval: When the user asks a question, the chain first looks at the chat history (ChatMessageHistory) to reformulate the user's query into a standalone question. This ensures that follow-up questions like "What about the second chapter?" are understood.
Similarity Search: The reformulated question is used to search the vector store for the most relevant document chunks.
Augmented Prompting: The retrieved text chunks are then "stuffed" into a prompt along with the user's original question and the chat history.
LLM Response Generation: This augmented prompt is sent to the Gemma2-9b-It model via the Groq API, which generates a concise and accurate answer based only on the provided context.
🛠️ Technology Stack
Application Framework: Streamlit
Orchestration Framework: LangChain
LLM Provider: Groq (using Gemma2-9b-It model)
Embedding Model: Hugging Face (all-MiniLM-L6-v2)
Vector Store: Chroma DB
Document Loader: PyPDFLoader
Environment Management: python-dotenv
🚀 Getting Started
Follow these steps to set up and run the project on your local machine.
Prerequisites
Python 3.8 or higher
pip (Python package installer)
1. Clone the Repository
If you haven't already, clone your main repository to your local machine:
git clone [https://github.com/kanhaiya-98/GenAI-Lab.git](https://github.com/kanhaiya-98/GenAI-Lab.git)
cd GenAI-Lab


2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies for this project.
Create the environment:
python -m venv venv


Activate the environment:
On Windows:
.\venv\Scripts\activate


On macOS & Linux:
source venv/bin/activate


3. Install Dependencies
Install all the required Python packages from within the project folder.
pip install -r RAG-Q&A-WITH-PDF-&-CHAT-HISTORY/requirements.txt


4. Configure Environment Variables
Create a file named .env inside the RAG-Q&A-WITH-PDF-&-CHAT-HISTORY directory. This file will store your Hugging Face API token.
HF_TOKEN="your_hugging_face_api_token"


Note: You can get your Hugging Face token from your Hugging Face profile settings.
5. Run the Application
Launch the Streamlit application using the following command from the root of the repository (GenAI-Lab):
streamlit run RAG-Q&A-WITH-PDF-&-CHAT-HISTORY/app.py


Your default web browser will automatically open a new tab with the application running.
📖 Usage
Enter Groq API Key: When the application loads, you will be prompted to enter your Groq API key. You can get one from the Groq Console.
Set Session ID: Optionally, change the session ID to maintain separate conversations.
Upload PDFs: Drag and drop or browse to upload the PDF files you want to chat with.
Ask Questions: Once the files are processed, you can start asking questions in the text input box at the bottom. The assistant's response and the ongoing chat history will be displayed.

