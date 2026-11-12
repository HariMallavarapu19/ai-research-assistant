from langchain_tavily import TavilySearch
from app.core.config import settings

def get_search_tool():
    if not settings.TAVILY_API_KEY:
        raise ValueError(
            "tavily key is missing"
        )
    search_tool=TavilySearch(
        tavily_api_key=settings.TAVILY_API_KEY,
        max_results=5,
        topic="general"
    )

    return search_tool

