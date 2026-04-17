import asyncio


async def tool_call(tool_name: str):
    print(f"Start of {tool_name} tool call")
    await asyncio.sleep(2)
    print(f"End of {tool_name} tool call")

def main():
    asyncio.run(tool_call("Example Tool"))

if __name__ == "__main__":
    main()