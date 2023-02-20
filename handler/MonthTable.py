import calendar
from datetime import datetime, timedelta
import lib.TimeTrackHelper as TimeTrackHelper
import lib.TimeCalculator as TimeCalculator
import lib.DateHelper as DateHelper

formattedTimePattern = "{days}d {hours}h {minutes}m"

def run():
	today = datetime.today()
	
	start = DateHelper.getFirstDayOfMonth(today)
	end = DateHelper.getLastDayOfMonth(today)

	print("Month", calendar.month_name[start.month])
	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	print("+-----------------------+")
	print("| Week  | Tracked Time  |")
	print("+-----------------------+")
	
	tmpWeek = DateHelper.getWeekOfDate(start)
	minutesForWeek = 0
	minutesTotal = 0
	
	day = start
	while day <= end:
		currentWeek = DateHelper.getWeekOfDate(day)
		if (tmpWeek < currentWeek):
			days = TimeCalculator.getDaysOfMinutes(minutesForWeek)
			minutesForWeek = TimeCalculator.subDaysOfMinutes(minutesForWeek, days)
			
			hours = TimeCalculator.getHoursOfMinutes(minutesForWeek)
			minutesForWeek = TimeCalculator.subHouesOfMinutes(minutesForWeek, hours)
			
			formattedDays = f'{days:02d}'
			formatteDateHelperours = f'{hours:02d}'
			formattedMinutes = f'{minutesForWeek:02d}'
			formattedTime = formattedTimePattern.format(days=formattedDays, hours=formatteDateHelperours, minutes=formattedMinutes)
			print("|  ", f'{tmpWeek:02d}' , " | ", formattedTime, " |")
			
			minutesForWeek = 0
			tmpWeek = currentWeek
			
		minutesForWeek += TimeTrackHelper.getTrackedMinutesOfDate(day)
		minutesTotal += minutesForWeek
		day = day + timedelta(days=1)

	print("+-----------------------+")	

	days = 0
	hours = 0
	minutes = 0

	if minutesTotal != 0:
			days = TimeCalculator.getDaysOfMinutes(minutesTotal)
			minutesTotal = TimeCalculator.subDaysOfMinutes(minutesTotal, days)
			
			hours = TimeCalculator.getHoursOfMinutes(minutesTotal)
			minutesTotal = TimeCalculator.subHouesOfMinutes(minutesTotal, hours)

	formattedDays = f'{days:02d}'
	formatteDateHelperours = f'{hours:02d}'
	formattedMinutes = f'{minutesTotal:02d}'
	formattedTime = formattedTimePattern.format(days=formattedDays, hours=formatteDateHelperours, minutes=formattedMinutes)
	print("| Total | ", formattedTime, " |")
	
	print("+-----------------------+")