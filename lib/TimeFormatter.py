import lib.TimeCalculator as TimeCalculator

def formatMinutesInHours(minutesTotal):
    hours = 0
    minutes = 0

    minutesInternal = minutesTotal
    if minutesInternal != 0:
        hours = TimeCalculator.getHoursOfMinutes(minutesInternal)
        minutesInternal = TimeCalculator.subHoursOfMinutes(minutesInternal, hours)

    formattedDateHelperHours = f'{hours:02d}'
    formattedMinutes = f'{minutesInternal:02d}'
    formattedTime = "{hours}h {minutes}m".format(hours=formattedDateHelperHours, minutes=formattedMinutes)

    return formattedTime

def formatMinutes(minutesTotal):
    formattedMinutes = f'{minutesTotal:02d}'
    formattedTime = "{minutes}m".format(minutes=formattedMinutes)

    return formattedTime