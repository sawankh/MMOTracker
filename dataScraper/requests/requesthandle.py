#!/usr/bin/python
# Title: requesthandle.py
# Description: Handles all the request and collects the results
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-17
# Version: 0.1
# Usage: python requesthandle.py
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

import requests

# Execute a get request 
def getRequest(request):
	return requests.get(request)

# Execute a get request with payload
def getRequestPayload(request, payload):
	return requests.get(request, params = payload)

# Execute a post request
def postRequest(request, content):
	return requests.post(request, data = content)

# Gets url of the request
def getURL(request):
	return request.url

# Gets status code for request
def getCode(request):
	return request.status_code

# Prints code of request
def printCode(request):
	print "The request's status code is: " + str(request.status_code)

# Prints url
def printURL(request):
	print "The request's url is: " + request.url