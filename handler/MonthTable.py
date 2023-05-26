from datetime import datetime, timedelta
from lib.TablePrinter import RowData, TablePrinter, groupRowDataByDateValue

import calendar
import lib.TimeTrackHelper as TimeTrackHelper
import lib.DateHelper as DateHelper

def run():
	today = datetime.today()
	start = DateHelper.getFirstDayOfMonth(today)
	end = DateHelper.getLastDayOfMonth(today)

	print("Month", calendar.month_name[start.month])
	print("Start:", start.strftime("%d.%m.%Y"))
	print("End:", end.strftime("%d.%m.%Y"))
	print()
	
	weekDataList = []

	day = start
	while day <= end:
		currentWeek = DateHelper.getWeekOfDate(day)
		minutesForDay = TimeTrackHelper.getTrackedMinutesOfDate(day)

		weekDataList.append(RowData(str(currentWeek), minutesForDay))
		day = day + timedelta(days=1)

	groupedWeekData = groupRowDataByDateValue(weekDataList)

	tablePrinter = TablePrinter("Week")
	tablePrinter.printTable(groupedWeekData)