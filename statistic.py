from handler import DailyLoginDate
from handler import DailyLoginSince
from handler import WeekTable
from handler import WeekSingle
from handler import LastWeeksTable
from handler import MonthTable
import lib.CliHelper as CliHelper

def printAvailableModes():
	print("available modes:")
	print("    daily-login-date                 print the absolute time of the first tracked time")
	print("    daily-login-since                print the relative time of the first tracked time")
	print("    week-single [large|normal]       print the statistic of the current week")
	print("        large                            print start date, end date, days, hours, minutes")
	print("        normal (default)                 print days, hours, minutes")
	print("    week-table                       print the statistic of the current week in table layout")
	print("    month-table                      print the statistic of the current month in table layout")
	print("    last-weeks-table weeks           print the statistic of the last given week in table layout")

mode = CliHelper.getArg(1)
additionalArg = CliHelper.getArg(2)

if mode is None:
	print("missing argument")
	printAvailableModes()
	exit(1)

if mode == "daily-login-date":
	DailyLoginDate.run()
elif mode == "daily-login-since":
	DailyLoginSince.run()
elif mode == "week-table":
	WeekTable.run()
elif mode == "week-single":
	if additionalArg is None:
		additionalArg = 'normal'
	WeekSingle.run(additionalArg)
elif mode == "month-table":
	MonthTable.run()
elif mode == "last-weeks-table":
	if additionalArg is None:
		print("no weeks given")
	else:
		LastWeeksTable.run(int(additionalArg))
else:
	print("unknown mode given")
	printAvailableModes()
