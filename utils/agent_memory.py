import threading
from collections import defaultdict

lock = threading.Lock()

memory = defaultdict(list)

def agent_memory_task(agent_id):
    with lock:
        memory[agent_id].append(f"Memory entry for {agent_id}")


if __name__ == "__main__":
    agent_ids = [f"Agent-{i+1}" for i in range(5)]
    threads = []

    for agent_id in agent_ids:
        thread = threading.Thread(target=agent_memory_task, args=(agent_id,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Agent memory contents:")
    for agent_id, entries in memory.items():
        print(f"{agent_id}: {entries}")
