import tkinter as tk
import sys

import classes as cls
import gui
import utils

GRID = cls.Grid()
GRID.add_bombs()

window = gui.create_main_window()
flag, mine = gui.create_images()
BOARD_IN_GAME = gui.create_board(window, GRID, flag, mine)
top_frame = gui.create_top_frame(window, GRID, BOARD_IN_GAME)


tk.mainloop()
