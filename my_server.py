from fastmcp import FastMCP
from fastmcp import utilities

# Log payloads for debugging to console
utilities.logging.get_logger("fastmcp").setLevel("DEBUG")

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)