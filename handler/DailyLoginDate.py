from datetime import datetime
import lib.FileHelper as FileHelper

def run():
	dayFile = FileHelper.getDayFile()
	timestamp = FileHelper.getFirstLineOfFile(dayFile)
	datetimeObject = datetime.fromtimestamp(int(timestamp))
	
	print(datetimeObject.strftime("%H:%m UTC"))