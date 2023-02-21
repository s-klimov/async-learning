import time
import curses

from typing import NamedTuple

from animations.blink import blink
from animations.figures import get_stars, load_figure, get_start_position
from animations.ship import animate_spaceship
from animations.space_garbage import fly_garbage

from constants import TIC_TIMEOUT, FRAME_THICKNESS


class Border(NamedTuple):
    upper: int
    left: int
    lower: int
    right: int


def draw(canvas):
    canvas.nodelay(True)
    canvas.border()
    rows, columns = canvas.getmaxyx()
    border = Border(FRAME_THICKNESS, FRAME_THICKNESS, rows - FRAME_THICKNESS, columns - FRAME_THICKNESS)

    coroutines = [
        blink(canvas, row, column, symbol, delay_periods)
        for row, column, symbol, delay_periods in get_stars("stars.txt", border)
    ]

    ship = load_figure("rocket_frame_1.txt", "rocket_frame_2.txt")

    start_y, start_x = get_start_position(ship, border)
    ship_coro = animate_spaceship(canvas, border, start_y, start_x, ship)

    coroutines.append(ship_coro)

    #
    garbage_duck = load_figure("duck.txt")
    garbage_hubble = load_figure("hubble.txt")
    garbage_lamp = load_figure("lamp.txt")
    coroutines.extend([
    fly_garbage(canvas, border, column=10, garbage=garbage_duck),
    fly_garbage(canvas, border, column=20, garbage=garbage_hubble),
    fly_garbage(canvas, border, column=80, garbage=garbage_lamp),
    ])

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        if len(coroutines) == 0:
            break

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == "__main__":
    curses.initscr()
    curses.update_lines_cols()
    curses.curs_set(False)
    curses.wrapper(draw)
