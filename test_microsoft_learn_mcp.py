import asyncio
import json

from fastmcp import Client

mcp_open_clients = {}

async def create_mcp_client_session(user: str):
    # print("Creating new client for user:", user)
    client = Client("https://learn.microsoft.com/api/mcp")
    await client.__aenter__()

    mcp_open_clients[user] = client
    # print("Client context saved for user:", user)

    return mcp_open_clients[user]


async def call_tool(user: str):

    if user not in mcp_open_clients:
        await create_mcp_client_session(user)

    user_client = mcp_open_clients[user]

    # result = await user_client.call_tool("greet", {"name": user}, timeout=3)

    # print(result)

    tools = await user_client.list_tools()
    prompts = await user_client.list_prompts()
    resources = await user_client.list_resources()

    print(json.dumps(tools, indent=2))
    print(json.dumps(prompts, indent=2))
    print(json.dumps(resources, indent=2))


async def close_session(user: str):
    if user in mcp_open_clients:
        client = mcp_open_clients[user]
        await client.__aexit__(None, None, None)


async def test():

    sessions_count = 10

    for i in range(sessions_count):
        await call_tool(f"Alice {i}")

    # input("Press Enter to call tool for Alice 1...")

    # await call_tool(f"Alice 1")

    # input("Press Enter to close sessions...")

    # for i in range(sessions_count):
    #     await close_session(f"Alice {i}")

    # input("Press Enter to exit...")

asyncio.run(test())