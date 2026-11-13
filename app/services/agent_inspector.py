def inspect_agent_response(response):
    messages=response.get("messages",[])
    for index,message in enumerate(messages):
        print(f"\nMessage{index+1}")
        print("Type:",type(message).__name__)

        print("Content:",message.content)

        if hasattr(message,"tool_calls") and message.tool_calls:
            print("tool calls",message.tool_calls)

            