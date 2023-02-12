import asyncio

from curses_tools import draw_frame, read_controls, get_frame_size
import numpy as np

from constants import TIC_TIMEOUT

DIRECTION_STEP = 3

async def animate_spaceship(canvas, row, column, frames):
    canvas.nodelay(True)
    max_row, max_column = canvas.getmaxyx()
    frame_rows, frame_columns = get_frame_size(frames[0])
    
    while True:

        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        row += rows_direction * DIRECTION_STEP
        column += columns_direction * DIRECTION_STEP

        if row < 1:
            row = 1
        elif row + frame_rows > max_row - 1:
            row = max_row - frame_rows - 1

        if column < 1:
            column = 1
        elif column + frame_columns > max_column - 1:
            column = max_column - frame_columns - 1

        for frame in frames:            
            draw_frame(canvas, row, column, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, column, frame, negative=True)
