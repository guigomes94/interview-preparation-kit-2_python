from compareTheTriplets import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual([3, 0], compareTheTriplets(1, 1, 1, 0, 0, 0))

    def test_2(self):
        self.assertEqual([0, 3], compareTheTriplets(0, 0, 0, 1, 1, 1))

    def test_3(self):
        self.assertEqual([2, 1], compareTheTriplets(17, 28, 30, 99, 16, 8))

    def test_4(self):
        self.assertEqual([1, 1], compareTheTriplets(5, 6, 7, 3, 6, 10))

unittest.main()
