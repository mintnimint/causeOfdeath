import unittest
import Main
import os
import xlrd
 
class TestDriven(unittest.TestCase):
 
  def test_workbookShouldNotBeNone(self):
    expect = None
    actual = Main.get_workbook()
    self.assertNotEqual(actual, expect)

  def test_worksheetShouldNotBeNone(self):
    expect = None
    actual = Main.get_worksheet(Main.get_workbook())
    self.assertNotEqual(actual, expect)

  def test_workbookShouldGetData(self):
 		expect = 'Book'
 		actual = Main.get_workbook()
 		self.assertEqual(type(actual).__name__, expect)

  def test_worksheetShouldGetData(self):
 		expect = 'Sheet'
 		actual = Main.get_worksheet(Main.get_workbook())
 		self.assertEqual(type(actual).__name__, expect)

  def test_dataSetShouldBeList(self):
 		expect = 0
 		actual = Main.get_dataset(Main.get_worksheet(Main.get_workbook()))
 		self.assertGreater(len(actual), expect)

  def test_meansmenShouldHaveData(self):
 		expect = (88.3, 55.6, 24.7, 29.0, 22.9, 20.8, 13.5, 10.5, 11.1, 7.2)
 		actual = Main.get_means_men(Main.get_dataset(Main.get_worksheet(Main.get_workbook())), 2009)
 		self.assertEqual(actual, expect)

  def test_barShouldGetColor(self):
 		expect = '#3300FF'
 		actual = Main.get_color(2009)
 		self.assertEqual(actual, expect)

  def test_barWidthShouldGetSize(self):
    expect = 0.15
    actual = Main.get_barWidth('all')
    self.assertEqual(actual, expect)

  def test_labelShouldGetText(self):
    expect = 'Amount'
    actual = Main.get_label('all')
    self.assertEqual(actual, expect)

if __name__ == '__main__':
  unittest.main()