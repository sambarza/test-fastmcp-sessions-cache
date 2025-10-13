from fastmcp import FastMCP
import fastmcp

fastmcp.settings.log_level = "DEBUG"

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

def get_favorite_color(name: str) -> str:
    if name.lower() == "alice":
        return "red"
    elif name.lower() == "bob":
        return "green"
    elif name.lower() == "sam":
        return "blue"
    else:
        return "yellow"

@mcp.tool()
def favorite_color(name: str) -> str:
    """_summary_

    Args:
        name (str): name of the person

    Returns:
        str: favorite color of the person
    """
    print(f"Finding favorite color for {name}")
    favorite_color = get_favorite_color(name)
    print(f"{name}'s favorite color is {favorite_color}")

    return favorite_color

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=9000)