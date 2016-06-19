#!/usr/bin/python
# Title: csvHandle.py
# Description: Handles all kind of required with CSV files
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-18
# Version: 0.1
# Usage: python csvHandle.py
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

import csv

# Constants
DEFAULT_PATH = ''

# Writes content to a csv file
def writeCSV(fileName, headers, content, path = DEFAULT_PATH):
	fileOpen = open(path + fileName, 'w')
	fileWriter = csv.writer(fileOpen)
	fileWriter.writerow(headers)
	
	for data in content:
		#print data
		fileWriter.writerow(data)
	
	fileOpen.close()