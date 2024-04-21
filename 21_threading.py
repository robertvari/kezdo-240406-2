import time, random

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

def convert_image():
    print("Convert started...")
    time.sleep(random.randint(3, 10))
    print("Convert finished!")