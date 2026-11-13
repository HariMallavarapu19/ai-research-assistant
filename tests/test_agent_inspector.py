from langchain.messages import HumanMessage,AIMessage,ToolMessage
from app.services.agent_inspector import inspect_agent_response

def test_agent_inspector():
    messages=[
        HumanMessage(content="Calculate 250 multiplied by 48"),
        AIMessage(
            content="",
            tool_calls=[
                {
                    "name":"calculator",
                    "args":{"expression":"250*48"},
                    "id":"call_123",
                    "type":"tool_call"
                }
            ]),
        ToolMessage(
            content="12000",
            tool_call_id="call_123"
        ),
        AIMessage(content="250 multipleid by 48 is 12000")
    ]

    response={"messages":messages}
    inspect_agent_response(response)
if __name__=="__main__":
    test_agent_inspector()

 