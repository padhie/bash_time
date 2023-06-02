#!/usr/bin/python3

import yaml

from handler import DailyLoginDate
from handler import DailyLoginSince
from handler import WeekTable
from handler import WeekSingle
from handler import LastWeeksTable
from handler import MonthTable
from handler import Help
import lib.CliHelper as CliHelper

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
elif mode == "help":
	Help.run()
else:
	print("unknown mode given")
