import asyncio
import curses

import numpy as np

from constants import TIC_TIMEOUT


async def blink(canvas, row, column, symbol="*", delay_periods=1):
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
