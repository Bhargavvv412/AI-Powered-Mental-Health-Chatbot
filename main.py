import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest
from chat_engine import get_response
from crisis import contains_crisis_keywords, SAFETY_MESSAGE
from doc_engine import query_documents
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Mental Health Chatbot",
    description="An AI-based chatbot for stress and emotional support.",
    version="1.0.0"
)


app.mount("/chatbot-ui", StaticFiles(directory="chatbot-ui"), name="chatbot-ui")

# Enable CORS (so frontend can talk to backend easily)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # You can specify your frontend URL later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def home():
    return {"message": "Mental Health Chatbot API is running!"}


# Chat endpoint
@app.post("/chat")
async def chat_with_memory(request: ChatRequest):
    session_id = request.session_id
    user_query = request.query
    
    # Check for crisis keywords
    if contains_crisis_keywords(user_query):
        return {"response": SAFETY_MESSAGE}

    # Get LLM-generated response
    response = get_response(session_id, user_query)

    return {"response": response}


@app.post("/doc-chat")
def chat_with_documents(request: ChatRequest):
    response = query_documents(request.query)
    return{"response":response}