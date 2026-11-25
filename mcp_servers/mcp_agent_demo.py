import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from app.core.llm import get_llm

async def main():
    client=MultiServerMCPClient(
        {
            "basic_server":{
                "transport":"stdio",
                "command":"python",
                "args":["mcp_servers/basic_server.py"]
            }
        }
    )

    tools=await client.get_tools()

    print("MCP tools loaded")

    for tool in tools:
        print(f"-{tool.name}")

    agent=create_agent(
        model=get_llm(),
        tools=tools
    )

    response=await agent.ainvoke(
        {
            "messages":[
                {
                     "role":"user",
                     "content":"What is 25+17? Use the add_number tool"    
                }
            ]
        }
    )

    print('\nAgent responsne:')
    print(response['messages'][-1].content)

if __name__=="__main__":
    asyncio.run(main())