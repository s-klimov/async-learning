import asyncio
import curses
import random

import numpy as np

from constants import TIC_TIMEOUT, STARS


def get_stars(rows, columns, count=50):
    for _ in range(count):
        pos_y = random.randint(1, rows-2)
        pos_x = random.randint(1, columns-2)
        symbol = random.choice(STARS)
        delay_periods = random.randint(1, 10)
        yield pos_y, pos_x, symbol, delay_periods


async def blink(canvas, row, column, symbol='*', delay_periods=1):

    while True:

        for _ in np.arange(0, 3, TIC_TIMEOUT):
            canvas.addstr(row, column, symbol, curses.A_DIM)
            await asyncio.sleep(0)

        for _ in range(delay_periods):
            canvas.addstr(row, column, symbol, curses.A_DIM)
            await asyncio.sleep(0)

        for _ in np.arange(0, 0.3, TIC_TIMEOUT):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)
        
        for _ in np.arange(0, 0.5, TIC_TIMEOUT):
            canvas.addstr(row, column, symbol, curses.A_BOLD)
            await asyncio.sleep(0)

        for _ in np.arange(0, 0.3, TIC_TIMEOUT):
            canvas.addstr(row, column, symbol)
            await asyncio.sleep(0)

