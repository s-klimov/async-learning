import asyncio
from itertools import repeat

from constants import DIRECTION_STEP, FREQUENCY
from curses_tools import draw_frame, read_controls


async def animate_spaceship(canvas, border, row, column, ship):

    while True:
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        row += rows_direction * DIRECTION_STEP
        column += columns_direction * DIRECTION_STEP

        row = min(border.lower - ship.height, max(row, border.upper))
        column = min(border.right - ship.width, max(column, border.left))

        frames = (x for item in ship.frames for x in repeat(item, FREQUENCY))

        for frame in frames:
            draw_frame(canvas, row, column, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, column, frame, negative=True)
