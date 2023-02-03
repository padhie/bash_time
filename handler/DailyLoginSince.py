import time
import lib.FileHelper as FileHelper
import lib.TimeCalculator as TimeCalculator

def run():
	now = int(time.time())
	dayFile = FileHelper.getDayFile()
	timestamp = int(FileHelper.getFirstLineOfFile(dayFile))
	
	seconds = now - timestamp
	output = ""
	
	if seconds >= 86400:
		days = TimeCalculator.getDaysOfSeconds(seconds)
		seconds = TimeCalculator.subDaysOfSeconds(seconds, days)
		output += " " + f'{days:02d}' + "d"
	
	if seconds >= 3600:
		hours = TimeCalculator.getHoursOfSeconds(seconds)
		seconds = TimeCalculator.subHoursOfSeconds(seconds, hours)
		output += " " + f'{hours:02d}' + "h"
	
	if seconds >= 60:
		minutes = TimeCalculator.getMinutesOfSeconds(seconds)
		seconds = TimeCalculator.subMinutesOfSeconds(seconds, minutes)
		output += " " + f'{minutes:02d}' + "m"
	
	output += " " + f'{seconds:02d}' + "s"
	
	print(output.strip())
