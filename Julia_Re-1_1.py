import os
from time import perf_counter

from core import fractal
from core import util


ITER = 50  # 50 is good balance
IMAGE_NB = 200


start = perf_counter()
argv = "julia image/Julia_Re-1_1.png 720x480 -0.8+0.156j"
image_path, height, width, set_arg = util.parse(argv)
image_array = fractal.loop(width, height, set_arg, ITER)
util.save_to_png(image_array, image_path)

os.mkdir("tmp")
for i in range(IMAGE_NB):
    re = i / (IMAGE_NB * 2) - 1
    print(f"Set number {i}/{IMAGE_NB}")
    argv = f"julia tmp/{i:03}.png 720x480 {re}+0.156j"
    image_path, height, width, set_arg = util.parse(argv)
    start = perf_counter()
    image_array = fractal.loop(width, height, set_arg, ITER)
    stop = perf_counter()
    util.save_to_png(image_array, image_path)
    print("Took: ", stop - start)
stop = perf_counter()
print("Took at least: ", stop - start)
os.chdir("tmp")
os.system("ffmpeg -framerate 30 -i %03d.png ../movie/example1.gif")
for i in range(IMAGE_NB):
    os.remove(f"{i:03}.png")
os.chdir("..")
os.rmdir("tmp")
