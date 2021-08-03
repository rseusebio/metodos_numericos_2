import sys
from os import path
from typing import List 

def is_image(file_path: str) -> bool:
    img_exts = [
        "jpeg", 
        "jpg",
        "png"
    ]

    for ext in img_exts:
        if file_path.endswith("." + ext):
            return True

    return False
    
def get_imgs() -> List[str]:

    if len(sys.argv) <= 1:
        print("there is no arguments")

        exit(2)

    imgs = []

    for i in range(len(sys.argv)):
        if i <= 0:
            continue

        verify_image(sys.argv[i])
        
        imgs.append(sys.argv[i])

    return imgs

def verify_image(file_path: str) -> None:

    if not path.isfile(file_path):
        print("not a file")
        exit(1)
    
    if not is_image(file_path):
        print("not an image")
        exit(1)