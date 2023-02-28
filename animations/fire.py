import asyncio
import curses

from animations.figures import Border
from animations.obstacles import has_collision
from global_vars import obstacles, obstacles_in_last_collisions


async def fire(canvas, border: Border, start_row: float, start_column: float, rows_speed: float = -0.3, columns_speed: float = 0.0):
    """
    Display animation of gun shot, direction and speed can be specified.

    Ключевые аргументы:
    canvas -- объект игрового поля
    border -- границы игрового поля
    start_row -- начальная горизонтальная координата выстрела
    start_column -- начальная вертикальная координата выстрела
    rows_speed -- вертикальная скорость движения выстрела
    columns_speed -- горизонтальная скорость движения выстрела
    """

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), "*")
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), "O")
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), " ")

    row += rows_speed
    column += columns_speed

    symbol = "-" if columns_speed else "|"

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while border.upper < row < max_row and border.left < column < max_column:

        for obstacle in obstacles:
            if has_collision(
                    (obstacle.row, obstacle.column),
                    (obstacle.rows_size, obstacle.columns_size),
                    (row, column)
            ):
                obstacles_in_last_collisions.append(obstacle)
                return

        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), " ")
        row += rows_speed
        column += columns_speed
