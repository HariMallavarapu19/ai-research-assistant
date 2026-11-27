import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

from app.core.llm import get_llm
from app.core.config import settings


async def main():
    github_token=os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

    if not github_token:
        raise RuntimeError("Github token not found")

    client=MultiServerMCPClient(
        {
            "github":{
                "transport":"stdio",
                "command":"docker" ,
                "args":[
                    "run",
                    "-i",
                    "--rm",
                    "--read-only",
                    "-e",
                    "GITHUB_PERSONAL_ACCESS_TOKEN",
                    "-e",
                    "GITHUB_READ_ONLY=1",
                    "ghcr.io/github/github-mcp-server"
                ],
                "env":{
                    "GITHUB_PERSONAL_ACCESS_TOKEN":github_token
                }
            },
            "basic":{
                "transport":"stdio",
                "command":"python",
                "args":["mcp_servers/basic_server.py"]
            }
        }
    )

    all_tools=await client.get_tools()

    print("\nDiscovered tools:")

    for tool in all_tools:
        print(tool.name)

    ALLOWED_TOOLS={
        "search_repositories",
        "add_numbers",
        "get_project_info"
    }

    tools=[
        tool for tool in all_tools
        if tool.name in ALLOWED_TOOLS
    ]

    print("Allowed tools:")
    print([tool.name for tool in tools])

    agent=create_agent(
        model=get_llm(),
        tools=tools
    )

    response=await agent.ainvoke(
        {
            "messages":[
                {
                    "role":"user",
                    'content':"""
                           1.Add 25 and 17 using tool.
                           2.Get the project information using a tool
                           3.Seaarch Github for the repository named 
                              ai research assistant.

                            present all three results clearly.
                    """
                }
            ]
        }
    )
    print("\n---Agent Response---")
    print(response)

if __name__=="__main__":
    asyncio.run(main())

