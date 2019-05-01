from catAndMouse import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual('Cat B', catAndMouse(1, 2, 3))

    def test_2(self):
        self.assertEqual('Mouse C', catAndMouse(1, 3, 2))

    def test_3(self):
        self.assertEqual('Cat A', catAndMouse(1, 4, 2))

unittest.main()
