from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():
    if not settings.GOOGLE_API_KEY:
        raise ValueError("api key is missing.Please config it in your .env file")

    llm=ChatGoogleGenerativeAI(
        model=settings.MODEL_NAME,
        google_api_key=settings.GOOGLE_API_KEY,
        
    )

    return llm

