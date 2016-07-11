#!/usr/bin/python
# Title: pipInstall.py
# Description: Contains the grammar and the methods to install python modules using pip
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-11
# Version: 0.1
# Usage: python pipInstall.py
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

# Rules
comma = Suppress(Literal(","))
executePipReservedWord = Suppress(Keyword("pipInstall"))
packages = QuotedString('"', escChar = "\\").setResultsName("packages", listAllMatches = True)
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
executePipExpr = executePipReservedWord + leftBracket + (packages | varID) + ZeroOrMore(comma + (packages | varID)) + rightBracket

# Install packages using pip
def pipInstall(tokens, varStack):
	packagesList = []
	if len(tokens.varID) > 0:
		iterator = 0
		for var in tokens.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					packagesList.append(item[1])
			iterator += 1
	if len(tokens.packages) > 0:
		for item in tokens.packages[:]:
			packagesList.append(item)

	print packagesList

executePipExpr.setParseAction(lambda tokens: pipInstall(tokens, varStack))