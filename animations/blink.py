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
    """
    Корутина мерцающей звезды
    canvas: объект экрана
    row: положение звезды по вертикали
    column: положение звезды по горизонтали
    symbol: символ, обозначающий звезду
    delay_periods: время ожидания до вспышки звезды в секундах. На вход ожидается рандомное число.
    """

    async def sleep(tics: float = 1.0):
        for _ in drange(0, tics, TIC_TIMEOUT):
            await asyncio.sleep(0)

    while True:

        # создаем звезду
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await sleep(delay_periods * TIC_TIMEOUT)

        # выжидаем рандомное время перед тем как она вспыхнет
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await sleep(delay_periods * TIC_TIMEOUT)

        # звезда мерцает
        canvas.addstr(row, column, symbol)
        await sleep(0.3)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await sleep(0.5)

        canvas.addstr(row, column, symbol)
        await sleep(0.3)
