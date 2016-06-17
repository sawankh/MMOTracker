#!/usr/bin/python
# Title: jsonHandle.py
# Description: Contains all sort of operations with JSON objects
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-17
# Version: 0.1
# Usage: python jsonHandle.py
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

import json

# Constants
DEFAULT_IDENTATION = 4

# Creates a json object from a string
def stringToJSON(jsonString):
	return json.loads(jsonString)

# prints json object in a pretty way
def printJSON(jsonObject, indentationValue = DEFAULT_IDENTATION):
	print json.dumps(jsonObject, indent = indentationValue, sort_keys = True)