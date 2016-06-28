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

from types import *

# Constants
DEFAULT_IDENTATION = 4
DEFAULT_DELIMITATOR = '__'
BLANK = 'NULL'

# Creates a json object from a string
def stringToJSON(jsonString):
	return json.loads(jsonString)

# Transform json object to string
def jsonToString(jsonObject):
	return json.dumps(jsonObject)

# prints json object in a pretty way
def printJSON(jsonObject, indentationValue = DEFAULT_IDENTATION):
	print json.dumps(jsonObject, indent = indentationValue, sort_keys = True)

# Reads JSON from an existing file
def readJSONFile(fileName):
    fileOpen = open(fileName, 'r')
    content = fileOpen.read()
    return json.loads(content)

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

# Converts to string
def toString(s):
    try:
        return str(s)
    except:
        return s.encode('utf-8')

# Returns data processed and ready to write in CSV
def getProcessedData(content, node):
    xs = 0
    processedData = []
    headerList = []
    for item in content:
        xs += 1
        reducedElement = {}
        reduce_item(node, item, reducedElement)

        headerList += reducedElement.keys()

        processedData.append(reducedElement)

    headerList = list(set(headerList))
    headerList.sort()
    
    return headerList, processedData

def clearDictionary(reducedElement):
    reducedElement.clear()

# Reduces elements
def reduce_item(key, value, reducedElement):
    # global reducedElement

    if type(value) is list:
        i = 0
        for sub_item in value:
            reduce_item(key + '_' + toString(i), sub_item, reducedElement)
            i += 1
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key + '_' + toString(sub_key), value[sub_key], reducedElement)
    else:
        reducedElement[toString(key)] = toString(value)

# Returns a list with all the different headerLists that the JSON object contains
def getheaderLists(jsonObjectList):
    headerListsList = []
    for json in jsonObjectList:
        for key in json.keys():
            if key not in headerListsList:
                headerListsList.append(key)
    return headerListsList

# Returns a list with the content ready to write in CSV
def getData(jsonObjectList, headerListList):
    dataList = []
    for json in jsonObjectList:
        row = []
        for headerList in headerListList:
            if headerList in json.keys():
                value = json.get(headerList, '')
                if type(value) is StringTypes:
                    row.append(value.encode('utf-8'))
                else:
                    row.append(value)
            else:
                row.append(BLANK)
        dataList.append(row)
    return dataList
        # for key, value in json.iteritems():
        #      print("key: {} | value: {}".format(key, value))
            # print content.key()