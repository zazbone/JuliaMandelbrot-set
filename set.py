import numpy as np


def julia(z, c, ITER):
    for i in range(ITER):
        z = z ** 2 + c
        if abs(z) > 4:
            return [i * 5] * 3
    return [0] * 3


def mandelbrot(c, ITER):
    z = complex(0, 0)
    for i in range(ITER):
        z = z ** 2 + c
        if abs(z) > 4:
            return [i * 5] * 3
    return [0] * 3


def julia_param():
    height, width = input("Give image resolution (HEIGHTxWIDTH):").lower().split('x')
    height, width = int(height), int(width)
    re, im = input("c value (RExIM):").lower().split('x')
    re, im = float(re), float(im)
    c = complex(re, im)
    return height, width, c


def mandelbrot_param():
    height, width = input("Give image resolution (HEIGHTxWIDTH):").lower().split('x')
    height, width = int(height), int(width)
    return width, height


def loop(parameter, set_choice, ITER):
    image_array = np.zeros(shape=(parameter[0], parameter[1], 3), dtype=np.uint8)
    w_size = (-1, 1)
    h_size = (-2, 1)
    avoid_alloc = np.linspace(h_size[0], h_size[1], num=parameter[1])
    for i, w in enumerate(np.linspace(w_size[0], w_size[1], num=parameter[0])):
        for j, h in enumerate(avoid_alloc):
            if set_choice == "julia":
                image_array[i][j] = julia(complex(h, w), parameter[2], ITER)
            else:
                image_array[i][j] = mandelbrot(complex(h, w), ITER)
    return image_array