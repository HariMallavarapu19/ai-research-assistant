from app.core.llm import get_llm
from app.tools.search_tool import get_search_tool
from langchain.messages import ToolMessage



def research_with_search(query:str):
    llm=get_llm()
    search_tool=get_search_tool()
    llm_with_tools=llm.bind_tools([search_tool])

    messages = [
        (
            "system",
            "You are an AI research assistant. "
            "Use web search when external or current information is needed. "
            "Never invent search results."
        ),
        ("human", query),
    ]

    response=llm_with_tools.invoke(messages)

    while response.tool_calls:
        messages.append(response)
   
        for tool_call in response.tool_calls:
            if tool_call['name']==search_tool.name:
                result=search_tool.invoke(
                    tool_call["args"]
                )

                tool_message=ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
                messages.append(tool_message)
        response=llm_with_tools.invoke(messages)
   
    return response.content


 