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

from dsl.grammar.behaviour.readFile import *
from dsl.grammar.behaviour.stringJoin import *
from dsl.grammar.behaviour.readLine import *

"""Constants"""
UNDERSCORE = '_'
varStack = []

"""Rules"""
identifier = Word(alphas, alphanums + UNDERSCORE)
number = Word(nums + '.')
string = QuotedString('"', unquoteResults = False)
arrow = Suppress('->')
assignment =  identifier.setResultsName("varName") + arrow + ( readFileExpr | readLineExpr.setParseAction(lambda tokens: readLine(tokens, varStack)) | joinStringExpr.setParseAction(lambda tokens: joinString(tokens, varStack)) | identifier | number | string).setResultsName("varValue")



def addStack(tokens):
	""" Adds element to the execution stack """
	if inList(varStack, tokens.varName):
		del varStack[getIndex(varStack, tokens.varName)]
		varStack.append(tokens[:])
	elif isInteger(tokens.varValue) is False:
		if inList(varStack, tokens.varValue):
			tokens[1] = getValue(tokens.varValue)
			varStack.append(tokens[:])
		else:
			varStack.append(tokens[:])
	else:
		varStack.append(tokens[:])

def inList(data, search):
	"""Check if an element is in the list"""
	for sublist in data:
		if sublist[0] == search:
			return True            

def getIndex(data, search):
	"""Get index of the element in the list"""
	iterator = 0
	for sublist in data:
		if sublist[0] == search:
			return iterator   
		iterator += 1       

def isInteger(string):
	"""Checks if string is integer"""
	try:
		int(string)
		return True
	except ValueError:
		return False

def getValue(string):
	"""Checks if the string is a integer or a variable, if is the last one returns its actual value from the stack"""
	if isInteger(string):
		return string
	elif inList(varStack, string):
		return varStack[getIndex(varStack, string)][1]
	else:
		raise Exception("Something went wrong while trying to parse your code!! Somewhere around " + string)

assignment.setParseAction(addStack)