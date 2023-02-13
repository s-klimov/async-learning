import os
import random

import curses_tools

FRAMES_FOLDER = "frames"


class Figure:
    """
    Класс фигур на игровом поле
    """

    def __init__(self, frames):
        self.__height, self.__width = curses_tools.get_frame_size(frames[0])
        self.__frames = frames

    @property
    def frames(self):
        return self.__frames

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width


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
        pos_y = random.randint(border.upper, border.lower)
        pos_x = random.randint(border.left, border.right)
        symbol = random.choice(stars)
        delay_periods = random.randint(1, 5)
        yield pos_y, pos_x, symbol, delay_periods
    