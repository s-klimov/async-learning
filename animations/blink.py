import asyncio
import curses

from constants import TIC_TIMEOUT


def drange(start: float, stop: float, step: float):
    """
    Генератор последовательности с дробными элементами
    """
    counter = start
    while counter < stop:
        yield counter
        counter += step


async def blink(canvas, row, column, symbol="*", delay_periods=1):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in drange(0, 3, TIC_TIMEOUT):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(delay_periods):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in drange(0, 0.3, TIC_TIMEOUT):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in drange(0, 0.5, TIC_TIMEOUT):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in drange(0, 0.3, TIC_TIMEOUT):
            await asyncio.sleep(0)
