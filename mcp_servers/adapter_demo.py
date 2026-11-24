import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client=MultiServerMCPClient(
        {
            "basic_server":{
                "transport":"stdio",
                "command":"python",
                "args":["mcp_servers/basic_server.py"],
            }
        }
    )

    tools=await client.get_tools()

    print("Tools retrievve from MCP server:\n")

    for tool in tools:
        print(f"Name:{tool.name}")
        print(f"Description:{tool.description}")
        print("-"*40)

if __name__=="__main__":
    asyncio.run(main())

