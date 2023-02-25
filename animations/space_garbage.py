import random

from animations.obstacles import Obstacle, show_obstacles
from constants import FREQUENCY, DIFFICULTY, obstacles, loop
from curses_tools import draw_frame
import asyncio

from constants import coroutines


async def fly_garbage(canvas, border, column, garbage, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""

    column = max(column, border.left)
    column = min(column, border.right)

    row = border.upper

    while row < border.lower:
        obstacle = Obstacle(row, column, garbage.height, garbage.width, uid='мусор')

        draw_frame(canvas, row, column, next(garbage))
        obstacles.append(obstacle)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, next(garbage), negative=True)
        obstacles.remove(obstacle)

        row += speed


async def fill_orbit_with_garbage(canvas, border, garbages):

    while True:
        coroutines.append(fly_garbage(
                canvas, border, column=random.randint(border.left, border.right), garbage=random.choice(garbages)
        ))
        coroutines.append(show_obstacles(
                canvas, obstacles
        ))
        for _ in range(FREQUENCY*DIFFICULTY):
            await asyncio.sleep(0)
