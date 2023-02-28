import asyncio

from animations.figures import load_figure, Border
from curses_tools import draw_frame


async def show_gameover(canvas, border: Border):
    """
    Display GAME OVER caption

    Ключевые аргументы:
    canvas -- объект игрового поля
    border -- границы игрового поля
    """

    game_over = load_figure("game_over.txt")
    row = int((border.lower - border.upper - game_over.height) / 2)
    column = int((border.right - border.left - game_over.width) / 2)

    while True:

        draw_frame(canvas, row, column, next(game_over))
        await asyncio.sleep(0)
