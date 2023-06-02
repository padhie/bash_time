import yaml
import os

class Config:
    breakList = []

class Break:
    def __init__(self, time, breakTime):
        self.time = time
        self.breakTime = breakTime

def loadConfig():
    configObject = Config()
    configFile = getAbsoluteConfigFile()

    if os.path.isfile(configFile) != True:
        return configObject

    with open(configFile, "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    for breakConfig in config["break"]:
        breakItem = Break(breakConfig["time"], breakConfig["break"])
        configObject.breakList.append(breakItem)

    return configObject

def getAbsoluteConfigFile():
    absoluteConfigFile = os.path.dirname(os.path.abspath(__file__)) + "/../config.yaml"
    normalizedAbsoluteConfigFile = os.path.normpath(absoluteConfigFile)

    return normalizedAbsoluteConfigFile
