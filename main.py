import time
import curses

from typing import NamedTuple

from animations.blink import blink
from animations.figures import get_stars, load_figure, get_start_position
from animations.ship import animate_spaceship

from constants import TIC_TIMEOUT


class Border(NamedTuple):
    upper: int
    left: int
    lower: int
    right: int


def draw(canvas):
    canvas.border()
    rows, columns = canvas.getmaxyx()
    border = Border(1, 1, rows - 1, columns - 1)

    coroutines = [
        blink(canvas, row, column, symbol, delay_periods)
        for row, column, symbol, delay_periods in get_stars("stars.txt", border)
    ]

    ship = load_figure("rocket_frame_1.txt", "rocket_frame_2.txt")

    start_y, start_x = get_start_position(ship, border)
    ship_coro = [
        animate_spaceship(canvas, border, start_y, start_x, ship),
    ]

    # fire_coroutines = [fire(canvas, int((rows - frame_rows) / 2), int((columns - 1) / 2))]
    coroutines.extend(ship_coro)

    while True:
        for coroutine in coroutines:
            coroutine.send(None)

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == "__main__":
    curses.initscr()
    curses.update_lines_cols()
    curses.curs_set(False)
    curses.wrapper(draw)
