import time, random


def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start}")

        return result

    return wrapper


def i_do_nothing(func):
    def wrapper(*args, **kwargs):
        print("Hello! I do nothing ;)")
        result = func(*args, **kwargs)
        return result
    
    return wrapper


@i_do_nothing
@my_timer
def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(2, 10))
    print("Worker 1 finished!")

@my_timer
def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(2, 10))
    print("Worker 2 finished!")

@my_timer
def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(2, 10))
    print("Worker 3 finished!")


worker1()
worker2()
worker3()