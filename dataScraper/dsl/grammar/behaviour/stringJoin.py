#!/usr/bin/python
# Title: stringJoin.py
# Description: Contains the grammar and methods to join two or more strings
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-27
# Version: 0.1
# Usage: python stringJoin.py
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
stringJoinReservedWord = Suppress(Keyword("joinString"))
string = QuotedString('"', escChar = "\\").setResultsName("stringsToJoin", listAllMatches = False)
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
joinStringExpr = stringJoinReservedWord + leftBracket + (string + comma + string) + ZeroOrMore(comma + string) + rightBracket

# Joins strings and returns quoted string
def joinString(sList):
	resultString = ''
	for s in sList:
		resultString += s
	return "\"" + resultString + "\""

joinStringExpr.setParseAction(lambda tokens: joinString(tokens))