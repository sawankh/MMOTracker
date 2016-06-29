#!/usr/bin/python
# Title: readLine.py
# Description: Contains the grammar and methods to read a specific line of a file
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-29
# Version: 0.1
# Usage: python readLine.py
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

# Rules
comma = Suppress(Literal(","))
readLineReservedWord = Suppress(Keyword("readLine"))
fileName = QuotedString('"', escChar = "\\").setResultsName("fileName")
lineNumber = QuotedString('"', escChar = "\\").setResultsName("lineNumber")
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
readLineExpr = readLineReservedWord + leftBracket + (fileName + comma + (lineNumber | varID)) + rightBracket

# Joins strings and returns quoted string
def readLine(sList, varStack):
	resultString = ''
	lineNu = ''
	fileN = ''
	if len(sList.varID) > 0:
		for var in sList.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					lineNu += item[1]
	if len(sList.fileName) > 0:
		fileN = sList.fileName
	if len(sList.lineNumber) > 0:
		lineNu = sList.lineNumber

	with open(fileN) as fp:
		for i, line in enumerate(fp):
			if i == (int(lineNu) - 1):
				resultString = line
				return "\"" + resultString + "\""
