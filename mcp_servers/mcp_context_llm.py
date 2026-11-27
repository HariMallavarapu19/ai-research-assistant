import asyncio
import sys
from mcp.client.stdio import stdio_client
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters
from app.core.llm import get_llm

async def main():
    server_params=StdioServerParameters(
        command=sys.executable,
        args=["-u","-m","mcp_servers.basic_server"]
    )

    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            resource_result=await session.read_resource(
                "project://info"
            )

            resource_context="\n".join(
                content.text for content in resource_result.contents
                if hasattr(content,"text")
            )
            print("/n__Resource Context----")
            print(resource_context)

            topic=input("\nEnter research topic:")
            prompt_result=await session.get_prompt(
                "research_prompt",
                arguments={
                    "topic":topic
                }
            )

            prompt_text='\n'.join(
                message.content.text
                for message in prompt_result.messages
                if hasattr(message.content,'text')
            )

            print(prompt_text)

            final_input = f"""
            PROJECT CONTEXT:

            {resource_context}

            RESEARCH INSTRUCTIONS:

            {prompt_text}

            Use the project context where relevant.
            Follow the research instructions carefully.
            """

            llm=get_llm()
            response=await llm.ainvoke(final_input)

            print("+++++++++Research Report+++++++++++++")
            print(response.content)

if __name__=="__main__":
    asyncio.run(main())

    