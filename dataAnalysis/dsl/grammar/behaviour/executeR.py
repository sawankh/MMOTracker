#!/usr/bin/python
# Title: executeR.py
# Description: Contains the grammar and methods to execute an R script
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-11
# Version: 0.1
# Usage: python executeR.py
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

# Constants
FILE_NAME = 0

# Rules
comma = Suppress(Literal(","))
executeRReservedWord = Suppress(Keyword("executeR"))
fileName =  QuotedString('"', escChar = "\\").setResultsName("fileName")
arguments = QuotedString('"', escChar = "\\").setResultsName("arguments", listAllMatches = True)
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
executeRExpr = executeRReservedWord + leftBracket + (fileName | varID) + ZeroOrMore(comma + (arguments | varID)) + rightBracket

# Executes R script
def executeR(tokens, varStack):
	fileName = ''
	args = []
	if len(tokens.varID) > 0:
		iterator = 0
		for var in tokens.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					if iterator == FILE_NAME:
						fileName += item[1]
					else:
						args.append(item[1])
			iterator += 1
	if len(tokens.fileName) > 0:
		fileName += tokens.fileName
	if len(tokens.arguments) > 0:
		for item in tokens.arguments[:]:
			args.append(item)
	print fileName
	print args

executeRExpr.setParseAction(lambda tokens: executeR(tokens, varStack))