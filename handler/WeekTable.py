from datetime import datetime, timedelta
from lib.TablePrinter import RowData, TablePrinter, groupRowDataByDateValue

import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper
import lib.BreakTimeCalculator as BreakTimeCalculator

def run():
	dt = datetime.today()
	
	week = DateHelper.getWeekOfDate(dt)
	start = DateHelper.getFirstDayOfWeek(dt)
	end = DateHelper.getLastDayOfWeek(dt)

	print("Week", week)
	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()

	weekDataList = []

	day = start
	while day <= end:
		hours = 0
		minutes = 0
		
		minutesOfDay = TimeTrackHelper.getTrackedMinutesOfDate(day)
		formattedDate = day.strftime("%d.%m.%Y")

		breakTime = BreakTimeCalculator.calulcateBreakTime(minutesOfDay)
		row = RowData(str(formattedDate), breakTime, minutesOfDay)
		weekDataList.append(row)
		day = day + timedelta(days=1)

	groupedWeekData = groupRowDataByDateValue(weekDataList)

	tablePrinter = TablePrinter("Date")
	tablePrinter.printTable(groupedWeekData)