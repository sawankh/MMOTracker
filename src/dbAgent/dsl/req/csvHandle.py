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

import csv, progressbar, time

"""Constants"""
DEFAULT_PATH = ''

def writeCSV(fileName, headers, content, path = DEFAULT_PATH):
	"""Writes content to a csv file"""
	fileOpen = open(path + fileName, 'wb')
	fileWriter = csv.writer(fileOpen)
	fileWriter.writerow(headers)
	
	bar = progressbar.ProgressBar(maxval = len(content), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.Timer()])

	bar.start()
	for data in content:
		fileWriter.writerow(data)
	bar.finish()

	fileOpen.close()

def writeDictCSV(fileName, headers, content, path = DEFAULT_PATH):
	"""Writes a dictionary to CSV, better for JSON objects"""
	with open(path + fileName, 'wb+') as f:
	    writer = csv.DictWriter(f, headers, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
	    writer.writeheader()

	    if len(content) > 0:
	    	bar = progressbar.ProgressBar(maxval = len(content), widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage(), ' ', progressbar.Timer()])
	    	
	    	bar.start()
	    	for row in content:
	    	    writer.writerow(row)
	    	bar.finish()
