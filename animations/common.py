import time

import global_vars
from animations.blink import blink
from animations.figures import Border, get_stars, load_figure, get_start_position, load_garbages
from animations.ship import animate_spaceship
from animations.space_garbage import fill_orbit_with_garbage
from constants import FRAME_THICKNESS, TIC_TIMEOUT
from global_vars import coroutines


def draw(canvas):
    """
    Основная функция проекта, которая генерирует корутины и запускает цикл событий

    Ключевые аргументы:
    canvas -- объект рабочего поля
    """
    canvas.nodelay(True)
    canvas.border()
    rows, columns = canvas.getmaxyx()
    border = Border(FRAME_THICKNESS, FRAME_THICKNESS, rows - FRAME_THICKNESS, columns - FRAME_THICKNESS)

    coroutines.extend([
        blink(canvas, row, column, symbol, delay_periods)
        for row, column, symbol, delay_periods in get_stars("stars.txt", border)
    ])

    ship = load_figure("rocket_frame_1.txt", "rocket_frame_2.txt")

    start_y, start_x = get_start_position(ship, border)
    ship_coro = animate_spaceship(canvas, border, start_y, start_x, ship)

    coroutines.append(ship_coro)

    garbages = load_garbages()

    coroutines.append(fill_orbit_with_garbage(canvas, border, garbages))

    year_timer = 0.0

    while True:

        year_timer += TIC_TIMEOUT
        if year_timer >= 1.5:
            global_vars.year += 1
            year_timer = 0

        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)
