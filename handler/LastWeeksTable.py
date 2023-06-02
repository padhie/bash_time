from datetime import datetime, timedelta
from lib.TablePrinter import RowData, TablePrinter, groupRowDataByDateValue

import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper
import lib.BreakTimeCalculator as BreakTimeCalculator

def run(weeksInPast):
	today = datetime.today()
	daysInPast = weeksInPast * 7
	todayInPast = today - timedelta(days=daysInPast)
	
	start = DateHelper.getFirstDayOfWeek(todayInPast)
	end = DateHelper.getLastDayOfWeek(today)

	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	weekDataList = []

	day = start
	while day <= end:
		currentWeek = DateHelper.getWeekOfDate(day)
		minutesForDay = TimeTrackHelper.getTrackedMinutesOfDate(day)

		totalTime = TimeTrackHelper.getTrackedMinutesOfDate(day)
		breakTime = BreakTimeCalculator.calulcateBreakTime(totalTime)
		weekDataList.append(RowData(str(currentWeek), breakTime, totalTime))
		day = day + timedelta(days=1)

	groupedWeekData = groupRowDataByDateValue(weekDataList)

	tablePrinter = TablePrinter("Week")
	tablePrinter.printTable(groupedWeekData)
