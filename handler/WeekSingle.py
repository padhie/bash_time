from datetime import datetime, timedelta
import lib.TimeTrackHelper as TimeTrackHelper
import lib.TimeCalculator as TimeCalculator
import lib.DateHelper as DateHelper

def run(output):
	dt = datetime.today()
	
	start = DateHelper.getFirstDayOfWeek(dt)
	end = datetime.today()
	
	outputPrefix = ""
	if output == 'large':
		print("Start:", start.strftime("%d.%m.%Y"))
		print("End:", end.strftime("%d.%m.%Y"))
		outputPrefix = "Time: "
		
	minutes = 0
	
	day = start
	while day <= end:
		minutes += TimeTrackHelper.getTrackedMinutesOfDate(day)
		day = day + timedelta(days=1)
	
	days = TimeCalculator.getDaysOfMinutes(minutes)
	minutes = TimeCalculator.subDaysOfMinutes(minutes, days)
	hours = TimeCalculator.getHoursOfMinutes(minutes)
	minutes = TimeCalculator.subHouesOfMinutes(minutes, hours)

	formattedDays = f'{days:02d}'
	formatteDateHelperours = f'{hours:02d}'
	formattedMinutes = f'{minutes:02d}'
	
	formattedTime = ""
	if formattedDays != '00' and formatteDateHelperours != '00':
		formattedTime += "{days}d {hours}h {minutes}m".format(days=formattedDays, hours=formatteDateHelperours, minutes=formattedMinutes)
	elif formattedDays == '00' and formatteDateHelperours != '00':
		formattedTime += "{hours}h {minutes}m".format(hours=formatteDateHelperours, minutes=formattedMinutes)
	elif formattedDays == '00' and formatteDateHelperours == '00':
		formattedTime += "{minutes}m".format(minutes=formattedMinutes)

	print(outputPrefix + formattedTime)
