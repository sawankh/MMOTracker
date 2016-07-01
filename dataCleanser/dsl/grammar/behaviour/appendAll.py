#!/usr/bin/python
# Title: appendAll.py
# Description: Contains the grammar and methods for creating one csv from all the files in that folder
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-01
# Version: 0.1
# Usage: python appendAll.py
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

from pyparsing import *
from dsl.grammar.basic_functionality.variable import *

import progressbar, datetime, glob
import pandas as pd

# Rules
comma = Suppress(Literal(","))
appendAllReservedWord = Suppress(Keyword("appendAll"))
path = QuotedString('"', escChar = "\\").setResultsName("path")
fileType = QuotedString('"', escChar = "\\").setResultsName("fileType")
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
appendAllExpr = appendAllReservedWord + leftBracket + (path + comma + (fileType | varID)) + rightBracket

# Method appends all files
def appendAll(tokens, varStack):
	path = ''
	fileType = ''
	if len(tokens.varID) > 0:
		for var in sList.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					fileType += item[1]
	if len(tokens.path) > 0:
		path = tokens.path
	if len(tokens.fileType) > 0:
		fileType = tokens.fileType

	print "Combining all files from --->" + path

	headers = True
	currentFile = None
	currentDate = datetime.datetime.now().strftime("%Y%m%d%H %M")

	allFiles = glob.glob(path + "/*.csv")
	frame = pd.DataFrame()
	list_ = []

	bar = progressbar.ProgressBar(maxval = len(allFiles), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.Timer()])
	iterator = 0
	

	bar.start()
	for f in allFiles:
		fileN = open(f)
		numline = len(fileN.readlines())
		if numline > 1:
			df = pd.read_csv(f, header = 0, engine='python', skip_blank_lines=True)
			list_.append(df)
		bar.update(iterator + 1)
		iterator += 1
		fileN.close()
	frame = pd.concat(list_, ignore_index = True)
	frame.to_csv(currentDate + ".csv", mode='a', index = False)
	bar.finish()
	print "Written file successfully --->" + path + currentDate

appendAllExpr.setParseAction(lambda tokens: appendAll(tokens, varStack))