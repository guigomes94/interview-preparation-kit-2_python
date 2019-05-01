from countingValleys import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, countingValleys('DU'))

    def test_2(self):
        self.assertEqual(2, countingValleys('DUDU'))

    def test_3(self):
        self.assertEqual(0, countingValleys('UUUDU'))

    def test_4(self):
        self.assertEqual(1, countingValleys('UDDDUDUU'))

    def test_5(self):
        self.assertEqual(2, countingValleys('DDUUDDUDUUUD'))

unittest.main()
