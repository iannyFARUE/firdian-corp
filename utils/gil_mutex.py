import threading
import time

def multi_agent_task():
    print(f"{threading.current_thread().name} is starting the multi-agent task.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has completed the multi-agent task.")

if __name__ == "__main__":
    agent1 = threading.Thread(target=multi_agent_task, name="Agent-1")
    agent2 = threading.Thread(target=multi_agent_task, name="Agent-2")

    start = time.time()
    agent1.start()
    agent2.start()
    agent1.join()
    agent2.join()
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")
