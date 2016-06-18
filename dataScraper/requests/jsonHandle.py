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
DEFAULT_DELIMITATOR = '__'

# Creates a json object from a string
def stringToJSON(jsonString):
	return json.loads(jsonString)

# Transform json object to string
def jsonToString(jsonObject):
	return json.dumps(jsonObject)

# prints json object in a pretty way
def printJSON(jsonObject, indentationValue = DEFAULT_IDENTATION):
	print json.dumps(jsonObject, indent = indentationValue, sort_keys = True)

# Removes levels of the json object, returning a flat object
def flattenJSON(jsonObject, delim = DEFAULT_DELIMITATOR):
    result = {}
    for i in jsonObject.keys():
        if isinstance( jsonObject[i], dict ):
            get = flattenJSON( jsonObject[i], delim )
            for j in get.keys():
                result[ i + delim + j ] = get[j]
        else:
            result[i] = jsonObject[i]
    return result

# Check if the object contains elements of the same size
def checkSize(jsonObjectList):
    sizeFirst = len(jsonObjectList[0].keys()) 
    for item in jsonObjectList:
        if sizeFirst != len(item.keys()):
            return False
    return True