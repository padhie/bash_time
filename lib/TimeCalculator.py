import math

def getDaysOfSeconds(seconds):
	days = 0
	if seconds >= 86400:
		days = math.floor(seconds/86400)
	return days

def subDaysOfSeconds(seconds, days):
	return seconds - (days*86400)

def getHoursOfSeconds(seconds):
	hours = 0
	if seconds >= 3600:
		hours = math.floor(seconds/3600)
	return hours

def subHoursOfSeconds(seconds, hours):
	return seconds - (hours*3600)

def getMinutesOfSeconds(seconds):
	minutes = 0
	if seconds >= 60:
		minutes = math.floor(seconds/60)
	return minutes

def subMinutesOfSeconds(seconds, minutes):
	return seconds - (minutes*60)

def getDaysOfMinutes(minutes):
	days = 0
	if minutes >= 60:
		days = math.floor(minutes/3600)
	return days

def subDaysOfMinutes(minutes, days):
	return minutes - (days*3600)

def getHoursOfMinutes(minutes):
	hours = 0
	if minutes >= 60:
		hours = math.floor(minutes/60)
	return hours

def subHoursOfMinutes(minutes, hours):
	return minutes - (hours*60)
