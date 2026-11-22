from langchain.messages import HumanMessage,AIMessage,ToolMessage
from app.services.tool_extractor import extract_tools_used

def test_extract_single_tool():
    response={
        "messages":[
            HumanMessage(content="Calculate 250*48"),
            AIMessage(
                content='',
                tool_calls=[
                    {

                        "name":"calculator",
                        "args":{"expression":"250*48"},
                        "id":"call_123",
                        "type":"tool_call"
                    }
                ]
            ),
            ToolMessage(content="12000",tool_call_id="call_123"),
            AIMessage(content="The answer is 12000")
        ]
    }
    tools=extract_tools_used(response)
    assert tools==['calculator']

def test_extract_multiple_tools():
    response={
        "messages":[
            HumanMessage(content="Research and calculate"),
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "tavily_search",
                        "args": {"query": "AI developments"},
                        "id": "call_123",
                        "type": "tool_call"
                    },
                    {
                        "name": "calculator",
                        "args": {"query": "250*34"},
                        "id": "call_234",
                        "type": "tool_call"
                    }
                ]
            ),
            ToolMessage(content="Search results",tool_call_id="call_123"),
            ToolMessage(content="12000",tool_call_id="call_234"),
            AIMessage(content="Research completed")
        ]
    }

    tools=extract_tools_used(response)
    assert tools==["tavily_search","calculator"]

def test_extract_no_tools():
    response={
        "messages":[
            HumanMessage(content="Hello"),
            AIMessage(content="HEllo how can i help you")
        ]
    }
    tools=extract_tools_used(response)
    assert tools==[]

if __name__=="__main__":
    test_extract_single_tool()
    test_extract_multiple_tools()
    test_extract_no_tools()

    print("All tool extractor tests passed")