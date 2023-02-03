import time
import lib.FileHelper as FileHelper

print("using DayFile: ", FileHelper.getDayFile())
print("start timer")

with open(FileHelper.getDayFile(),'a+') as f:
	while True:
		currentTimestamp = int(time.time())
		
		print('current timestamp', currentTimestamp)
		f.write(str(currentTimestamp) + "\n")
		
		time.sleep(60)
