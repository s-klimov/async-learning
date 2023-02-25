import asyncio

TIC_TIMEOUT = 0.1
FRAME_THICKNESS = 1
DIRECTION_STEP = 3
FREQUENCY = 2  # В анимации корабля кадры сменяют друг друга каждые два такта.
DIFFICULTY = 8
coroutines = list()
obstacles = list()
loop = asyncio.get_event_loop()
