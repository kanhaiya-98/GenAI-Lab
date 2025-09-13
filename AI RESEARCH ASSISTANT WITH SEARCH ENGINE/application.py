# Import necessary libraries
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import AgentExecutor, create_react_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.memory import ConversationBufferWindowMemory
from langchain import hub

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UI & STYLING ---
st.title("🔎 AI Research Assistant")
st.markdown("""
Welcome to your AI-powered Research Assistant! I can search the web, browse Wikipedia, and find academic papers on arXiv. 
To get started, please enter your Groq API key in the sidebar.
""")

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .stChatMessage {
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .st-emotion-cache-janbn0 {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR SETUP ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    # API Key Input
    api_key = st.text_input(
        "Enter your Groq API Key:", 
        type="password", 
        help="Get your free API key from [GroqCloud](https://console.groq.com/keys)."
    )
    
    # Model Selection - Updated with current models
    model_name = st.selectbox(
        "Select Model",
        ("llama-3.3-70b-versatile","openai/gpt-oss-120b","openai/gpt-oss-20b", "mixtral-8x7b-32768"),
        index=0
    )
    
    st.markdown("---")
    st.header("🛠️ Tools")
    st.write("This agent uses the following tools to answer your questions:")
    st.info("- **DuckDuckGo**: For general web searches.\n"
            "- **Wikipedia**: For factual lookups on a wide range of topics.\n"
            "- **ArXiv**: For searching scientific and academic papers.")
    st.markdown("---")
    # Clear Chat Button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()


# --- AGENT AND TOOLS INITIALIZATION ---
# Initialize the tools the agent will use
@st.cache_resource
def get_tools():
    """Initializes and returns a list of tools for the agent."""
    # DuckDuckGo for general web searches
    search = DuckDuckGoSearchRun(name="Search")
    
    # ArXiv for academic paper searches
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
    
    # Wikipedia for encyclopedic knowledge
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    
    return [search, arxiv, wiki]

tools = get_tools()

# --- SESSION STATE MANAGEMENT ---
# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your AI Research Assistant. How can I help you today?"}
    ]

# Initialize agent memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        k=5, 
        return_messages=True,
        memory_key="chat_history"
    )

# --- CHAT INTERFACE ---
# Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if prompt := st.chat_input(placeholder="e.g., What are the latest advancements in AI?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Check for API key
    if not api_key:
        st.info("Please add your Groq API key to continue.")
        st.stop()

    # Initialize the LLM with the API key and selected model
    llm = ChatGroq(
        groq_api_key=api_key, 
        model_name=model_name,
        temperature=0,
        streaming=True
    )

    # Pull the ReAct agent prompt template
    prompt_template = hub.pull("hwchase17/react-chat")

    # Create the agent using the modern create_react_agent function
    agent = create_react_agent(llm, tools, prompt_template)

    # Create the agent executor
    # handle_parsing_errors=True helps prevent crashes on malformed LLM output
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True,
        memory=st.session_state.memory
    )
    
    # Execute the agent and display the response
    with st.chat_message("assistant"):
        # Use StreamlitCallbackHandler to display agent's thoughts and actions
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        
        # Invoke the agent with the user's prompt and callbacks
        response = agent_executor.invoke(
            {"input": prompt},
            {"callbacks": [st_cb]}
        )
        
        # Extract and display the final response
        output = response["output"]
        st.session_state.messages.append({"role": "assistant", "content": output})
        st.markdown(output)

