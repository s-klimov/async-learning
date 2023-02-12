import time
import curses
import random

import itertools

from animations.stars import blink, get_stars
from animations.fire import fire
from animations.ship import animate_spaceship
from curses_tools import get_frame_size, read_controls

from constants import TIC_TIMEOUT


def draw(canvas):
    canvas.border()
    rows, columns = canvas.getmaxyx()  

    coroutines = [blink(canvas, row, column, symbol, delay_periods) for row, column, symbol, delay_periods in get_stars(rows, columns)]
    
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

