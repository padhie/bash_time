def fillString(message, maxLength, fillChar):
	message = str(message)
	if len(message) >= maxLength:
		return message

	needToFill = maxLength - len(message)
	fillBySite = needToFill / 2

	tmpMessage = ""
	while(len(tmpMessage) < fillBySite):
		tmpMessage += fillChar

	tmpMessage += message

	while(len(tmpMessage) < maxLength):
		tmpMessage += fillChar

	return tmpMessage