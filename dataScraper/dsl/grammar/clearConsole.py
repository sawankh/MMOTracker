#!/usr/bin/python
# Title: clearConsole.py
# Description: Contains the grammar to clear the console
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-24
# Version: 0.1
# Usage: python clearConsole.py
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

import os

# Rules
clearReservedWorld = Literal("clearConsole")
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
clearExpr = clearReservedWorld + leftBracket + rightBracket

def clearConsole():
	os.system('cls' if os.name=='nt' else 'clear')

clearExpr.setParseAction(clearConsole)