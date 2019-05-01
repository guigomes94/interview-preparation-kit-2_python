from birthdayCakeCandles import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, birthdayCakeCandles([1, 1, 1, 3]))

    def test_2(self):
        self.assertEqual(2, birthdayCakeCandles([1, 3, 1, 3]))

    def test_3(self):
        self.assertEqual(3, birthdayCakeCandles([1, 3, 3, 3]))

    def test_4(self):
        self.assertEqual(2, birthdayCakeCandles([3, 2, 1, 3]))

    def test_5(self):
        self.assertEqual(5, birthdayCakeCandles([18, 90, 90, 13, 90, 75, 90, 8, 90, 43]))

unittest.main()
