from datetime import datetime, timedelta

import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper
import lib.TimeFormatter as TimeFormatter
import lib.BreakTimeCalculator as BreakTimeCalculator

def run():
	today = datetime.today()

	totalTime = TimeTrackHelper.getTrackedMinutesOfDate(today)
	breakTime = BreakTimeCalculator.calulcateBreakTime(totalTime)

	trackedTime = totalTime - breakTime
	formattedTime = TimeFormatter.formatMinutesInHours(trackedTime)

	print(formattedTime)
