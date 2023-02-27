import curses

from animations.common import draw

if __name__ == "__main__":
    curses.initscr()
    curses.update_lines_cols()
    curses.curs_set(False)
    curses.wrapper(draw)
