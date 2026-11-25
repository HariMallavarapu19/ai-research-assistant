import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    github_token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

    if not github_token:
        raise RuntimeError("GitHub token not found in environment!")

    client = MultiServerMCPClient(
        {
            "github": {
                "transport": "stdio",
                "command": "docker",
                "args": [
                    "run",
                    "-i",
                    "--rm",
                    "--read-only",
                    "-e",
                    "GITHUB_PERSONAL_ACCESS_TOKEN",
                    "-e",
                    "GITHUB_READ_ONLY=1",
                    "ghcr.io/github/github-mcp-server",
                ],
                "env": {
                    "GITHUB_PERSONAL_ACCESS_TOKEN": github_token,
                },
            }
        }
    )

    tools = await client.get_tools()

    print("\nGitHub MCP tools discovered:\n")

    for tool in tools:
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"Input Schema;{tool.args}")
        print("-" * 60)


if __name__ == "__main__":
    asyncio.run(main())