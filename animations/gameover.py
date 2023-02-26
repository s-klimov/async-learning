import asyncio

from animations.figures import load_figure
from curses_tools import draw_frame


async def show_gameover(canvas, border):
    """Display GAME OVER caption"""

    game_over = load_figure("game_over.txt")
    row = int((border.lower - border.upper - game_over.height ) /2)
    column = int((border.right - border.left - game_over.width) / 2)

    while True:

        draw_frame(canvas, row, column, next(game_over))
        await asyncio.sleep(0)

