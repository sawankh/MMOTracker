#!/usr/bin/python
# Title: loop.py
# Description: Contains the grammar and the set of rules to create loops for the dsl
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-24
# Version: 0.1
# Usage: python loop.py
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
loopReservedWord = Suppress(Literal("repeat"))
arrow = Suppress(Literal("->"))
identifier = Word(alphas, alphanums + UNDERSCORE)
fromVar = Word(nums) | identifier
toVar = Word(nums) | identifier
toReservedWord = Suppress(Literal("to"))
endReservedWord = Suppress(Literal("end"))
statement = Word(printables)
newLine = Suppress(Literal("\n"))
loopExpr = loopReservedWord + identifier + arrow + fromVar + toReservedWord + toVar + OneOrMore(newLine)
print loopExpr.parseString("repeat i -> 1 to 10")