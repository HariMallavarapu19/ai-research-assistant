from app.core.llm import get_llm
from app.tools.search_tool import get_search_tool

def research_with_search(query:str):
    llm=get_llm()
    search_tool=get_search_tool()
    llm_with_tools=llm.bind_tools([search_tool])

    response=llm_with_tools.invoke(
        f"""
             YOu are an AI research assistant
             Research this qustion:{query}


            Use the web search tool when current information or external sources are needed
        """
    )

    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call['name']==search_tool.name:
                result=search_tool.invoke(
                    tool_call["args"]
                )
    else:
        print("\nGemini answerd without calling a tool")

    return response

 