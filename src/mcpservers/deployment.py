from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Arithmetic-Add")

@mcp.tool()
def add(a:int, b:int) -> int:
    """Adds two numbers together"""
    return a + b