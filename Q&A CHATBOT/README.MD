🤖 Local LLM Q&A ChatbotA simple, yet powerful and beautifully designed Q&A chatbot that runs entirely on your local machine using Streamlit and Ollama. This project allows you to interact with powerful open-source language models like Llama 3, Phi-3, and Mistral without needing an internet connection or paying for API access.It features a clean, modern user interface with chat history, model selection, and parameter tuning.📸 Screenshot(Note: You should replace this link with a real screenshot of your running application!)✨ Key FeaturesInteractive Chat Interface: A clean, modern UI for a seamless conversational experience.Chat History: Remembers your conversation within a session.Local LLM Support: Powered by Ollama, allowing you to run various open-source models (Llama 3, Phi-3, etc.) locally.Model Configuration: Easily switch between different models available on your system via a dropdown menu.Parameter Tuning: Adjust Temperature and Max Response Length in real-time to control the model's creativity and verbosity.Secure & Private: Since the models run locally, your data and conversations never leave your machine.Built with Modern Tools: Utilizes Streamlit for the frontend and LangChain for structuring the LLM interaction.🛠️ Tech StackFramework: StreamlitLLM Orchestration: LangChainLLM Hosting: OllamaLanguage: Python📋 PrerequisitesBefore you begin, ensure you have the following installed on your system:Python 3.8+Ollama: Follow the official installation guide at ollama.com.An Ollama-compatible Model: After installing Ollama, pull a model to use. For example, to get Llama 3:ollama pull llama3
🚀 Getting StartedFollow these steps to get the chatbot up and running on your local machine.1. Clone the RepositoryFirst, clone this repository to your local machine using Git:git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Create a Virtual EnvironmentIt's highly recommended to use a virtual environment to keep your project dependencies isolated.# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install DependenciesInstall all the required Python packages using the requirements.txt file:pip install -r requirements.txt

4. Set Up Environment Variables (Optional)This project is configured to use Langsmith for tracking and debugging your LLM calls. If you want to use it:Sign up at langsmith.com.Create a .env file in the root of your project directory.Add your Langsmith API key to the .env file:LANGCHAIN_API_KEY="your_langsmith_api_key_here"
LANGCHAIN_TRACING_V2="true"
If you don't want to use Langsmith, the app will still work perfectly fine.▶️ How to Run the ApplicationWith your virtual environment activated and dependencies installed, run the Streamlit app with the following command:streamlit run app.py
Your web browser should automatically open to the application's URL (usually http://localhost:8501).You can now start chatting with your local LLM! 🎉