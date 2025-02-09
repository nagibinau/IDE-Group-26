from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    """
    Start of image processing

    :param image: np.array
    :param size: int
    :param gradation_step: int
    :return: np.array
    """

    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    """
    Returns the average brightness in the image block

    :param block:
    :param size:
    :param gradation_step:
    :return: float

    >>> get_average_brightness(4, 4, 6)
    55.0

    >>> get_average_brightness(2, 2, 2)
    57.0

    >>> get_average_brightness(0, 0, 2)
    57.0

    >>> get_average_brightness(2, 2, -1)
    0.0
    """
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    block_size = int(input("Введите размер блока: "))
    gradations_count = int(input("Введите количество градаций серого: "))
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save(input("Введите имя файла, в которой хотите сохранить результат: "))


if __name__ == '__main__':
    main()
