from datetime import datetime, timedelta
import lib.TimeTrackHelper as TimeTrackHelper
import lib.TimeCalculator as TimeCalculator
import lib.DateHelper as DateHelper

formattedTimePattern = "{days}d {hours}h {minutes}m"

def printRow(minutesForWeek, week):
	days = TimeCalculator.getDaysOfMinutes(minutesForWeek)
	minutesForWeek = TimeCalculator.subDaysOfMinutes(minutesForWeek, days)
	
	hours = TimeCalculator.getHoursOfMinutes(minutesForWeek)
	minutesForWeek = TimeCalculator.subHouesOfMinutes(minutesForWeek, hours)
	
	formattedDays = f'{days:02d}'
	formattedHours = f'{hours:02d}'
	formattedMinutes = f'{minutesForWeek:02d}'
	formattedTime = formattedTimePattern.format(days=formattedDays, hours=formattedHours, minutes=formattedMinutes)
	print("| ", f'{week:02d}' , " | ", formattedTime, " |")

def run(weeksInPast):
	today = datetime.today()
	daysInPast = weeksInPast * 7
	todayInPast = today - timedelta(days=daysInPast)
	
	start = DateHelper.getFirstDayOfWeek(todayInPast)
	end = DateHelper.getLastDayOfWeek(today)

	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	print("|- --------------------|")
	print("| Week |  Tracked Time |")
	print("|----------------------|")
	
	tmpWeek = DateHelper.getWeekOfDate(start)
	minutesForWeek = 0
	
	day = start
	while day <= end:
		currentWeek = DateHelper.getWeekOfDate(day)
		if (tmpWeek != currentWeek):
			printRow(minutesForWeek, tmpWeek)

			minutesForWeek = 0
			tmpWeek = currentWeek
			
		minutesForWeek += TimeTrackHelper.getTrackedMinutesOfDate(day)
		day = day + timedelta(days=1)
		
	printRow(minutesForWeek, tmpWeek)
	print("|----------------------|")