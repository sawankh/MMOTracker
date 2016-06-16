#!/usr/bin/python
# Title: DSAgent.py
# Description: Scraping agent that takes an API as input and produces csv files of raw data
# Author: Sawan J. Kapai Harpalani
# Date	: 2016-06-16
# Version: 0.1
# Usage: python p.py
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
#=============================================================================


import sys, getopt



# Error Constants
OPTION_ERROR = 0
PARAM_ERROR = 1
NO_ARG = 2
MAND_ARG_MISSING = 3
READING_CONF_ERROR = 4


def main(argv):
	if len(argv):
		printError(NO_ARG)

	try:
		opts, args = getopt.getopt(argv, 'h:c:u:p', ['help', 'configFile=', 'username=', 'password='])
	except getopt.GetoptError:
		printError(OPTION_ERROR)

	configFile = ''

	for opt, arg in opts:
		if opt in ('-h', '--help'):
		 	printHelp()
		elif opt in ('-c', '--config'):
		 	configFile = arg
		elif opt in ('-u', '--username'):
		 	userName = askUser()
		elif opt in ('-p', '--password'):
		 	password = askPassword()		
		else:
		 	printError(PARAM_ERROR)


# Prints errors 
def printError(errorType):
	if errorType == OPTION_ERROR:
		print 'Options Error: One or more options inserted do not exist'
	elif errorType == PARAM_ERROR:
		print 'Parameters Error: One or more parameters are missing'	
	elif errorType == NO_ARG:
		print 'No arguments shutting down! Bye Bye!'
	elif errorType == MAND_ARG_MISSING:
		print 'Mandatory arguments are missing!'
	elif errorType == READING_CONF_ERROR:
		print 'Error occurred while reading configuration file!'	

	sys.exit(2)

def askUser():
	#### Ask user name ####

def askPassword():
	#### Ask user password ####	