import random

import global_vars

from animations.explosion import explode
from animations.figures import Border, Figure
from animations.game_scenario import get_garbage_delay_tics, show_year
from animations.obstacles import Obstacle, show_obstacles
from curses_tools import draw_frame
import asyncio

from global_vars import coroutines, obstacles, obstacles_in_last_collisions


async def fly_garbage(canvas, border: Border, column: int, garbage: Figure, speed=0.5):
    """
    Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start.

    Ключевые аргументы:
    canvas -- объект игрового поля
    border -- границы игрового поля
    column -- горизонтальная координата начала движения мусора вниз
    garbage -- фигура мусора
    speed -- скорость движения мусора
    """
    column = max(column, border.left)
    column = min(column, border.right)

    row = border.upper

    while row < border.lower:
        obstacle = Obstacle(row, column, garbage.height, garbage.width, uid='мусор')

        draw_frame(canvas, row, column, next(garbage))
        obstacles.append(obstacle)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, next(garbage), negative=True)

        destroyed = obstacle in obstacles_in_last_collisions
        obstacles.remove(obstacle)
        if destroyed:
            coroutines.append(explode(canvas, row+garbage.height/2, column+garbage.width/2))
            obstacles_in_last_collisions.remove(obstacle)
            break

        row += speed


async def fill_orbit_with_garbage(canvas, border: Border, garbages: list):
    """
    Заполняет игровое поле мусором.

    Ключевые аргументы:
    canvas -- объект игрового поля
    border -- границы игрового поля
    garbages -- список фигур мусора
    """

    while True:

        coroutines.append(show_year(canvas, border))

        if get_garbage_delay_tics(global_vars.year) is None:
            await asyncio.sleep(0)
            continue

        coroutines.append(fly_garbage(
                canvas, border, column=random.randint(border.left, border.right), garbage=random.choice(garbages)
        ))
        coroutines.append(show_obstacles(
                canvas, obstacles
        ))

        for _ in range(get_garbage_delay_tics(global_vars.year)):
            await asyncio.sleep(0)
