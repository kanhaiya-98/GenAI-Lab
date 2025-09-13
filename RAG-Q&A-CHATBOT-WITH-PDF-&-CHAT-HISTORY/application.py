# RAG Q&A Conversation With PDF Including Chat History

# Import necessary libraries
import streamlit as st
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os

# Import and load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Set the Hugging Face API token from environment variables
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")

# Initialize the embedding model from Hugging Face
# This model converts text into numerical vectors.
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# --- Streamlit App Interface ---

# Set the title for the Streamlit app
st.title("Conversational RAG With PDF Uploads and Chat History")
# Add a descriptive subtitle
st.write("Upload PDFs and chat with their content.")

# Create a text input field for the user to enter their Groq API key
api_key = st.text_input("Enter your Groq API key:", type="password")

# --- Core Application Logic ---

# Check if the Groq API key has been provided
if api_key:
    # Initialize the Language Model (LLM) from Groq with the provided API key
    llm = ChatGroq(groq_api_key=api_key, model_name="Gemma2-9b-It")

    # Create a text input for the session ID to manage different conversations
    session_id = st.text_input("Session ID", value="default_session")

    # Initialize a session state to store chat histories if it doesn't already exist
    # This ensures that chat history persists across reruns of the script.
    if 'store' not in st.session_state:
        st.session_state.store = {}

    # Create a file uploader for PDF files, allowing multiple uploads
    uploaded_files = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=True)
    
    # --- Document Processing and Vectorization ---
    
    # Process the uploaded files if any
    if uploaded_files:
        documents = []
        # Loop through each uploaded file
        for uploaded_file in uploaded_files:
            # Save the uploaded file temporarily to disk to be read by PyPDFLoader
            temppdf = f"./temp.pdf"
            with open(temppdf, "wb") as file:
                file.write(uploaded_file.getvalue())
            
            # Load the PDF using PyPDFLoader
            loader = PyPDFLoader(temppdf)
            docs = loader.load()
            # Add the loaded documents to our list
            documents.extend(docs)

        # Split the documents into smaller chunks for processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
        splits = text_splitter.split_documents(documents)
        
        # Create a vector store from the document splits using the embedding model
        # This allows for efficient similarity searches.
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        
        # Create a retriever from the vector store to fetch relevant documents
        retriever = vectorstore.as_retriever()

        # --- Context-Aware Retriever Chain ---

        # This system prompt helps the LLM reformulate the user's question 
        # to be a standalone question based on the chat history.
        contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
        
        # Create a prompt template for contextualizing the question
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"), # Placeholder for chat history
                ("human", "{input}"), # Placeholder for the user's input
            ]
        )
        
        # Create a history-aware retriever chain that first contextualizes the question
        # and then retrieves relevant documents.
        history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

        # --- Question-Answering Chain ---

        # This system prompt instructs the LLM on how to answer the question
        # using the retrieved context.
        system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise."
            "\n\n"
            "{context}" # Placeholder for the retrieved context
        )
        
        # Create a prompt template for the final QA step
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        
        # Create a chain to combine the retrieved documents and pass them to the LLM
        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        
        # Create the final retrieval chain that combines the retriever and the QA chain
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        # --- Session History Management ---

        # Function to get the chat history for a specific session ID
        def get_session_history(session: str) -> BaseChatMessageHistory:
            if session_id not in st.session_state.store:
                # If no history exists for the session, create a new one
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]
        
        # Create a runnable that integrates the RAG chain with session history management
        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

        # --- User Interaction and Response ---

        # Create a text input for the user's question
        user_input = st.text_input("Your question:")
        if user_input:
            # Retrieve the session history
            session_history = get_session_history(session_id)
            
            # Invoke the conversational RAG chain with the user's input and session ID
            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}},
            )
            
            # Display the entire session state (for debugging or visibility)
            st.write(st.session_state.store)
            
            # Display the assistant's answer
            st.write("Assistant:", response['answer'])
            
            # Display the current chat history
            st.write("Chat History:", session_history.messages)

else:
    # Show a warning if the Groq API key is not entered
    st.warning("Please enter the Groq API Key to proceed.")
