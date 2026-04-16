from multiprocessing import Process
import time

def tool_call(tool_name: str):
    print(f"Start of {tool_name} tool call")
    time.sleep(2)
    print(f"End of {tool_name} tool call")


if __name__ == "__main__":

    tool_calls = [
        Process(target=tool_call, args=(f"Tool #{i+1}",)) for i in range(3)
    ]

    for process in tool_calls:
        process.start()

    # Wait for all tool calls to finish
    for process in tool_calls:
        process.join()

    print("All tool calls completed successfully.")
