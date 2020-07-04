import numpy as np


def set(z, c, ITER):
    for i in range(ITER):
        z = z ** 2 + c
        if abs(z) > 4:
            return [i * 5] * 3
    return [0] * 3


def loop(width, height, c,  ITER):
    image_array = np.zeros(shape=(width, height, 3), dtype=np.uint8)
    w_size = (-1, 1)
    h_size = (-2, 2)
    avoid_alloc = np.linspace(h_size[0], h_size[1], num=height)
    for i, w in enumerate(np.linspace(w_size[0], w_size[1], num=width)):
        for j, h in enumerate(avoid_alloc):
            image_array[i][j] = set(complex(h, w), c, ITER)
    return image_array
