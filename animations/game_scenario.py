import asyncio

import global_vars
from animations.figures import Border

PHRASES = {
    # Только на английском, Repl.it ломается на кириллице
    1957: "First Sputnik",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
}


def get_garbage_delay_tics(year: int):
    """
    В зависимости от года, уменьшает интервалы между появлением нового мусора.
    Чем дальше в будущее, тем быстрее появляется новый мусор

    Ключевые аргументы:
    year -- год
    """

    if year < 1961:
        return None
    elif year < 1969:
        return 20
    elif year < 1981:
        return 14
    elif year < 1995:
        return 10
    elif year < 2010:
        return 8
    elif year < 2020:
        return 6
    else:
        return 2


async def show_year(canvas, border: Border):
    """
    Display YEAR value

    Ключевые аргументы:
    canvas -- объект игрового поля
    border -- границы игрового поля
    """

    year = str(global_vars.year)
    row = border.lower - 1
    column = border.right - len(year) - 1

    while True:
        # NOTE не получилось использовать canvas.derwin
        canvas.addstr(row, column, year)
        await asyncio.sleep(0)
