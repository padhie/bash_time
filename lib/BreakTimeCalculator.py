import lib.ConfigLoader as ConfigLoader

def calulcateBreakTime(time):
    config = ConfigLoader.loadConfig()
    breakConfigList = sorted(config.breakList, key=lambda d: d.breakTime, reverse=True)

    for breakConfig in breakConfigList:
        if time >= breakConfig.time:
            return breakConfig.breakTime

    return 0