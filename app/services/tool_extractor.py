def extract_tools_used(response:dict):
    messages=response.get("messages",[])
    tools_used=[]
    for message in messages:
        if hasattr(message,"tool_calls") and message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name=tool_call['name']
                tools_used.append(tool_name)

    return tools_used


