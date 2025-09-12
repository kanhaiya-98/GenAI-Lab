import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# --- LOAD ENVIRONMENT VARIABLES ---
# Load environment variables from a .env file for better security
load_dotenv()

# Set up Langsmith tracking if you want to monitor your LLM applications
# Make sure to set these in your .env file
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "false")
if os.environ["LANGCHAIN_TRACING_V2"].lower() == "true":
    os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

# --- PAGE CONFIGURATION ---
# Set the page configuration for a more professional look
st.set_page_config(
    page_title="Local LLM Chatbot",
    page_icon="🧠", # Using a more professional icon
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- STYLES ---
# Custom CSS for a professional dark theme
st.markdown("""
<style>
    /* Overall App Theme */
    .stApp {
        background-color: #1a1a1a; /* Dark background */
        color: #e6e6e6; /* Light text for readability */
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1f1f1f;
        border-right: 1px solid #333;
    }
    
    /* Titles and Headers */
    h1, h2, h3 {
        color: #ffffff;
    }
    .st-emotion-cache-1xarl3l { /* Streamlit's caption class */
        color: #a0a0a0;
    }

    /* Chat Message Bubbles */
    [data-testid="stChatMessage"] {
        padding: 1rem 1.25rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        border: 1px solid transparent;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Assistant's Chat Bubble */
    [data-testid="stChatMessage"]:has(span[data-testid="chatAvatarIcon-assistant"]) {
        background-color: #2b2b2b; /* Darker grey for assistant */
    }

    /* User's Chat Bubble */
    [data-testid="stChatMessage"]:has(span[data-testid="chatAvatarIcon-user"]) {
        background-color: #0d47a1; /* A deeper, more professional blue */
    }
    
    /* Chat Input Box */
    [data-testid="stChatInput"] {
        background-color: #1a1a1a;
        border-top: 1px solid #333;
    }
    .st-emotion-cache-1629p8f { /* Input text area */
        background-color: #2b2b2b;
        color: #e6e6e6;
        border-radius: 0.5rem;
        border: 1px solid #444;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 0.5rem;
        background-color: #007bff;
        color: white;
        border: none;
        transition: background-color 0.2s, transform 0.1s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stButton>button:active {
        transform: scale(0.98);
    }
    .stButton>button:focus {
        outline: none;
        box-shadow: 0 0 0 2px #007bff;
    }

</style>
""", unsafe_allow_html=True)


# --- PROMPT TEMPLATE ---
# A more conversational and structured prompt template with a placeholder for history
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a knowledgeable and friendly assistant. Your goal is to provide clear and concise answers based on the provided conversation history."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

# --- LLM CHAIN FUNCTION ---
# This function creates and returns the LLM chain. Caching it improves performance.
@st.cache_resource
def get_llm_chain(model, temperature, num_predict):
    """
    Initializes and returns a LangChain chain.
    Using st.cache_resource ensures the model is loaded only once.
    """
    # Initialize the Ollama LLM with specified parameters
    llm = Ollama(model=model, temperature=temperature, num_predict=num_predict)
    output_parser = StrOutputParser()
    chain = prompt_template | llm | output_parser
    return chain

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("Model Configuration")
    st.markdown("Select a local model and adjust its parameters.")
    
    # Model selection
    selected_model = st.selectbox(
        "Choose a model",
        ["llama3.1:8b","llama3", "phi3", "mistral", "gemma"],
        key="selected_model"
    )

    # Temperature slider for creativity
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controls the randomness of the output. Lower is more deterministic."
    )

    # Max tokens (num_predict for Ollama) slider for response length
    num_predict = st.slider(
        "Max Response Length",
        min_value=100,
        max_value=1000,
        value=150,
        step=10,
        help="Maximum number of tokens to generate in the response."
    )

    st.markdown("---")
    
    # Button to clear chat history
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- MAIN CHAT INTERFACE ---
st.title("Local LLM Chatbot")
st.caption(f"Powered by Ollama and the `{selected_model}` model")


# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome. I am your local AI assistant. Please select a model from the sidebar and ask me anything."}
    ]

# Display past messages from the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT AND RESPONSE GENERATION ---
# Get user input from the chat input box
if user_question := st.chat_input("Ask me anything..."):
    # Add user's message to the chat history and display it
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Get the LLM chain
            chain = get_llm_chain(selected_model, temperature, num_predict)
            
            # Invoke the chain with the user's question and the chat history
            response = chain.invoke({
                "question": user_question,
                "chat_history": st.session_state.messages 
            })
            
            # Display the response
            st.write(response)

    # Add assistant's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

