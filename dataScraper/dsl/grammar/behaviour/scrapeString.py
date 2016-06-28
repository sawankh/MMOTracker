#!/usr/bin/python
# Title: scrapeString.py
# Description: Contains the grammar and the methods to scrape a string
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-27
# Version: 0.1
# Usage: python scrapeString.py
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

import ast

from requests.requestHandle import *
from requests.jsonHandle import *
from requests.csvHandle import *
from grammar.basic_functionality.variable import *

# Constants
HEADERS = 0
CONTENT = 1
BLANK = ' '
CSV_EXTENSION = '.csv'
LOG_EXTENSION = '.log'
SEPARATOR = "##############################################################################"
SUCCESS_REQUEST = 200

# Rules
scrapeStringReservedWord = Suppress(Keyword("scrapeString"))
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
comma = Suppress(Literal(","))
string = QuotedString('"', escChar = "\\")
node = QuotedString('"', escChar = "\\")
Path = QuotedString('"', escChar = "\\")
fileName = QuotedString('"', escChar = "\\")
trueKeyword = CaselessKeyword("True")
falseKeyword = CaselessKeyword("False")
varID = identifier
scrapeStringExpr = scrapeStringReservedWord + leftBracket + (string.setResultsName("content") | identifier.setResultsName("varIDC")) + comma + (node.setResultsName("node") | identifier.setResultsName("varIDN")) + comma + (fileName.setResultsName("fileName") | identifier.setResultsName("varIDF")) + comma + (Path.setResultsName("path") | identifier.setResultsName("varIDP")) + comma + (trueKeyword | falseKeyword).setResultsName("log") + rightBracket

# Checks the stack and returns value
def checkStack(element, alternative, stack):
	resultString = ''
	if len(element) > 0:
		for item in stack[:]:
			if element == item[0]:
				if item[1].startswith('"') and item[1].endswith('"'):
				    item[1] = item[1][1:-1]
				resultString += item[1]
				return resultString
	elif len(alternative) > 0:
		resultString = alternative
		return resultString
	else:
		resultString = ''

# Scrapes an String and returns csv
def scrapeString(tokens):
	log = ast.literal_eval(tokens.log)
	strContent = checkStack(tokens.varIDC, tokens.content, varStack)
	strNode = checkStack(tokens.varIDN, tokens.node, varStack)
	strFileName = checkStack(tokens.varIDF, tokens.fileName, varStack)
	strPath = checkStack(tokens.varIDP, tokens.path, varStack)

	if log is True:
		print "Writing log file..."
		with open(strPath + strFileName + LOG_EXTENSION, "w") as logFile:
		    logFile.write(strContent)
		print "Log file written successfully --> " + strPath + strFileName
	print SEPARATOR
	jsonObject = stringToJSON(strContent)
	print SEPARATOR
	print "Your data is being processed..."
	if strNode is BLANK:
		processData = getProcessedData(jsonObject, BLANK)	
	else:
		processData = getProcessedData(jsonObject[strNode], strNode)
	print "Data processed successfully!"

	print SEPARATOR
	print "Going to write CSV..."
	writeDictCSV(strFileName + CSV_EXTENSION, processData[HEADERS], processData[CONTENT], strPath)
	print "CSV written successfully ---> " + strPath + strFileName + CSV_EXTENSION
	
scrapeStringExpr.setParseAction(lambda tokens: scrapeString(tokens))
