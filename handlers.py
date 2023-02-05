import tkinter as tk
from tkinter import messagebox
import sys
import time
import global_vars as g
import utils


# Event handlers ###############################################################
def left_handler(grid, board, i, j, mine):
    if board[i][j]["image"] == "" and not grid.tab[i][j].revealed:
        board[i][j]["state"] = "disabled"
        board[i][j]["relief"] = tk.SUNKEN

        if grid.tab[i][j].is_bomb:
            board[i][j]["image"] = mine
            board[i][j]["state"] = "normal"
            end_game(False, grid, board)
        else:
            grid.tab[i][j].revealed = True
            g.SQUARES_REVEALED += 1

            if grid.tab[i][j].bombs_around != 0:
                board[i][j]["text"] = grid.tab[i][j].bombs_around
            else:
                for (x, y) in utils.neighbours(i, j):
                    left_handler(grid, board, x, y, mine)

            if g.SQUARES_REVEALED == (g.WIDTH * g.HEIGHT - g.BOMBS):
                end_game(True, grid, board)


def right_handler(grid, board, i, j, flag):
    if not grid.tab[i][j].revealed:
        if board[i][j]["image"] == "":
            board[i][j]["image"] = flag
            board[i][j]["state"] = "normal"
            g.BOMBS_LEFT -= 1
        else:
            board[i][j]["state"] = "disabled"
            board[i][j]["image"] = ""
            g.BOMBS_LEFT += 1

#####################################################
def end_game(win, grid, board):
    if win:
        title = "- YOU WIN -"
        msg = "CONGRATULATION !!. Play again?"
    else:
        title = "- YOU LOST -"
        msg = "AGAIN!"
    ans = messagebox.askyesno(title, msg)
    if ans == 1:
        start_new_game(grid, board)
    else:
        sys.exit()


def start_new_game(grid, board):
    for x in range(g.HEIGHT):
        for y in range(g.WIDTH):
            grid.tab[x][y].reset()
            board[x][y]["image"] = ""
            board[x][y]["text"] = ""
            board[x][y]["state"] = tk.DISABLED
            board[x][y]["relief"] = tk.RAISED
    grid.add_bombs()
    g.SQUARES_REVEALED = 0
    g.BOMBS_LEFT = g.BOMBS
    g.INIT_TIME = time.time()

