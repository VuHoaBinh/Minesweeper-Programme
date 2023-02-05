from tkinter import *
import tkinter as tk
import sys

import pyttsx3
import datetime

import classes as cls
import gui
import utils


# Set AI voice ######################################################
AI_voices = pyttsx3.init()
voice = AI_voices.getProperty("voices")
AI_voices.setProperty("voice", voice[1].id)

def speak(voice):
	AI_voices.say(voice)
	AI_voices.runAndWait()

def welcome():
	# pass
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour<12:
		speak("Good Morning !")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	elif hour>=18 and hour<24:
		speak("Good Evening")
	speak("Welcome to Minesweeper") 
welcome()

# Initialisation of the data ###################################################
GRID = cls.Grid()
GRID.add_bombs()

# Creation of the GUI ##########################################################
window = gui.create_main_window()
flag, mine = gui.create_images()
BOARD_IN_GAME = gui.create_board(window, GRID, flag, mine)
top_frame = gui.create_task_bar(window, GRID, BOARD_IN_GAME)



tk.mainloop()
