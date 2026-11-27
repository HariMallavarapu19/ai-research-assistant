import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.stdio import StdioServerParameters

async def main():
    server_params=StdioServerParameters(
        command="python",
        args=["mcp_servers/basic_server.py"]
    )

    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            resources=await session.list_resources()
            print("Available resources")
            print(resources)
            resource=await session.read_resource(
                "project://info"
            )

            print("\n--Resource Content---")
            print(resource)

if __name__=="__main__":
    asyncio.run(main())

    
