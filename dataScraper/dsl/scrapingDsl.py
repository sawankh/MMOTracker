#!/usr/bin/python
# Title: scrapingDsl.py
# Description: Main structures and mechanism of the data scraping agent's domain specific language(dsl)
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-25
# Version: 0.1
# Usage: python scrapingDsl.py
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

import sys

sys.path.insert(0, 'grammar/basic_functionality')

from clearConsole import *
from comments import *
from loop import *
from printConsole import *
from sleep import *
from variable import *


# DSL types of expression
newLine = Suppress(White("\n"))
agentDSL = ZeroOrMore((clearExpr | commentsExpr | loopExpr | printExpr | sleepExpr | assignment) + Optional(newLine))

agentDSL.parseString("a -> 2 \n printConsole(a) \n x -> 4 printConsole(x1 + \"dsadas\") clearConsole()")