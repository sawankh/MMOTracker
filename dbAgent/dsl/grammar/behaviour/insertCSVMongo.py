#!/usr/bin/python
# Title: insertCSVMongo.py
# Description: Contains the grammar and the methods to insert a csv file to a mongo database
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-09
# Version: 0.1
# Usage: python insertCSVMongo.py
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
from pymongo import MongoClient
from dsl.grammar.basic_functionality.variable import *

import progressbar, csv


# Constants
SEPARATOR = "##############################################################################"
HOST = 0
PORT = 1
DB_NAME = 2
COLLECTION_NAME = 3
FILE = 4

# Rules
comma = Suppress(Literal(","))
insertCSVMongoReservedWord = Suppress(Keyword("insertCSVMongo"))
host = QuotedString('"', escChar = "\\").setResultsName("host")
port = QuotedString('"', escChar = "\\").setResultsName("port")
dbName = QuotedString('"', escChar = "\\").setResultsName("dbName")
collectionName = QuotedString('"', escChar = "\\").setResultsName("collectionName")
fileToInsert = QuotedString('"', escChar = "\\").setResultsName("fileToInsert")
leftBracket = Suppress(Literal("("))
rightBracket = Suppress(Literal(")"))
varID = Word(alphas, alphanums + "_").setResultsName("varID", listAllMatches = True)
insertCSVMongoExpr = insertCSVMongoReservedWord + leftBracket + (host | varID) + comma + (port | varID) + comma + (dbName | varID) + comma + (collectionName | varID) + comma + (fileToInsert | varID) + rightBracket

# Insert csv file to MongoDB
def insertCSVMongo(tokens, varStack):
	print tokens
	hostDB = ''
	portDB = ''
	dbNameDB = ''
	collectionNameDB = ''
	fileToInsertDB = ''
	if len(tokens.varID) > 0:
		iterator = 0
		for var in tokens.varID.asList():
			for item in varStack[:]:
				if var == item[0]:
					if item[1].startswith('"') and item[1].endswith('"'):
						item[1] = item[1][1:-1]
					if iterator == HOST:
						hostDB += item[1]
					elif iterator == PORT:
						portDB += item[1]
					elif iterator == DB_NAME:
						dbNameDB += item[1]
					elif iterator == COLLECTION_NAME:
						collectionNameDB += item[1]
					elif iterator == FILE:
						fileToInsertDB += item[1]
			iterator += 1
	if len(tokens.host) > 0:
		hostDB += tokens.host
	if len(tokens.port) > 0:
		portDB += tokens.port
	if len(tokens.dbName) > 0:
		dbNameDB += tokens.dbName
	if len(tokens.collectionName) > 0:
		collectionNameDB += tokens.collectionName
	if len(tokens.fileToInsert) > 0:
		fileToInsertDB += tokens.fileToInsert

	print SEPARATOR
	print "Inserting " + fileToInsertDB + " to Mongo database --> " + hostDB + ":" + portDB
	print SEPARATOR

	mongoConnection = MongoClient(hostDB, int(portDB))
	mongoDatabase = mongoConnection[dbNameDB]
	mongoCollection = mongoDatabase[collectionNameDB]

	csvFile = open(fileToInsertDB, 'r')
	fileSize = open(fileToInsertDB, 'r')
	csvReader = csv.DictReader(csvFile)
	row_count = len(fileSize.readlines()) - 1

	print "Inserting to database --> " + dbNameDB + " to collection -->" + collectionNameDB
	print SEPARATOR

	bar = progressbar.ProgressBar(maxval = row_count, widgets = [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	iterator = 0

	bar.start()
	for entry in csvReader:
		bar.update(iterator + 1)
		mongoCollection.insert_one(entry)
		iterator += 1
	bar.finish()
	print "Insertion successfull!"
	print SEPARATOR

insertCSVMongoExpr.setParseAction(lambda tokens: insertCSVMongo(tokens, varStack))