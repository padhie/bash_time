import time
import lib.FileHelper as FileHelper
import lib.CliHelper as CliHelper

print("using DayFile: ", FileHelper.getDayFile())
print("start timer")

def addTimestampToDayFile():
	with open(FileHelper.getDayFile(),'a+') as f:
		currentTimestamp = int(time.time())
		print('current timestamp', currentTimestamp)
		f.write(str(currentTimestamp) + "\n")

def runLoop():
	while True:
		addTimestampToDayFile()
		time.sleep(60)


mode = CliHelper.getArg(1)

if mode == "single":
	addTimestampToDayFile()
else:
	runLoop()