#!/usr/bin/python
# Title: variable.py
# Description: Contains the grammar and the implementation of the variable declaration for the domain specific language
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-22
# Version: 0.1
# Usage: python variable.py
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

# Constants
UNDERSCORE = '_'

# Rules
identifier = Word(alphas, alphanums + UNDERSCORE)
number = Word(nums + '.')
arrow = Suppress('->')
assignment =  identifier.setResultsName("varName") + arrow + (identifier | number).setResultsName("varValue")

varStack = []

def addStack(tokens):
	if inList(varStack, tokens.varName):
		del varStack[getIndex(varStack, tokens.varName)]
		varStack.append(tokens)
	else:
		varStack.append(tokens)

# Check if an element is in the list
def inList(data, search):
    for sublist in data:
    	if sublist[0] == search:
			return True            

# Get index of the element in the list
def getIndex(data, search):
	iterator = 0
	for sublist in data:
		if sublist[0] == search:
			return iterator   
		iterator += 1       

assignment.setParseAction(addStack)