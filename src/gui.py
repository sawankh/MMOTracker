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
from collections import OrderedDict
from gui.guiEditor import *

import Pmw

# Constants
WINDOW_W = 800
WINDOW_H = 600
TITLE = "PowerKnowledge"
TABS = OrderedDict([("DS", "Data Collector"), ("DC", "Data Cleanser"), ("DB", "Database Agent"), ("DA", "Data Analysis")])
FOCUSED_TAB = "DS"

# Main method
def main():
	root = Tk()

	# Name of the Window
	root.title(TITLE)

	# Size of the Window by default
	root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
	
	# Main widgets of the app
	createNotebook(root)
	#GuiEditor(root).pack(side="top", fill="both", expand=True)
	# Run app
	root.mainloop()


# Creates a Notebook and adds
def createNotebook(parent):
	notebook = Pmw.NoteBook(parent)
	notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

	frames = {}

	for key, value in TABS.items():
		frames[key] = notebook.add(value)
		
	notebook.tab(TABS.get(FOCUSED_TAB)).focus_set()

	for key, frame in frames.items():
		GuiEditor(frame).pack(side = "top", fill = "both", expand = True)

if __name__ == '__main__':
	main() 