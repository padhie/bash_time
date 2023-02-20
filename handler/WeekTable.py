from datetime import datetime, timedelta
import lib.TimeTrackHelper as TimeTrackHelper
import lib.TimeCalculator as TimeCalculator
import lib.DateHelper as DateHelper

formattedTimePattern = "{hours}h {minutes}m"

def run():
	dt = datetime.today()
	
	week = DateHelper.getWeekOfDate(dt)
	start = DateHelper.getFirstDayOfWeek(dt)
	end = DateHelper.getLastDayOfWeek(dt)
	minutesTotal = 0
	
	print("Week", week)
	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	print("+---------------------------+")
	print("|    Date    | Tracked Time |")
	print("+---------------------------+")
	day = start
	while day <= end:
		hours = 0
		minutes = 0
		
		minutesOfDay = TimeTrackHelper.getTrackedMinutesOfDate(day)
		minutesTotal += minutesOfDay
		if minutesOfDay != 0:
			hours = TimeCalculator.getHoursOfMinutes(minutesOfDay)
			minutes = TimeCalculator.subHouesOfMinutes(minutesOfDay, hours)
	
		formatteDateHelperours = f'{hours:02d}'
		formattedMinutes = f'{minutes:02d}'
		formattedTime = formattedTimePattern.format(hours=formatteDateHelperours, minutes=formattedMinutes)
		
		formattedDate = day.strftime("%d.%m.%Y")

		print("|", formattedDate , "|   ", formattedTime, "  |")
		
		day = day + timedelta(days=1)
	
	print("+---------------------------+")

	hours = 0
	minutes = 0
	
	if minutesTotal != 0:
		hours = TimeCalculator.getHoursOfMinutes(minutesTotal)
		minutes = TimeCalculator.subHouesOfMinutes(minutesTotal, hours)

	formatteDateHelperours = f'{hours:02d}'
	formattedMinutes = f'{minutes:02d}'
	formattedTime = formattedTimePattern.format(hours=formatteDateHelperours, minutes=formattedMinutes)
	print("|    Total   |   ", formattedTime, "  |")
	print("+---------------------------+")