from mcp.server.mcpserver import MCPServer

mcp=MCPServer("BasicServer")

@mcp.tool()
def add_numbers(a:int,b:int)->int:
    "Add two numbers and return the result"
    return a+b

@mcp.tool()
def get_project_info():
    "Just provide the what tthe project name is"
    return "AI Research Assistant"
if __name__=="__main__":
    mcp.run()


