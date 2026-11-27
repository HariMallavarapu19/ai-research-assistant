from mcp.server.fastmcp import FastMCP

mcp=FastMCP("BasicServer")

@mcp.tool()
def add_numbers(a:int,b:int)->int:
    "Add two numbers and return the result"
    return a+b

@mcp.tool()
def get_project_info():
    "Just provide the what tthe project name is"
    return "AI Research Assistant"

@mcp.resource("project://info")
def project_info():
    """Provide basic project information."""
    return """
       Project:AI Research Assiatant
       Purpose:
       Build an AI-powered research assitant using Langchain,
       Langgraph,MCP and RAG.
       Currennt capabilities:
       -Web Search
       -calculator
       wikipedia
       -MCP Integration
       -Github MCP integration
       """ 

@mcp.prompt()
def research_prompt(topic:str)->str:
    """Generate a research prompt for a given topic."""
    return f"""
      Research the following topic;{topic}
      Structure your response as:
      1.Overview
      2.Key concepts
      3.Important findings
      4.Challenges
      5.Conclusion   
      Be factual and clearly distinguish facts from speculation.
"""

if __name__=="__main__":
    mcp.run()





