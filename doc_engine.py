import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.llms.google_genai import GoogleGenAI

# Load env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# Use Gemini for both LLM and embeddings
llm = GoogleGenAI(model="gemini-2.0-flash", api_key=GEMINI_API_KEY)
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Set LlamaIndex global settings
Settings.llm = llm
Settings.embed_model = embed_model

# Load your text data (like stress_managment.txt)
documents = SimpleDirectoryReader("data").load_data()

# Build the vector index with Gemini embeddings
index = VectorStoreIndex.from_documents(documents)

# Create query engine
query_engine = index.as_query_engine(llm=llm)

def query_documents(user_query: str) -> str:
    """Query your document knowledge base."""
    response = query_engine.query(user_query)
    return str(response)