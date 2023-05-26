import lib.StringFiller as StringFiller
import lib.TimeFormatter as TimeFormatter

class RowData:
    def __init__(self, dateValue, totalTime, breakTime):
        self.dateValue = dateValue
        self.totalTime = totalTime
        self.breakTime = breakTime

class Length:
    maxLengthDateColumn = 0
    maxLengthBreakTime = len("Break Time")
    maxLengthTotalTime = len("Total Time")

class TablePrinter:
    def __init__(self, firstColumnName):
        self.maxLength = Length()
        self.firstColumnName = firstColumnName
        self.maxLengthOfFirstColumn = len(firstColumnName)

    def printTable(self, rowDataList):
        self.maxLength = Length()
        self.maxLength.maxLengthDateColumn = len(self.firstColumnName)

        totalRowData = RowData("Total", 0, 0)

        for rowData in rowDataList:
            currentLengthOfFirstColumn = len(rowData.dateValue)
            if currentLengthOfFirstColumn > self.maxLength.maxLengthDateColumn:
                self.maxLength.maxLengthDateColumn = currentLengthOfFirstColumn

            currentLengthOfBreakTime = len(str(rowData.breakTime))
            if currentLengthOfBreakTime > self.maxLength.maxLengthBreakTime:
                self.maxLength.maxLengthBreakTime = currentLengthOfBreakTime

            totalRowData.breakTime += rowData.breakTime
            totalRowData.totalTime += rowData.totalTime

        if totalRowData.breakTime > self.maxLength.maxLengthBreakTime:
            self.maxLength.maxLengthBreakTime = totalRowData.breakTime

        self.printHeadline()
        for rowData in rowDataList:
            self.printRow(rowData)
        self.printTotalLine(totalRowData)

    def printHeadline(self):
        firstColumnNameToDisplay = StringFiller.fillString(self.firstColumnName, self.maxLength.maxLengthDateColumn+2, " ")
        firstColumnNameDelimiterFiller = StringFiller.fillString("", self.maxLength.maxLengthDateColumn+2, "-")

        print("+" + firstColumnNameDelimiterFiller + "-----------------------------------------+")
        print("|" + firstColumnNameToDisplay + "| Tracked Time | Break Time | Total Time |")
        print("+" + firstColumnNameDelimiterFiller + "-----------------------------------------+")

    def printTotalLine(self, rowData):
        firstColumnName = "Total"
        firstColumnNameToDisplay = StringFiller.fillString(firstColumnName, self.maxLength.maxLengthDateColumn+2, " ")
        firstColumnNameDelimiterFiller = StringFiller.fillString("", self.maxLength.maxLengthDateColumn+2, "-")

        print("+" + firstColumnNameDelimiterFiller + "-----------------------------------------+")
        self.printRow(rowData)
        print("+" + firstColumnNameDelimiterFiller + "-----------------------------------------+")

    def printRow(self, rowData):
        firstColumnName = ""
        firstColumnNameToDisplay = StringFiller.fillString(rowData.dateValue, self.maxLength.maxLengthDateColumn+2, " ")

        formattedTotalTime = TimeFormatter.formatMinutesInHours(rowData.totalTime)
        totalTimeToDisplay = StringFiller.fillString(formattedTotalTime, self.maxLength.maxLengthTotalTime+2, " ")

        if rowData.breakTime > 60:
            formattedBreakTime = TimeFormatter.formatMinutesInHours(rowData.breakTime)
        else:
            formattedBreakTime = TimeFormatter.formatMinutes(rowData.breakTime)
        breakTimeToDisplay = StringFiller.fillString(formattedBreakTime, self.maxLength.maxLengthTotalTime+2, " ")

        trackedTime = rowData.totalTime - rowData.breakTime
        formattedTrackedTime = TimeFormatter.formatMinutesInHours(trackedTime)
        trackedTimeToDisplay = StringFiller.fillString(formattedTrackedTime, 14, " ")

        print("|" + firstColumnNameToDisplay + "|" + trackedTimeToDisplay + "|" + breakTimeToDisplay + "|" + totalTimeToDisplay + "|")
