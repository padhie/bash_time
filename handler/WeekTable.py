from datetime import datetime, timedelta
from lib.TablePrinter import RowData, TablePrinter, groupRowDataByDateValue

import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper

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

		weekDataList.append(RowData(str(formattedDate), minutesOfDay))
		day = day + timedelta(days=1)

	groupedWeekData = groupRowDataByDateValue(weekDataList)

	tablePrinter = TablePrinter("Date")
	tablePrinter.printTable(groupedWeekData)