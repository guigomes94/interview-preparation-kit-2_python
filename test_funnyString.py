from funnyString import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual('Funny', funnyString('abc'))

    def test_2(self):
        self.assertEqual('Not Funny', funnyString('abd'))

    def test_3(self):
        self.assertEqual('Funny', funnyString('acxz'))

    def test_4(self):
        self.assertEqual('Not Funny', funnyString('bcxz'))

unittest.main()
