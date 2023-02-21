from curses_tools import draw_frame
import asyncio

async def fly_garbage(canvas, border, column, garbage, speed=0.5):
    """Animate garbage, flying from top to bottom. Сolumn position will stay same, as specified on start."""
    rows_number, columns_number = canvas.getmaxyx()

    column = max(column, border.left)
    column = min(column, border.right)

    row = border.upper

    while row < border.lower:
        draw_frame(canvas, row, column, next(garbage))
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, next(garbage), negative=True)
        row += speed
