import sys

def getArg(index):
	args = sys.argv
	if len(args) < (index+1):
		return None
	
	return args[index]