

import asyncio


async def call_tool(name: str , delay: int):
    print(f"Tool {name} started...")
    await asyncio.sleep(delay)
    return f"{name} result"

async def main():
    results =await asyncio.gather(
        call_tool("WebServer" , 2),
        call_tool("Database" , 1),
        call_tool("Calculator" , 0.5)
    )
    print(f"Agent processes all results: {results}")

asyncio.run(main())    