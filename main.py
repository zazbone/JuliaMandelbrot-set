from set import *
from PIL import Image
from time import perf_counter


def save_to_png(image_array):
    image = Image.fromarray(image_array)
    image.save("out.png")


def main():
    ITER = 50  # 50 is good balance
    set_choice = input("Mandelbrot or julia ?:").lower()
    if set_choice == "julia":
        parameter = julia_param()
    else:
        parameter = mandelbrot_param()
    start = perf_counter()
    image_array = loop(parameter, set_choice, ITER)
    stop = perf_counter()
    save_to_png(image_array)
    print("Took", stop - start)


main()
