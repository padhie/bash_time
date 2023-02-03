import os
import lib.FileHelper as FileHelper

def getTrackedMinutesOfDate(dt):
	dateFile = FileHelper.getFileOfDate(dt)
	if not os.path.isfile(dateFile):
		return 0
	
	timestamps = FileHelper.getUniqueTimestampsOfFile(dateFile)
	return len(timestamps)