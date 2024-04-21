import time, random, queue, threading

file_list = [
    "image_0001.exr",
    "image_0002.exr",
    "image_0003.exr",
    "image_0004.exr",
    "image_0005.exr",
    "image_0006.exr",
    "image_0007.exr",
    "image_0008.exr",
    "image_0009.exr",
    "image_0010.exr",
    "image_0011.exr",
]

job_queue = queue.Queue()

# fill up job queue
for i in file_list:
    job_queue.put(i)

# converter worker
def convert_image_worker():
    while not job_queue.empty():
        file_path = job_queue.get()
        
        print(f"Conversion started: {file_path}")
        time.sleep(random.randint(3, 10))
        print(f"Conversion finished: {file_path}")

        job_queue.task_done()

# start workers
for _ in range(10):
    t = threading.Thread(target=convert_image_worker)
    t.start()