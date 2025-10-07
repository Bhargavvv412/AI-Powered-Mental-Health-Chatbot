import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# load env
load_dotenv()
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("API key not found")

llm = GoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7,api_key=GEMINI_API_KEY)

#store per person memomery session

session_memory_map = {}

def get_response(session_id: str,user_query:str)->str:
    if session_id not in session_memory_map:
        memory  = ConversationBufferMemory()
        session_memory_map[session_id] = ConversationChain(llm=llm,memory=memory,verbose=True)

    conversation = session_memory_map[session_id]
    return conversation.predict(input=user_query)