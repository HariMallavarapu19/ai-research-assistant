
from mcp import Client,StdioServerParameters
import asyncio

async def main():
    server_params=StdioServerParameters(
        command="python",
        args=['mcp_servers/basic_server.py']
    )

    async with Client(server_params) as client:
        tools=await client.list_tools()
        print("Available tools")

        for tool in tools.tools:
            print(f"-{tool.name}:{tool.description}")

        result=await client.call_tool(
            "add_numbers",{"a":10,'b':20}
        )

        print("\nTool result")
        print(result)


if __name__=="__main__":
    asyncio.run(main())