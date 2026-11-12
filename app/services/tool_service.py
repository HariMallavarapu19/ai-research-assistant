from app.core.llm import get_llm
from app.tools.tool_registry import get_tools
from langchain.messages import ToolMessage



def research_with_tools(query:str):
    llm=get_llm()
    tools=get_tools()
    llm_with_tools=llm.bind_tools(tools)
    tool_map={
        tool.name:tool
        for tool in tools
    }
    messages = [
        (
            "system",
            """You have access to these tools:

            1. Tavily Search:
               Use for current information and web research.

            2. Calculator:
               Use for mathematical calculations.

            3. Wikipedia:
               Use for general knowledge and encyclopedic information.

            Select the appropriate tool when necessary.

            Never invent tool results.
            
            """

        ),
        ("human", query),
    ]

    response=llm_with_tools.invoke(messages)

    while response.tool_calls:
        messages.append(response)
   
        for tool_call in response.tool_calls:
            tool_name=tool_call['name']
            tool_args=tool_call['args']
            print(f"\nExecuting tool:{tool_name}")
            selected_tool=tool_map.get(tool_name)
            if selected_tool is None:
                result=f"Unknown tool:{tool_name}"
            else:
                result=selected_tool.invoke(tool_args)

            tool_message=ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
            messages.append(tool_message)
        response=llm_with_tools.invoke(messages)
   
    return response.content


 