from tkinter import *   
import tkinter as tk
import tkinter.font as tkf
import time

import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os

import classes as cls
import utils
import handlers
import global_vars as g


    
# Main unresizable window ######################################################
def create_main_window():
    window = tk.Tk()
    window.title("Minesweeper Game")
    window["bg"] = "green"
    window.resizable(width=False, height=False)
    return window


# Images #######################################################################
def create_images():
    flag = tk.PhotoImage(file="images/red_flag.gif")
    mine = tk.PhotoImage(file="images/mine.gif")
    return (flag, mine) # return in main.py


# Game frame ###################################################################
def create_board(window, GRID, flag, mine):
    game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

    def create_square(i, j):
        f = tk.Frame(game_frame, height=30, width=30)
        s = tk.Button(f, borderwidth=1, state="normal", disabledforeground="#FF0000") # color number in game
        s.pack(fill=tk.BOTH, expand=True)

        # buttons bindings
        def __handler(event, x=i, y=j):
            if event.num == 1:
                handlers.left_handler(GRID, BOARD, i, j, mine)
            elif event.num == 3:
                handlers.right_handler(GRID, BOARD, i, j, flag)
            else:
                raise Exception('Invalid event code.')
        s.bind("<Button-1>", __handler)
        s.bind("<Button-3>", __handler)

        f.pack_propagate(False)
        f.grid(row=i, column=j)
        return s

    BOARD = [[create_square(i, j) for j in range(g.WIDTH)] for i in range(g.HEIGHT)]
    game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)
    
    return BOARD


# task bar (main) ####################################################################
def create_task_bar(window, grid, board):
    top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
    top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x") 
    top_frame.pack()
    for i in range(4):
        top_frame.columnconfigure(i, weight=1)

    create_bombs_counter(top_frame)
    create_new_game_button(top_frame, grid, board)
    create_setting_button(top_frame)
    create_quit_button(top_frame)
    create_time_counter(top_frame)

    return top_frame

# setting #####################################################################
AI_voices = pyttsx3.init()
voice = AI_voices.getProperty("voices")
AI_voices.setProperty("voice", voice[1].id)

def speak(voice):
    AI_voices.say(voice)
    AI_voices.runAndWait()

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
    except sr.UnknownValueError:
        # speak('Sorry sir! Can you typing in the box')
        # T = Text(root, height = 5, width = 52)
 
        # # Create label
        # l = Label(root, text = "Your order is: ")
        # l.config(font =("Courier", 14))
         
        # Fact = """You are ....."""
        # button  = Button(top,text = "quit", command = top.destroy).pack()

        query = str(input('Your idea is: '))
    return query

def create_setting_button(top_frame):

    def open():
        # top = Toplevel()
        # top.title("Voice")
        speak("Can I help you")
        while True:
            query=command().lower()
            speak("What should I search")
            url = f"https://google.com/search?q={query}"
            wb.get().open(url)
            speak(f'Here is your {query} on google')
            if "out" in query:
                speak("Goodbye. Have a good day")
                destroy()

    newgame_button = tk.Button( top_frame, bd=1, width=15, text="Setting",command=open) # button setting
    newgame_button.grid(row=0, column=2, padx=0)

# bombs #######################################################
def create_bombs_counter(top_frame):
    """ bombs_counter, left """
    bombs_counter_str = tk.StringVar()

    def update_bombs_counter():
        bombs_counter_str.set(g.BOMBS_LEFT)
        top_frame.after(100, update_bombs_counter)
    update_bombs_counter()


    bombs_counter = tk.Label( top_frame, height=1, width=4, bg='white', textvariable=bombs_counter_str, 
        font=tkf.Font(family='Lucida Console',weight='bold', size=10))
    bombs_counter.grid(row=0, column=0, padx=5, sticky=tk.W)

###############################################################
def create_new_game_button(top_frame, grid, board):
    """ new game button, middle left """
    def _start_new_game(g=grid, b=board):
        handlers.start_new_game(grid, board)

    newgame_button = tk.Button( top_frame, bd=1, width=15, text="New game",command=_start_new_game) # button New game
    newgame_button.grid(row=0, column=1, padx=0, sticky=tk.E)


def create_quit_button(top_frame):
    quit_button = tk.Button(top_frame, bd=1, width=15, text="Quit Game", command=top_frame.destroy)
    quit_button.grid(row=0, column=3, padx=0, sticky=tk.W)


# time ########################################################
def create_time_counter(top_frame):
    time_counter_str = tk.StringVar()

    def update_time_counter():
        time_counter_str.set(int((time.time() - g.INIT_TIME)//1))
        top_frame.after(100, update_time_counter);
    update_time_counter();


    time_counter = tk.Label(top_frame, height=1, width=4, bg='white', textvariable=time_counter_str,
        font=tkf.Font(family='Courier',slant='italic', size=10))
    time_counter.grid(row=0, column=4, padx=5, sticky=tk.E)

