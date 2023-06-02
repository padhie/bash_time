import unittest
from lib.TablePrinter import RowData, groupRowDataByDateValue

class GroupRowDataByDateValueTest(unittest.TestCase):
    def test_groupRowDataByDateValue(self):
        list = []
        list.append(RowData("a", 10, 20))
        list.append(RowData("a", 20, 30))
        list.append(RowData("b", 30, 40))
        list.append(RowData("b", 40, 50))

        groupedRowData = groupRowDataByDateValue(list)

        self.assertEqual(2, len(groupedRowData))
        self.assertEqual("a", groupedRowData[0].dateValue)
        self.assertEqual(30, groupedRowData[0].breakTime)
        self.assertEqual(50, groupedRowData[0].totalTime)
        self.assertEqual("b", groupedRowData[1].dateValue)
        self.assertEqual(70, groupedRowData[1].breakTime)
        self.assertEqual(90, groupedRowData[1].totalTime)

if __name__ == '__main__':
    unittest.main()