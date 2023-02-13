import time
import curses
import random

import itertools

from typing import NamedTuple

from animations.stars import blink
from animations.figures import get_stars, load_figure
from animations.fire import fire
from animations.ship import animate_spaceship
from curses_tools import get_frame_size, read_controls

from constants import TIC_TIMEOUT

class Border(NamedTuple):
    upper: int
    left: int
    lower: int
    right: int


def draw(canvas):
    canvas.border()
    rows, columns = canvas.getmaxyx()
    border = Border(1, 1, rows-2, columns-2)

    coroutines = [blink(canvas, row, column, symbol, delay_periods) for row, column, symbol, delay_periods in get_stars("stars.txt", border)]
    
    ship = load_figure("rocket_frame_1.txt", "rocket_frame_2.txt")

    with open('frames/rocket_frame_1.txt') as fh1, open('frames/rocket_frame_2.txt') as fh2:
        frame1 = fh1.read()
        frame2 = fh2.read()
    
    frame_rows, frame_colums = get_frame_size(frame1)

    ship_coro = [
        animate_spaceship(canvas, int((rows - frame_rows) / 2), int((columns - frame_colums) / 2), [frame1, frame2]),
    ]

    # fire_coroutines = [fire(canvas, int((rows - frame_rows) / 2), int((columns - 1) / 2))]
    coroutines.extend(ship_coro)

    while True:
        for coroutine in coroutines:

            coroutine.send(None)


        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.initscr()
    curses.update_lines_cols()
    curses.curs_set(False)
    curses.wrapper(draw)

