import multiprocessing
import os
import time

print("outside main")
def work(name):
    for i in range(10):
        print(f"{name} work {i} times in Progress{os.getpid()}")
        time.sleep(0.1)

def study(name):
    for i in range(10):
        print(f"{name} study {i} times in Progress{multiprocessing.current_process().pid}")
        time.sleep(0.2)

if __name__ == "__main__":
        p1 = multiprocessing.Process(target = work, args = ("abc",), name = "p1")
        p2 = multiprocessing.Process(target = study, kwargs = {"name":"efg"}, name = "p2")

        p1.start()
        p2.start()

        print("mian run")
