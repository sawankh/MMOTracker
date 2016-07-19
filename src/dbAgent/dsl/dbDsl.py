#!/usr/bin/python
# Title: cleaningDsl.py
# Description: Main structures and mechanism of the data scraping agent's domain specific language(dsl)
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-25
# Version: 0.1
# Usage: python cleaningDsl.py
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

from dsl.grammar.basic_functionality.clearConsole import *
from dsl.grammar.basic_functionality.comments import *
from dsl.grammar.basic_functionality.loop import *
from dsl.grammar.basic_functionality.printConsole import *
from dsl.grammar.basic_functionality.sleep import *
from dsl.grammar.basic_functionality.variable import *
from dsl.grammar.behaviour.appendAll import *
from dsl.grammar.behaviour.insertCSVMongo import *
from dsl.grammar.behaviour.insertJSONMongo import *


"""DSL types of expression"""
newLine = Suppress(White("\n"))
agentDSL = ZeroOrMore((insertCSVMongoExpr | insertJSONMongoExpr | appendAllExpr | clearExpr | commentsExpr | loopExpr.setParseAction(lambda tokens: loop(tokens, agentDSL)) | printExpr | sleepExpr | assignment) + Optional(newLine))

def dslParseFile(fileName):
	"""Parses an entire file"""
	agentDSL.parseFile(fileName)

def dslParseString(string):
	"""Parses a string"""
	agentDSL.parseString(string)