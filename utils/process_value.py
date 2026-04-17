from multiprocessing import Process, Value

def increment_counter(counter):
    for _ in range(1000000):
        with counter.get_lock():  # Ensure that only one process can access the counter at a time
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # 'i' indicates a signed integer

    processes = [Process(target=increment_counter, args=(counter,)) for _ in range(4)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Final counter value: {counter.value}")