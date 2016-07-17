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
from tkFileDialog import *

import os

# Constants
WINDOW_W = 800
WINDOW_H = 600
TITLE = "PowerKnowledge"
TABS = OrderedDict([("ds", "Data Collector"), ("dc", "Data Cleanser"), ("db", "Database Agent"), ("da", "Data Analysis")])
DATA_SCRAPER = "ds"
DATA_SCRAPER_NAME = "Data Collector"
DATA_CLEANSER = "dc"
DATA_CLEANSER_NAME = "Data Cleanser"
DATA_BASE = "db"
DATA_BASE_NAME = "Database Agent"
DATA_ANALAYSIS = "da"
DATA_ANALAYSIS_NAME = "Data Analysis"
RUN_EDITOR = "Run editor"
SAVE_EDITOR = "Save editor"
RUN_EXTERNAL = "Run script"
CLEAR_CONSOLE = "Clear"

# Elements dictionaries
frames = []
editors = []
terminals = []
buttonRunEditor = []
buttonSaveScript = []
buttonRunExternal = []
buttonClearTerminal = []

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

def test(frame):
	print frame
	print frame.children["editor"]

# Saves Script to a folder
def saveScript(fr):
	print fr.children["editor"].editorText
	fileOpen = asksaveasfile(mode='w', defaultextension=".dat")
	if fileOpen is None:
	    return
	textToSave = fr.nametowidget("editor").editorText
	fileOpen.write(textToSave)
	fileOpen.close() 

# Creates a Notebook and adds
def createNotebook(parent):
	notebook = Notebook(parent)
	notebook.place(relwidth = 0.98, relheight = 0.98, relx = 0.01, rely = 0.01)

	parent.update()

	global frames
	global editors
	global terminals
	global buttonRunEditor
	global buttonSaveScript
	global buttonRunExternal
	global buttonClearTerminal

	frameDS = Frame(parent, name = DATA_SCRAPER)
	frameDC = Frame(parent, name = DATA_CLEANSER)
	frameDB = Frame(parent, name = DATA_BASE)
	frameDA = Frame(parent, name = DATA_ANALAYSIS)
	
	notebook.add(frameDS, text = DATA_SCRAPER_NAME)
	notebook.add(frameDC, text = DATA_CLEANSER_NAME)
	notebook.add(frameDB, text = DATA_BASE_NAME)
	notebook.add(frameDA, text = DATA_ANALAYSIS_NAME)

	guiDS = GuiEditor(frameDS, name = "editor").place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7)
	terminalDS = ScrolledText(frameDS, name = "terminal", state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92)
	clearDS = Button(frameDS, name = "bClearTerm", text = CLEAR_CONSOLE).place(relx = 0.86, rely = 0.49)
	runEditorDS = Button(frameDS, name = "bRunEditor", text = RUN_EDITOR).place(relx = 0.79, rely = 0.43)
	saveScriptDS = Button(frameDS, name = "bSaveScript", text = SAVE_EDITOR).place(relx = 0.86, rely = 0.43)
	runExternalDS = Button(frameDS, name = "bRunExtern", text = RUN_EXTERNAL).place(relx = 0.79, rely = 0.49)	

	guiDC = GuiEditor(frameDC, name = "editor").place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7)
	terminalDC = ScrolledText(frameDC, name = "terminal", state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92)
	clearDC = Button(frameDC, name = "bClearTerm", text = CLEAR_CONSOLE).place(relx = 0.86, rely = 0.49)
	runEditorDC = Button(frameDC, name = "bRunEditor", text = RUN_EDITOR).place(relx = 0.79, rely = 0.43)
	saveScriptDC = Button(frameDC, name = "bSaveScript", text = SAVE_EDITOR).place(relx = 0.86, rely = 0.43)
	runExternalDC = Button(frameDC, name = "bRunExtern", text = RUN_EXTERNAL).place(relx = 0.79, rely = 0.49)	

	guiDB = GuiEditor(frameDB, name = "editor").place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7)
	terminalDB = ScrolledText(frameDB, name = "terminal", state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92)
	clearDB = Button(frameDB, name = "bClearTerm", text = CLEAR_CONSOLE).place(relx = 0.86, rely = 0.49)
	runEditorDB = Button(frameDB, name = "bRunEditor", text = RUN_EDITOR).place(relx = 0.79, rely = 0.43)
	saveScriptDB = Button(frameDB, name = "bSaveScript", text = SAVE_EDITOR).place(relx = 0.86, rely = 0.43)
	runExternalDB = Button(frameDB, name = "bRunExtern", text = RUN_EXTERNAL).place(relx = 0.79, rely = 0.49)	

	guiDA = GuiEditor(frameDA, name = "editor").place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7)
	terminalDA = ScrolledText(frameDA, name = "terminal", state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92)
	clearDA = Button(frameDA, name = "bClearTerm", text = CLEAR_CONSOLE).place(relx = 0.86, rely = 0.49)
	runEditorDA = Button(frameDA, name = "bRunEditor", text = RUN_EDITOR).place(relx = 0.79, rely = 0.43)
	saveScriptDA = Button(frameDA, name = "bSaveScript", text = SAVE_EDITOR).place(relx = 0.86, rely = 0.43)
	runExternalDA = Button(frameDA, name = "bRunExtern", text = RUN_EXTERNAL).place(relx = 0.79, rely = 0.49)	

	# iterator = 0
	# for key, value in TABS.items():
	# 	frames.append(Frame(parent, name = key))
	# 	notebook.add(frames[iterator], text = value)
	# 	iterator += 1
	
	# for frame in frames:
	# 	editors.append(GuiEditor(frame, name = "editor").place(relx = 0.01, rely = 0.02, relheight = 0.55, relwidth = 0.7))
	# 	terminals.append(ScrolledText(frame, name = "terminal", state = "disabled").place(relx = 0.035, rely = 0.6, relheight = 0.39, relwidth = 0.92))
	# 	buttonClearTerminal.append(Button(frame, name = "bClearTerm", text = CLEAR_CONSOLE).place(relx = 0.86, rely = 0.49))
	# 	buttonRunEditor.append(Button(frame, name = "bRunEditor", text = RUN_EDITOR).place(relx = 0.79, rely = 0.43))
	# 	buttonSaveScript.append(Button(frame, name = "bSaveScript", text = SAVE_EDITOR).place(relx = 0.86, rely = 0.43))
	# 	buttonRunExternal.append(Button(frame, name = "bRunExtern", text = RUN_EXTERNAL).place(relx = 0.79, rely = 0.49))	

	# for key, value in parent.children.items():
	# 	if key in TABS:
	# 		for btonName, button in value.children.items():
	# 			if btonName == "bSaveScript":
	# 				print value
	# 				button.config(command = lambda: test(value))

if __name__ == '__main__':
	main() 