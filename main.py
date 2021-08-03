from PIL import Image
from skimage.metrics import mean_squared_error as mse
from utils import get_imgs
from tools import to_vector, split_images

def compare_imgs():

    imgs = get_imgs()

    img_A = to_vector(imgs[0])
    img_B = to_vector(imgs[1])

    matrices = split_images(img_A, 1, 3)

    count = 0
    min_mse = None
    index = None

    for M in matrices:

        if img_B.shape != M.shape:
            img_B = to_vector(imgs[1], M.shape[0], M.shape[1])
        
        res = mse(M, img_B)
        
        if min_mse == None or res < min_mse:
            min_mse = res
            index = count

        count += 1

    if index == 0:
        print("EYES")
    elif index == 1:
        print("NOSE")
    else:
        print("MOUTH")

    Image.fromarray(matrices[index]).show()


if __name__ == "__main__":
    compare_imgs()
