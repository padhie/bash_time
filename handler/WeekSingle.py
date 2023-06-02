from datetime import datetime, timedelta
import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper
import lib.TimeFormatter as TimeFormatter
import lib.BreakTimeCalculator as BreakTimeCalculator

def run(output):
	dt = datetime.today()
	start = DateHelper.getFirstDayOfWeek(dt)
	end = datetime.today()
		
	totalTime = 0
	breakTime = 0

	day = start
	while day <= end:
		minutes = TimeTrackHelper.getTrackedMinutesOfDate(day)

		totalTime += minutes
		breakTime += BreakTimeCalculator.calulcateBreakTime(minutes)

		day = day + timedelta(days=1)

	trackedTime = totalTime - breakTime
	formattedTime = TimeFormatter.formatMinutesInHours(trackedTime)

	if output == 'large':
		print("Start:", start.strftime("%d.%m.%Y"))
		print("End:", end.strftime("%d.%m.%Y"))
		print("Tracked Time:", formattedTime)
		print("Break Time:", TimeFormatter.formatMinutesInHours(breakTime))
		print("Total Time:", TimeFormatter.formatMinutesInHours(totalTime))
	else:
		print(formattedTime)
