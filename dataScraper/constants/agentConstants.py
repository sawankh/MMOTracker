#!/usr/bin/python
# Title: agentconstants.py
# Description: Contains all the constants required for the proper execution of the Scraper Agent.
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-16
# Version: 0.1
# Usage: python agentconstants.py
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

# Error Constants
OPTION_ERROR = 0
PARAM_ERROR = 1
NO_ARG = 2
MAND_ARG_MISSING = 3
READING_CONF_ERROR = 4

# Instruction Constant
COMMAND_HELP = ['-c: Configuration file, where all the information about the API and the output is contained', '--username: Username, indicates that username is required for the use of the API', '--password: Password, indicates that password is required for the use of the API']