from app.tools.search_tool import get_search_tool
from app.tools.calculator_tool import calculator
from app.tools.wikipedia_tool import wikipedia_search

def get_tools():
    search_tool=get_search_tool()
    tools=[
        search_tool,
        calculator,
        wikipedia_search
    ]

    return tools

