from PIL import Image


def parse(command):
    """
    :param command: Must be like (set_name, image_path, heightxwidth, set_arg)
    :return: set_param
    """
    command = command.split(" ")
    set_name = command[0].lower()
    image_path = command[1]
    height, width = command[2].split('x')
    if set_name == "julia":
        set_arg = complex(command[3])
    else:
        set_arg = complex()
    return image_path, int(height), int(width), set_arg


def save_to_png(image_array, path):
    image = Image.fromarray(image_array)
    image.save(path)
