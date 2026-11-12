import os
from dotenv import load_dotenv

load_dotenv()
class Settings():
    GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY","")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    MODEL_NAME:str="gemini-3.6-flash"
    

settings=Settings()

