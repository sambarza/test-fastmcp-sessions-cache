import asyncio
from fastmcp import Client

mcp_open_clients = {}

async def create_mcp_client_session(user: str):
    print("Creating new client for user:", user)
    client = Client("http://localhost:9000/mcp")
    await client.__aenter__()

    mcp_open_clients[user] = client
    print("Client context saved for user:", user)

    return mcp_open_clients[user]

async def call_tool(user: str):

    if user not in mcp_open_clients:
        await create_mcp_client_session(user)

    user_client = mcp_open_clients[user]

    result = await user_client.call_tool("greet", {"name": user}, timeout=3)

    print(result)

async def close_session(user: str):
    if user in mcp_open_clients:
        client = mcp_open_clients[user]
        await client.__aexit__(None, None, None)
        
async def test():

    for i in range(200):
        await call_tool(f"Alice {i}")

    await call_tool(f"Alice 10")

    input("Press Enter to close sessions...")

    for i in range(200):
        await close_session(f"Alice {i}")
    
    input("Press Enter to exit...")

asyncio.run(test())
