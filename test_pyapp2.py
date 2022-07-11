import gui
import unittest
import datetimechecker

class TestApp(unittest.TestCase):
	def testCase1(self):
		result = gui.testApp(11,12,12)
		self.assertEqual(result, False)
		
	def testCase2(self):
		result = gui.testApp(11,12,2021)
		self.assertEqual(result, True)

	def testCase3(self):
		result = gui.testApp(11,13,1200)
		self.assertEqual(result, False)

	def testCase4(self):
		result = gui.testApp(32,12,1221)
		self.assertEqual(result, False)
		
if __name__ == '__main__':
	unittest.main()
	