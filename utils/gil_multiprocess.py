from multiprocessing import Process
from time import time


def crunch_number_tool():
    print(f"Started the count tool in process {Process().name}")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished the count tool in process {Process().name}")


if __name__ == "__main__":

    start = time()

    p1 = Process(target=crunch_number_tool, name="Cruncher-1")
    p2 = Process(target=crunch_number_tool, name="Cruncher-2")

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f"Total time taken: {end - start:.2f} seconds")