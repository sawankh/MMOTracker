# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import os, sys

path = ''

# Adds path if not default folder
if len(sys.argv) > 0:
	path = sys.argv[1:]
	print path[0]

title = raw_input("Enter a title for your script: ")

# Add .py to the end of the script.
title = title + '.py'

# Convert all letters to lower case.
title = title.lower()

# Remove spaces from the title.
title = title.replace(' ', '_')

# Check to see if the file exists to not overwrite it.
if exists(title):
    print "\nA script with this name already exists."
    exit(1)

descrpt = raw_input("Enter a description: ")
name = "Sawan J. Kapai Harpalani"
ver = "0.1"
gnu = 'Copyright 200X Sawan J. Kapai Harpalani \n# This file is part of MMOTracker. MMOTracker is free software: you can redistribute it  and/or modify \n# it under the terms of the GNU GeneralPublic License as published by the Free Software  Foundation, \n# either version 3 of the License,  or (at your option) any later version \n# MMOTracker is distributed in the hope that it willbe useful, but WITHOUT ANY WARRANTY; without \n# even the implied warranty of MERCHANTABILITY or FITNESSFOR A PARTICULAR PURPOSE. See the GNU General \n# PubliLicense for more details.You should have received a copy of the GNU GeneralPublic License along with MMOTracker. \n# If not, seehttp://www.gnu.org/licenses/.'
div = '======================================='

# Create a file that can be written to.
filename = open(path[0] + title, 'w')

# Set the date automatically.
date = strftime("%Y-%m-%d")

# Write the data to the file. 
filename.write('#!/usr/bin/python')
filename.write('\n# Title: ' + title)
filename.write('\n# Description: ' + descrpt)
filename.write('\n# Author: ' + name)
filename.write('\n# Date: ' + date)
filename.write('\n# Version: ' + ver)
filename.write('\n# Usage: ' + 'python ' + title)
filename.write('\n# Notes: ')
filename.write('\n# python_version: 2.6.6')
filename.write('\n# License: ' + gnu)
filename.write('\n#' + div * 2 + '\n')
filename.write('\n')
filename.write('\n')

# Close the file after writing to it.
filename.close()

# Clear the screen. This line of code will not work on Windows.
os.system("clear") 

print "Done!"
