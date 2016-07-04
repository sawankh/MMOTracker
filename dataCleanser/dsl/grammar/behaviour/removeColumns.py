#!/usr/bin/python
# Title: removeColumns.py
# Description: Contains the grammar and the methods to remove from a csv file
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-04
# Version: 0.1
# Usage: python removeColumns.py
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

import progressbar, datetime
import pandas as pd

# Constants
SEPARATOR = "##############################################################################"

# Rules
comma = Suppress(Literal(","))
removeColumnsReservedWord = Suppress(Keyword("removeColumns"))
columns = QuotedString('"', escChar = "\\").setResultsName("columns", listAllMatches = True)
fileToTransform = QuotedString('"', escChar = "\\").setResultsName("fileToTransform")
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
removeColumnsExpr = removeColumnsReservedWord + leftBracket + (fileToTransform | varID) + comma + OneOrMore(columns | varID + Optional(comma)) + rightBracket

# Removes the clomuns desired from the csv file
def removeColumns(tokens, varStack):
	fileToTransform = ''
	columns = []
	if len(tokens.varID) > 0:
		iterator = 0
		for var in sList.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					if iterator == 0:
						fileToTransform += item[1]
					else:
						columns.append(item[1])
			iterator += 1
	if len(tokens.fileToTransform) > 0:
		fileToTransform += tokens.fileToTransform
	if len(tokens.columns) > 0:
		for item in tokens.columns[:]:
			columns.append(item)

	fileToTransformPd = pd.read_csv(fileToTransform)
	print SEPARATOR
	print "Removing columns " + columns + " from " + fileToTransform
	print SEPARATOR
	
	bar = progressbar.ProgressBar(maxval = len(columns), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.Timer()])

	bar.start()
	progress = 0
	for column in columns:
		fileToTransformPd.drop(column, axis = 1, inplace = True)
		bar.update(progress + 1)
		progress += 1
	bar.finish()

	splitedPath = fileToTransform.split(".csv")
	currentDate = datetime.datetime.now().strftime("%Y%m%d%H %M")
	outputFile = splitedPath[0] + currentDate + ".csv"

	fileToTransformPd.to_csv(outputFile)
	print "Written successfully to " + outputFile
	
removeColumnsExpr.setParseAction(lambda tokens: removeColumns(tokens, varStack))