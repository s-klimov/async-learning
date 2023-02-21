import itertools
import os
import random

import curses_tools
from constants import FREQUENCY

FRAMES_FOLDER = "frames"


class Figure:
    """
    Класс фигур на игровом поле
    """

    def __init__(self, frames):
        self.__height, self.__width = curses_tools.get_frame_size(frames[0])
        self.__frames = [x for item in frames for x in itertools.repeat(item, FREQUENCY)]
        self.__iterator = itertools.cycle(self.__frames)

    @property
    def frames(self):
        return self.__frames

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    def __next__(self):
        return next(self.__iterator)



def get_start_position(figure, border):
    return (
        int((border.lower - figure.height) / 2) + border.upper,
        int((border.right - figure.width) / 2) + border.left,
    )


def load_figure(*paths):
    """
    Загрузка фигуры из файлов
    """

    frames = list()

    for path in paths:
        with open(os.path.join(FRAMES_FOLDER, path)) as file:
            frames.append(file.read())

    return Figure(frames)


def get_stars(path: str, border, count=50):
    """
    Формирование списка звёзд
    """

    with open(os.path.join(FRAMES_FOLDER, path)) as file:
        stars = file.read()

    for _ in range(count):
        pos_y = random.randint(border.upper, border.lower - 1)
        pos_x = random.randint(border.left, border.right - 1)
        symbol = random.choice(stars)
        delay_periods = random.randint(1, 5)
        yield pos_y, pos_x, symbol, delay_periods
