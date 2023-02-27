import time
import curses

from typing import NamedTuple

import constants
from animations.blink import blink
from animations.figures import get_stars, load_figure, get_start_position
from animations.ship import animate_spaceship
from animations.space_garbage import fill_orbit_with_garbage

from constants import TIC_TIMEOUT, FRAME_THICKNESS, coroutines


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

    coroutines.extend([
        blink(canvas, row, column, symbol, delay_periods)
        for row, column, symbol, delay_periods in get_stars("stars.txt", border)
    ])

    ship = load_figure("rocket_frame_1.txt", "rocket_frame_2.txt")

    start_y, start_x = get_start_position(ship, border)
    ship_coro = animate_spaceship(canvas, border, start_y, start_x, ship)

    coroutines.append(ship_coro)

    garbages = [
        load_figure("duck.txt"),
        load_figure("hubble.txt"),
        load_figure("lamp.txt"),
        load_figure("trash_large.txt"),
        load_figure("trash_small.txt"),
        load_figure("trash_xl.txt"),
    ]

    coroutines.append(fill_orbit_with_garbage(canvas, border, garbages))

    year_timer = 0.0

    while True:

        year_timer += TIC_TIMEOUT
        if year_timer >= 1.5:
            constants.year += 1
            year_timer = 0

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
