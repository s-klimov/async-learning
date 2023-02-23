import asyncio

from animations.physics import update_speed
from curses_tools import draw_frame, read_controls


async def animate_spaceship(canvas, border, row, column, ship):
    row_speed, column_speed = 0, 0

    while True:
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        row_speed, column_speed = update_speed(row_speed, column_speed, rows_direction, columns_direction, 3, 3)

        row += row_speed
        column += column_speed

        row = min(border.lower - ship.height, max(row, border.upper))
        column = min(border.right - ship.width, max(column, border.left))

        for frame in ship.frames:
            draw_frame(canvas, row, column, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, column, frame, negative=True)
