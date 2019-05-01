from hackerrankInString import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual('YES', hackerrankInString('hereiamstackerrank'))

    def test_2(self):
        self.assertEqual('NO', hackerrankInString('hackerworld'))

    def test_3(self):
        self.assertEqual('YES', hackerrankInString('hhaacckkekraraannk'))

    def test_4(self):
        self.assertEqual('NO', hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))

unittest.main()
