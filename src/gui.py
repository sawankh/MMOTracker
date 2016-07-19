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
import tkMessageBox
from ttk import *
from collections import OrderedDict
from gui.guiEditor import *
from ScrolledText import ScrolledText
from tkFileDialog import *
from StringIO import StringIO
from PIL import ImageTk, Image

import os, subprocess, threading, time

# Constants
WINDOW_W = 1366
WINDOW_H = 768
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
SCRAPE_URL = "Scrape URL"
SCRAPE_STRING = "Scrape String"
REMOVE_COLUMNS = "Remove Columns"
REMOVE_LINE = "Remove Lines"
APPEND_FILE = "Append Files"
INSERT_CSV = "Insert CSV"
INSERT_JSON = "Insert JSON"
EXECUTE_PYTHON = "Execute Python"
EXECUTE_R = "Execute R"
EXECUTE_MATLAB = "Execute Matlab"
SEPARATOR = "==============================================================================\n"

# Main method
def main():
	root = Tk()
	root.state('normal')

	# Name of the Window
	root.title(TITLE)

	# Size of the Window by default
	root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
	root.update()
	root.resizable(0,0)
	
	# Main widgets of the app
	createNotebook(root)
	
	# Run app
	root.mainloop()



# Saves Script to a folder
def saveScript(fr):
	def task():
		fileOpen = asksaveasfile(mode='w', defaultextension=".dat")
		if fileOpen is None:
		    return
		textToSave = fr
		fileOpen.write(textToSave)
		fileOpen.close() 
	t = threading.Thread(target = task)
	t.start()

# Runs the editor
def runEditor(string, typeAgent, terminal):
	def task():
		terminal.config(state = "normal")
		terminal.insert(INSERT, SEPARATOR)
		startT = time.time()
		startTime = time.localtime(startT)
		terminal.insert(INSERT, "Execution started at ---> " + time.asctime(startTime) + "\n")
		terminal.insert(INSERT, SEPARATOR)
		terminal.config(state = "disabled")
		f = open(typeAgent + ".dat",'w')
		f.write(string)
		f.close()
		process = None
		if typeAgent == DATA_SCRAPER: 
			subProcess = "python dataScraper/DSAgent.py -c " + typeAgent + ".dat"
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_CLEANSER:
			subProcess = "python dataCleanser/DCAgent.py -c " + typeAgent + ".dat"
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_BASE:
			subProcess = "python dbAgent/DBAgent.py -c " + typeAgent + ".dat"
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_ANALAYSIS:
			subProcess = "python dataAnalysis/DAAgent.py -c " + typeAgent + ".dat"
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		if not output:
			output = "There might be an error in your syntax, please check it carefully.\n"
		terminal.config(state = "normal")
		terminal.insert(INSERT, output)
		terminal.insert(INSERT, SEPARATOR)
		endT = time.time()
		endTime = time.localtime(endT)
		terminal.insert(INSERT, "Execution finished at ---> " + time.asctime(endTime) + "\n")
		elapsed = endT - startT
		terminal.insert(INSERT, "Time elapsed ---> " + time.strftime("%H hours %M minutes and %S seconds", time.gmtime(elapsed)) + "\n")
		terminal.insert(INSERT, SEPARATOR)
		terminal.config(state = "disabled")
		os.remove(typeAgent + ".dat")
	t = threading.Thread(target = task)
	t.start()


# Clears the terminal
def clearTerminal(terminal):
	def task():
		terminal.config(state = "normal")
		terminal.delete('1.0', END)
		terminal.config(state = "disabled")
	t = threading.Thread(target = task)
	t.start()

