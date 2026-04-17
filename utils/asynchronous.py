import asyncio
import time


async def tool_call(tool_name: str):
    print(f"Start of {tool_name} tool call")
    await asyncio.sleep(2)
    print(f"End of {tool_name} tool call")

async def main():
    await asyncio.gather(tool_call("Example Tool"), tool_call("Another Tool"), tool_call("Third Tool")
                         )

if __name__ == "__main__":
    asyncio.run(main())