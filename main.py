import sys
import numpy as np
from os import path
from PIL import Image

def get_image_path() -> str:
    if len(sys.argv) <= 1:
        print("there is no arguments")
        exit(0)

    file_path = sys.argv[1]

    if not path.isfile(file_path):
        print("not a file")
        exit(0)

    print(sys.argv)
    
    return file_path

def load_image(file_path: str):

    img = Image.open(file_path).convert("RGBA")

    img.show()

    print(img)

    arr = np.array(img)

    print(arr)

    return arr

if __name__ == "__main__":
    img_path = get_image_path()
    arr = load_image(img_path)