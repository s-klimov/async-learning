import asyncio

from curses_tools import draw_frame, read_controls


DIRECTION_STEP = 3


async def animate_spaceship(canvas, border, row, column, ship):
    canvas.nodelay(True)

    while True:
        rows_direction, columns_direction, space_pressed = read_controls(canvas)
        row += rows_direction * DIRECTION_STEP
        column += columns_direction * DIRECTION_STEP

        if row <= border.upper:
            row = border.upper
        elif row + ship.height >= border.lower:
            row = border.lower - ship.height

        if column <= border.left:
            column = border.left
        elif column + ship.width >= border.right:
            column = border.right - ship.width

        for frame in ship.frames:
            draw_frame(canvas, row, column, frame)
            await asyncio.sleep(0)
            draw_frame(canvas, row, column, frame, negative=True)
