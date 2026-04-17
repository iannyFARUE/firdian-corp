import asyncio 
import time
from concurrent.futures import ThreadPoolExecutor

def tool_call(tool_name: str):
    print(f"Start of {tool_name} tool call")
    time.sleep(2)
    print(f"End of {tool_name} tool call")
    return f"{tool_name} completed"

async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, tool_call, "Example Tool")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    print("All tool calls completed successfully.")