import time, random

def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(2, 10))
    print("Worker 1 finished!")

def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(2, 10))
    print("Worker 2 finished!")

start = time.time()
worker1()
print(f"Worker 1 process time: {time.time() - start}")

start = time.time()
worker2()
print(f"Worker 2 process time: {time.time() - start}")