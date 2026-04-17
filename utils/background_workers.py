import threading
import time
import asyncio

def background_task(task_id):
    while True:
        print(f"Background task {task_id} is running.")
        time.sleep(1)

async def tool_call(tool_name: str):
    await asyncio.sleep(3)
    print(f"End of {tool_name} tool call")

if __name__ == "__main__":
    threading.Thread(target=background_task, args=(1,), daemon=True).start()

    asyncio.run(tool_call("Example Tool"))