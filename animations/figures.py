import curses_tools


class Figure:
    """
    Класс фигур на игровом поле
    """

    def __init__(self, *frames):
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
