import os
from datetime import datetime
import lib.DirectoryHelper as DirectoryHelper

def createDataPath():
	os.makedirs(DirectoryHelper.getDataDir(), exist_ok=True)

def getFileOfDate(dt):
	day = f'{dt.day:02d}'
	month = f'{dt.month:02d}'
	dayFile = "{month}_{day}.txt".format(month=month, day=day)
	
	return DirectoryHelper.getDataDir() + "/" + dayFile

def getDayFile():
	today = datetime.today()
	return getFileOfDate(today)

def getUniqueTimestampsOfFile(dateFile):
	f = open(dateFile, "r")
	lines = f.readlines()
	f.close()
	
	uniqueLines = []
	for line in lines:
		clearLine = line.replace("\n", "").strip()
		if clearLine not in uniqueLines:
			uniqueLines.append(clearLine)
	
	return uniqueLines

def getFirstLineOfFile(file):
	with open(file) as f:
		return f.readline().strip('\n')