from countApplesAndOranges import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual([1, 0], countApplesAndOranges(5, 10, 0, 15, [0, 3, 6], [17, 20]))
    def test_2(self):
        self.assertEqual([1, 1], countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]))
    def test_3(self):
        self.assertEqual([1, 0], countApplesAndOranges(8, 9, -1, 15, [-2, 2, 10], [20, 21]))

unittest.main()

