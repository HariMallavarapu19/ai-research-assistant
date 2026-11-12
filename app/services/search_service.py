from app.tools.search_tool import get_search_tool

def search_web(query:str):
    search_tool=get_search_tool()
    results=search_tool.invoke({
        "query":query
    })

    return results

