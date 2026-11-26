import asyncio 
import os
import sys
from pathlib import Path
import logging
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from app.core.llm import get_llm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger=logging.getLogger(__name__)


async def main():
    github_token=os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
    if not github_token:
        raise RuntimeError("GitHub token not found in environment")

    client=MultiServerMCPClient(
        {
            "github":{
                "transport":"stdio",
                "command":"docker",
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
                },
            }
        }
    )

    max_retires=3

    for attempt in range(1,max_retires+1):
        try:
            logger.info("Attempt %s to load GitHub tools",attempt)
            tools=await asyncio.wait_for(
                client.get_tools(),
                timeout=30
            )

            tools=[
                tool for tool in tools
                if tool.name=="search_repositories"
            ]

            logger.info("loaded %s Github mcp tools",len(tools))
            break
        except asyncio.TimeoutError:
            logger.warning("Tool loading timeout on attempt %s",attempt)

        except Exception:
            logger.exception("Tool loading failed on attempt %s",attempt)

        if attempt<max_retires:
            await asyncio.sleep(2**(attempt-1))

    else:
        logger.error("Github MCP failed after %s attempts",max_retires)
        return

    agent=create_agent(
        model=get_llm(),
        tools=tools
    )

    response=await agent.ainvoke(
        {
        "messages":[
            {
                "role":"user",
"content": """
Find a GitHub repository named ai-research-assistant.

Search GitHub for the repository.

Before reporting any result, validate:
1. The repository name must be exactly ai-research-assistant.
2. The owner must be HariMallavarapu19.

If the repository doesn't match both conditions,
do not report it as the requested repository.

Return:
- Owner
- Repository name
- Description
- Primary language
- URL
- Stars

If you cannot verify the repository, clearly say so.
"""            }
        ]
        }
    )

    print('\n--Agent Responnse----')

    for message in response['messages']:
        print("Message type:{type(message).__name__}")
        print(f"Content:{message.content}")

        if hasattr(message,"tool_calls") and message.tool_calls:
            
            print("tool_call")
            for tool_call in message.tool_calls:
                print(tool_call)

        if message.type=='tool':
            print("tool executionn result:")
            print(message.content)


if __name__=="__main__":
    asyncio.run(main())




