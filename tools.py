import numpy as np
import os
from os import path
from PIL import Image
from typing import List 
from utils import get_imgs


def to_vector(file_path: str, height: int = 0, width: int = 0) -> np.ndarray:

    img = Image.open(file_path)

    #convert image to grey scale
    img = img.convert("L")

    #resize image
    if height > 0 and width > 0:
        img = img.resize( (width, height) )

    matrix: np.ndarray = np.array(img)

    return matrix

def split_images(matrix: np.ndarray, vertical: int, horizontal: int) -> List[np.ndarray]:
    
    height, width = matrix.shape

    h_delta = height/horizontal
    w_delta = width/vertical

    matrices = []

    for i in range(horizontal):
        h_start = round( i * h_delta )
        h_end = round( (i + 1) * h_delta )

        for j in range(vertical):
            w_start = round( j * w_delta )
            w_end = round( (j + 1) * w_delta )

            matrices.append(matrix[h_start:h_end, w_start:w_end])
    
    return matrices

def split_and_save_main_img(img_path: str):

    matrices = split_images(to_vector(img_path), 1, 3)

    i = 0

    for M in matrices:
        
        img = Image.fromarray()

        img.show()

        img_path = path.join(path.abspath(os.curdir), "main/imgs/part_{0}.png".format(i))

        i += 1

        img.save(fp=img_path, format="PNG")