import itertools
import random
from os import listdir
from os.path import isfile, join as join_path
from typing import NamedTuple

import curses_tools
from constants import FREQUENCY

FRAMES_FOLDER = "frames"
GARBAGE_SUBFOLDER = "garbage"


class Figure:
    """
    Класс фигур на игровом поле
    """

    def __init__(self, frames):
        """
        Конструктор класса.

        Ключевые аргументы:
        frames -- кадры анимации фигуры

        Создает атрибуты высоты и ширины фигуры __height, __width
        __frames - каждый кадр анимации дублируется в зависимости от параметра FREQUENCY проекта
        __cycle - бесконечный генератор по списку __frames
        """
        self.__height, self.__width = curses_tools.get_frame_size(frames[0])
        self.__frames = [x for item in frames for x in itertools.repeat(item, FREQUENCY)]
        self.__cycle = itertools.cycle(self.__frames)

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
        return next(self.__cycle)


class Border(NamedTuple):
    upper: int
    left: int
    lower: int
    right: int


def get_start_position(figure: Figure, border: Border) -> (int, int):
    """
    Функция расчета левых верхних координат для размещения фигуры в центре поля

    Ключевые аргументы:
    figure -- фигура
    border -- границы игрового поля
    """
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
        with open(join_path(FRAMES_FOLDER, path)) as file:
            frames.append(file.read())

    return Figure(frames)


def load_garbages() -> list:
    """
    Получение фреймов мусора из всех текстовых файлов в папке GARBAGE_FOLDER
    """
    return [load_figure(join_path(GARBAGE_SUBFOLDER, f)) for f in listdir(join_path(FRAMES_FOLDER, GARBAGE_SUBFOLDER))
            if isfile(join_path(FRAMES_FOLDER, GARBAGE_SUBFOLDER, f)) and f.endswith(".txt")]


def get_stars(path: str, border, count=50):
    """
    Формирование списка звёзд
    """

    with open(join_path(FRAMES_FOLDER, path)) as file:
        stars = file.read()

    for _ in range(count):
        pos_y = random.randint(border.upper, border.lower - 1)
        pos_x = random.randint(border.left, border.right - 1)
        symbol = random.choice(stars)
        delay_periods = random.randint(1, 5)
        yield pos_y, pos_x, symbol, delay_periods
