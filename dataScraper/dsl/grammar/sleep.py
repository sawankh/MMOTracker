#!/usr/bin/python
# Title: sleep.py
# Description: Contains the grammar and the method to sleep the agent for a certain amount of time
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-23
# Version: 0.1
# Usage: python sleep.py
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

import progressbar, time

# Rules
sleepReservedWord = Suppress(Literal("sleep"))
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
number = Word(nums)
sleepExpr = sleepReservedWord + leftBracket + number.setResultsName("value") + rightBracket

# Sleeps the agent for the value especified of seconds
def sleepAgent(value):
	value = stringToInt(value)
	bar = progressbar.ProgressBar(maxval = len(value), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.Timer()])

	bar.start()
	for i in range(0, value):
		sleep(1)
	bar.finish()

# Converts string to int
def stringToInt(strNumber):
	return int(strNumber)


x = []
x.append(sleepExpr.parseString("sleep(3)").value)
x.append(sleepExpr.parseString("sleep(2)").value)
x.append(sleepExpr.parseString("sleep(1)").value)
x.append(sleepExpr.parseString("sleep(4)").value)
x.append(sleepExpr.parseString("sleep(7)").value)
print x[0]
sleepAgent(x[0])