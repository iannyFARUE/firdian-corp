from multiprocessing import Process, Queue
import time

queue = Queue()

def code_scanner_agent(queue):
    print(f"{Process().name} is starting the code scanning task.")
    time.sleep(2)
    queue.put("Code scanning completed.")

def code_reviewer_agent(queue):
    print(f"{Process().name} is starting the code reviewing task.")
    time.sleep(3)
    queue.put("Code reviewing completed.")


if __name__ == "__main__":
    scanner_process = Process(target=code_scanner_agent, args=(queue,), name="CodeScanner")
    reviewer_process = Process(target=code_reviewer_agent, args=(queue,), name="CodeReviewer")

    scanner_process.start()
    reviewer_process.start()

    scanner_process.join()
    reviewer_process.join()

    while not queue.empty():
        print(queue.get())

