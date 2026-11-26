from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings
from langchain_groq import ChatGroq
import os

def get_llm():

    groq_api_key=os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("api key is missing.Please config it in your .env file")

    llm=ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=groq_api_key,
        temperature=0
    )

    return llm

