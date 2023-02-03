import os

def getApplicationDir():
	return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getDataDir():
	return getApplicationDir() + "/data"