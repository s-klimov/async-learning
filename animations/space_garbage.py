import random

from constants import FREQUENCY, DIFFICULTY
from curses_tools import draw_frame
import asyncio

from constants import coroutines


async def fly_garbage(canvas, border, column, garbage, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""

    column = max(column, border.left)
    column = min(column, border.right)

    row = border.upper

    while row < border.lower:
        draw_frame(canvas, row, column, next(garbage))
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, next(garbage), negative=True)
        row += speed


async def fill_orbit_with_garbage(canvas, border, garbages):

    while True:
        coroutines.append(fly_garbage(
                canvas, border, column=random.randint(border.left, border.right), garbage=random.choice(garbages)
        ))
        for _ in range(FREQUENCY*DIFFICULTY):
            await asyncio.sleep(0)
