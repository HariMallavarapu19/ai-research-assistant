import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters
import sys

async def main():
    server_params=StdioServerParameters(
        command=sys.executable,
        args=["mcp_servers/basic_server.py"]
    )

    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            prompts=await session.list_prompts()

            print("Available prompts:")
            print(prompts)

            prompt=await session.get_prompt(
                "research_prompt",
                arguments={
                    "topic":"Artficial Intelligence Agents"
                }
            )

            print("\n__-Retriveed Prompt----")
            print(prompt)

if __name__=="__main__":
    asyncio.run(main())
    