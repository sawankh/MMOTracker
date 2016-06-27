#!/usr/bin/python
# Title: scrapeURL.py
# Description: Contains the grammar and the methods to scrape an URL
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-27
# Version: 0.1
# Usage: python scrapeURL.py
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
###############################################################################

from pyparsing import *

import ast, sys

sys.path.insert(1, '../../../requests/')

from requestHandle import *
from jsonHandle import *
from csvHandle import *

# Constants
HEADERS = 0
CONTENT = 1
BLANK = ' '
CSV_EXTENSION = '.csv'
SEPARATOR = "##############################################################################"
SUCCESS_REQUEST = 200

# Rules
scrapeURLReservedWord = Suppress(Keyword("scrapeURL"))
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
comma = Suppress(Literal(","))
URL = QuotedString('"', escChar = "\\")
node = QuotedString('"', escChar = "\\")
Path = QuotedString('"', escChar = "\\")
fileName = QuotedString('"', escChar = "\\")
trueKeyword = CaselessKeyword("True")
falseKeyword = CaselessKeyword("False")
scrapeURLExpr = scrapeURLReservedWord + leftBracket + URL.setResultsName("url") + comma + node.setResultsName("node") + comma + fileName.setResultsName("fileName") + comma + Path.setResultsName("path") + comma + (trueKeyword | falseKeyword).setResultsName("log") + rightBracket

# Scrapes an URL and returns csv
def scrapeURL(strUrl, strNode, strFileName, strPath, log):
	requestURL = getRequest(strUrl)
	
	print SEPARATOR
	printCode(requestURL)
	printURL(requestURL)
	jsonString = getContent(requestURL)
	jsonObject = stringToJSON(jsonString)
	print SEPARATOR
	if getCode(requestURL) == SUCCESS_REQUEST: 
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
	else:
		print "Shutting down wrong error in request!"
		sys.exit(2)

scrapeURLExpr.setParseAction(lambda tokens: scrapeURL(tokens.url, tokens.node, tokens.fileName, tokens.path, ast.literal_eval(tokens.log)))