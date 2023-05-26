from datetime import datetime, timedelta
from lib.TablePrinter import RowData, TablePrinter, groupRowDataByDateValue

import lib.TimeTrackHelper as TimeTrackHelper
import lib.TimeCalculator as TimeCalculator
import lib.DateHelper as DateHelper

def run(weeksInPast):
	today = datetime.today()
	daysInPast = weeksInPast * 7
	todayInPast = today - timedelta(days=daysInPast)
	
	start = DateHelper.getFirstDayOfWeek(todayInPast)
	end = DateHelper.getLastDayOfWeek(today)

	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	tmpWeek = DateHelper.getWeekOfDate(start)
	minutesForWeek = 0

	weekDataList = []

	day = start
	while day <= end:
		currentWeek = DateHelper.getWeekOfDate(day)
		minutesForDay = TimeTrackHelper.getTrackedMinutesOfDate(day)

		totalTime = TimeTrackHelper.getTrackedMinutesOfDate(day)
		weekDataList.append(RowData(str(currentWeek), totalTime))
		day = day + timedelta(days=1)

	groupedWeekData = groupRowDataByDateValue(weekDataList)

	tablePrinter = TablePrinter("Week")
	tablePrinter.printTable(groupedWeekData)
