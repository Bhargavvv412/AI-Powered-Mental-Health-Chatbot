import os
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.google_genai import GoogleGenAI

llm = GoogleGenAI(model="gemini-2.5-flash",api_key=os.getenv("GEMINI_API_KEY"))

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(llm=llm)

def query_documents(user_query: str)->str:
    return str(query_engine.query(user_query))