#!/usr/bin/python
# Title: gui.py
# Description: Implementation of the graphical interface of powerknowledge system, using Tkinter
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-12
# Version: 0.1
# Usage: python gui.py
# Notes: 
# python_version: 2.6.6
# License: Copyright 200X Sawan J. Kapai Harpalani 
# This file is part of MMOTracker. MMOTracker is free software: you can redistribute it  and/or modify 
# it under the terms of the GNU GeneralPublic License as published by the Free Software  Foundation, 
# either version 3 of the License,  or (at your option) any later version 
# MMOTracker is distributed in the hope that it willbe useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESSFOR A PARTICULAR PURPOSE. See the GNU General 
# PubliLicense for more details.You should have received a copy of the GNU GeneralPublic License along with MMOTracker. 
# If not, seehttp://www.gnu.org/licenses/.
#==============================================================================

from Tkinter import *
from ttk import *
from collections import OrderedDict
from gui.guiEditor import *
from ScrolledText import ScrolledText

import os

# Constants
WINDOW_W = 800
WINDOW_H = 600
TITLE = "PowerKnowledge"
TABS = OrderedDict([("DS", "Data Collector"), ("DC", "Data Cleanser"), ("DB", "Database Agent"), ("DA", "Data Analysis")])
FOCUSED_TAB = "DS"
RUN_EDITOR = "Run editor"
SAVE_EDITOR = "Save editor"
RUN_EXTERNAL = "Run script"

# Main method
def main():
	root = Tk()
	root.state('zoomed')

	# Name of the Window
	root.title(TITLE)

	# Size of the Window by default
	root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
	root.update()

	# Main widgets of the app
	createNotebook(root)
	
	# Run app
	root.mainloop()


# Creates a Notebook and adds
def createNotebook(parent):
	notebook = Notebook(parent)
	notebook.place(relwidth = 0.98, relheight = 0.98, relx = 0.01, rely = 0.01)

	parent.update()

	frames = {}
	editors = {}
	terminals = {}
	buttonRunEditor = {}
	buttonSaveScript = {}
	buttonRunExternal = {}

	for key, value in TABS.items():
		frames[key] = Frame(parent)
		notebook.add(frames[key], text = value)
	
	for key, frame in frames.items():
		editors[key] = GuiEditor(frame).place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7)
		terminals[key] = ScrolledText(frame, state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92)
		buttonRunEditor[key] = Button(frame, text = RUN_EDITOR).place(relx = 0.81, rely = 0.37)
		buttonSaveScript[key] = Button(frame, text = SAVE_EDITOR).place(relx = 0.81, rely = 0.43)
		buttonRunExternal[key] = Button(frame, text = RUN_EXTERNAL).place(relx = 0.81, rely = 0.49)

if __name__ == '__main__':
	main() 