# Runs external Script
def runExternal(typeAgent, terminal):
	def task():
		fileName = askopenfilename(filetypes = (("PowerKnowledge files", "*.dat"), ("All files", "*.*")))
		terminal.config(state = "normal")
		terminal.insert(INSERT, SEPARATOR)
		startT = time.time()
		startTime = time.localtime(startT)
		terminal.insert(INSERT, "Execution started at ---> " + time.asctime(startTime) + "\n")
		terminal.insert(INSERT, SEPARATOR)
		terminal.config(state = "disabled")
		process = None
		if typeAgent == DATA_SCRAPER: 
			subProcess = "python dataScraper/DSAgent.py -c " + fileName
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_CLEANSER:
			subProcess = "python dataCleanser/DCAgent.py -c " + fileName
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_BASE:
			subProcess = "python dbAgent/DBAgent.py -c " + fileName
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		elif typeAgent == DATA_ANALAYSIS:
			subProcess = "python dataAnalysis/DAAgent.py -c " + fileName
			process = subprocess.Popen(subProcess, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
			output, errors = process.communicate()
		if not output:
			output = "There might be an error in your syntax, please check it carefully."
		terminal.config(state = "normal")
		terminal.insert(INSERT, output)
		terminal.insert(INSERT, errors)
		terminal.insert(INSERT, SEPARATOR)
		endT = time.time()
		endTime = time.localtime(endT)
		terminal.insert(INSERT, "Execution finished at ---> " + time.asctime(endTime) + "\n")
		elapsed = endT - startT
		terminal.insert(INSERT, "Time elapsed ---> " + time.strftime("%H hours %M minutes and %S seconds", time.gmtime(elapsed)) + "\n")
		terminal.insert(INSERT, SEPARATOR)
		terminal.config(state = "disabled")
	t = threading.Thread(target = task)
	t.start()

# Shows basic information about the application
def showInfo(event):
	tkMessageBox.showinfo(title = 'Information', message = ' Button pressed! ')

# Creates a Notebook and adds
def createNotebook(parent):
	notebook = Notebook(parent)
	notebook.place(relwidth = 0.98, relheight = 0.98, relx = 0.01, rely = 0.01)

	parent.update()

	frameDS = Frame(parent, name = DATA_SCRAPER)
	frameDC = Frame(parent, name = DATA_CLEANSER)
	frameDB = Frame(parent, name = DATA_BASE)
	frameDA = Frame(parent, name = DATA_ANALAYSIS)
	
	notebook.add(frameDS, text = DATA_SCRAPER_NAME)
	notebook.add(frameDC, text = DATA_CLEANSER_NAME)
	notebook.add(frameDB, text = DATA_BASE_NAME)
	notebook.add(frameDA, text = DATA_ANALAYSIS_NAME)

	iOpen = Image.open("resources/pwlogo.png").resize((247, 192), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(iOpen)
	panel = Label(parent, image = img, cursor = "hand2")
	panel.bind('<Button-1>', showInfo)
	panel.image = img
	panel.place(relx = 0.76, rely = 0.05, relheight = 0.25, relwidth = 0.182)

	labelFrameGUIDS = LabelFrame(frameDS, name = "labelFrameGUIDS", text = " Editor ")
	guiDS = GuiEditor(frameDS, name = "editor")
	labelFrameCDS = LabelFrame(frameDS, name = "labelFrameCDS", text = " Console ")
	terminalDS = ScrolledText(frameDS, name = "terminal", state = "disabled")
	labelFrameDSG = LabelFrame(frameDS, name = "labelFrameDSG", text = " General ")
	clearDS = Button(frameDS, name = "bClearTerm", text = CLEAR_CONSOLE, command = (lambda: clearTerminal(terminalDS)))
	runEditorDS = Button(frameDS, name = "bRunEditor", text = RUN_EDITOR, command = (lambda: runEditor(guiDS.editorText, DATA_SCRAPER, terminalDS)))
	saveScriptDS = Button(frameDS, name = "bSaveScript", text = SAVE_EDITOR, command = (lambda: saveScript(guiDS.editorText)))
	runExternalDS = Button(frameDS, name = "bRunExtern", text = RUN_EXTERNAL, command = (lambda: runExternal(DATA_SCRAPER, terminalDS)))	
	labelFrameDS = LabelFrame(frameDS, name = "labelFrameDS", text = " Specific Functions ")
	scrapeURL = Button(frameDS, name = "bScrapeURL", text = SCRAPE_URL)	
	scrapeString = Button(frameDS, name = "bScrapeString", text = SCRAPE_STRING)	
	
	guiDS.place(relx = 0.01, rely = 0.03, relheight = 0.55, relwidth = 0.7)
	terminalDS.place(relx = 0.035, rely = 0.63, relheight = 0.36, relwidth = 0.92)
	clearDS.place(relx = 0.86, rely = 0.52)
	runEditorDS.place(relx = 0.79, rely = 0.46)
	saveScriptDS.place(relx = 0.86, rely = 0.46)
	runExternalDS.place(relx = 0.79, rely = 0.52)
	labelFrameDS.place(relx = 0.76, rely = 0.27, relheight = 0.09, relwidth = 0.19)
	labelFrameDSG.place(relx = 0.76, rely = 0.43, relheight = 0.14, relwidth = 0.19)
	labelFrameGUIDS.place(relx = 0.005, rely = 0.0035, relheight = 0.59, relwidth = 0.715)
	labelFrameCDS.place(relx = 0.005, rely = 0.6, relheight = 0.4, relwidth = 0.96)
	scrapeURL.place(relx = 0.79, rely = 0.3)
	scrapeString.place(relx = 0.86, rely = 0.3)

	labelFrameGUIDC = LabelFrame(frameDC, name = "labelFrameGUIDC", text = " Editor ")
	guiDC = GuiEditor(frameDC, name = "editor")
	labelFrameCDC = LabelFrame(frameDC, name = "labelFrameCDC", text = " Console ")
	terminalDC = ScrolledText(frameDC, name = "terminal", state = "disabled")
	labelFrameDCG = LabelFrame(frameDC, name = "labelFrameDCG", text = " General ")
	clearDC = Button(frameDC, name = "bClearTerm", text = CLEAR_CONSOLE, command = (lambda: clearTerminal(terminalDC)))
	runEditorDC = Button(frameDC, name = "bRunEditor", text = RUN_EDITOR, command = (lambda: runEditor(guiDC.editorText, DATA_CLEANSER, terminalDC)))
	saveScriptDC = Button(frameDC, name = "bSaveScript", text = SAVE_EDITOR,  command = (lambda: saveScript(guiDC.editorText)))
	runExternalDC = Button(frameDC, name = "bRunExtern", text = RUN_EXTERNAL, command = (lambda: runExternal(DATA_CLEANSER, terminalDC)))
	labelFrameDC = LabelFrame(frameDC, name = "labelFrameDC", text = " Specific Functions ")
	removeColumns = Button(frameDC, name = "bRemoveColumns", text = REMOVE_COLUMNS)
	removeLine = Button(frameDC, name = "bRemoveLine", text = REMOVE_LINE)
	appendFiles = Button(frameDC, name = "bAppendFiles", text = APPEND_FILE)

	guiDC.place(relx = 0.01, rely = 0.03, relheight = 0.55, relwidth = 0.7)
	terminalDC.place(relx = 0.035, rely = 0.63, relheight = 0.36, relwidth = 0.92)
	clearDC.place(relx = 0.86, rely = 0.52)
	runEditorDC.place(relx = 0.79, rely = 0.46)
	saveScriptDC.place(relx = 0.86, rely = 0.46)
	runExternalDC.place(relx = 0.79, rely = 0.52)
	labelFrameDC.place(relx = 0.76, rely = 0.27, relheight = 0.14, relwidth = 0.19)
	labelFrameDCG.place(relx = 0.76, rely = 0.43, relheight = 0.14, relwidth = 0.19)
	labelFrameGUIDC.place(relx = 0.005, rely = 0.0035, relheight = 0.59, relwidth = 0.715)
	labelFrameCDC.place(relx = 0.005, rely = 0.6, relheight = 0.4, relwidth = 0.96)
	removeColumns.place(relx = 0.77, rely = 0.3)
	removeLine.place(relx = 0.86, rely = 0.3)
	appendFiles.place(relx = 0.77, rely = 0.36)

	labelFrameGUIDB = LabelFrame(frameDB, name = "labelFrameGUIDS", text = " Editor ")
	guiDB = GuiEditor(frameDB, name = "editor")
	labelFrameCDB = LabelFrame(frameDB, name = "labelFrameCDB", text = " Console ")
	terminalDB = ScrolledText(frameDB, name = "terminal", state = "disabled")
	labelFrameDBG = LabelFrame(frameDB, name = "labelFrameDBG", text = " General ")
	clearDB = Button(frameDB, name = "bClearTerm", text = CLEAR_CONSOLE, command = (lambda: clearTerminal(terminalDB)))
	runEditorDB = Button(frameDB, name = "bRunEditor", text = RUN_EDITOR, command = (lambda: runEditor(guiDB.editorText, DATA_BASE, terminalDB)))
	saveScriptDB = Button(frameDB, name = "bSaveScript", text = SAVE_EDITOR, command = (lambda: saveScript(guiDB.editorText)))
	runExternalDB = Button(frameDB, name = "bRunExtern", text = RUN_EXTERNAL, command = (lambda: runExternal(DATA_BASE, terminalDB)))
	labelFrameDB = LabelFrame(frameDB, name = "labelFrameDB", text = " Specific Functions ")
	insertCSV = Button(frameDB, name = "bInsertCSV", text = INSERT_CSV)
	insertJSON = Button(frameDB, name = "bInsertJSON", text = INSERT_JSON)

	guiDB.place(relx = 0.01, rely = 0.03, relheight = 0.55, relwidth = 0.7)
	terminalDB.place(relx = 0.035, rely = 0.63, relheight = 0.36, relwidth = 0.92)
	clearDB.place(relx = 0.86, rely = 0.52)
	runEditorDB.place(relx = 0.79, rely = 0.46)
	saveScriptDB.place(relx = 0.86, rely = 0.46)
	runExternalDB.place(relx = 0.79, rely = 0.52)
	labelFrameDB.place(relx = 0.76, rely = 0.27, relheight = 0.09, relwidth = 0.19)
	labelFrameDBG.place(relx = 0.76, rely = 0.43, relheight = 0.14, relwidth = 0.19)
	labelFrameGUIDB.place(relx = 0.005, rely = 0.0035, relheight = 0.59, relwidth = 0.715)
	labelFrameCDB.place(relx = 0.005, rely = 0.6, relheight = 0.4, relwidth = 0.96)
	insertCSV.place(relx = 0.79, rely = 0.3)
	insertJSON.place(relx = 0.86, rely = 0.3)

	labelFrameGUIDA = LabelFrame(frameDA, name = "labelFrameGUIDA", text = " Editor ")
	guiDA = GuiEditor(frameDA, name = "editor")
	labelFrameCDA = LabelFrame(frameDA, name = "labelFrameCDA", text = " Console ")
	terminalDA = ScrolledText(frameDA, name = "terminal", state = "disabled")
	labelFrameDAG = LabelFrame(frameDA, name = "labelFrameDAG", text = " General ")
	clearDA = Button(frameDA, name = "bClearTerm", text = CLEAR_CONSOLE, command = (lambda: clearTerminal(terminalDA)))
	runEditorDA = Button(frameDA, name = "bRunEditor", text = RUN_EDITOR, command = (lambda: runEditor(guiDA.editorText, DATA_ANALAYSIS, terminalDA)))
	saveScriptDA = Button(frameDA, name = "bSaveScript", text = SAVE_EDITOR, command = (lambda: saveScript(guiDA.editorText)))
	runExternalDA = Button(frameDA, name = "bRunExtern", text = RUN_EXTERNAL, command = (lambda: runExternal(DATA_ANALAYSIS, terminalDA)))	
	labelFrameDA = LabelFrame(frameDA, name = "labelFrameDA", text = " Specific Functions ")
	executePython = Button(frameDA, name = "bExecPy", text = EXECUTE_PYTHON)	
	executeR = Button(frameDA, name = "bExecR", text = EXECUTE_R)
	executeMatlab = Button(frameDA, name = "bExecMat", text = EXECUTE_MATLAB)

	guiDA.place(relx = 0.01, rely = 0.03, relheight = 0.55, relwidth = 0.7)
	terminalDA.place(relx = 0.035, rely = 0.63, relheight = 0.36, relwidth = 0.92)
	clearDA.place(relx = 0.86, rely = 0.52)
	runEditorDA.place(relx = 0.79, rely = 0.46)
	saveScriptDA.place(relx = 0.86, rely = 0.46)
	runExternalDA.place(relx = 0.79, rely = 0.52)
	labelFrameDA.place(relx = 0.76, rely = 0.27, relheight = 0.14, relwidth = 0.19)
	labelFrameDAG.place(relx = 0.76, rely = 0.43, relheight = 0.14, relwidth = 0.19)
	labelFrameGUIDA.place(relx = 0.005, rely = 0.0035, relheight = 0.59, relwidth = 0.715)
	labelFrameCDA.place(relx = 0.005, rely = 0.6, relheight = 0.4, relwidth = 0.96)
	executePython.place(relx = 0.78, rely = 0.3)
	executeR.place(relx = 0.86, rely = 0.3)
	executeMatlab.place(relx = 0.78, rely = 0.36)

if __name__ == '__main__':
	main() 