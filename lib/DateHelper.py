import calendar
from datetime import timedelta

def getWeekOfDate(dt):
	return dt.isocalendar()[1]

def getFirstDayOfWeek(dt):
	return dt - timedelta(days=dt.weekday())

def getLastDayOfWeek(dt):
	return getFirstDayOfWeek(dt) + timedelta(days=6)

def getFirstDayOfMonth(dt):
	return dt.replace(day=1)

def getLastDayOfMonth(dt):
	monthRange = calendar.monthrange(dt.year, dt.month)
	return dt.replace(day=monthRange[1])
