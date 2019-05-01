from sortLibrary import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(['1000', '2000', '3000'], sortLibrary(['3000', '2000', '1000']))
    def test_2(self):
        self.assertEqual(['0015', '0100', '1233'], sortLibrary(['1233', '0015', '0100']))
    def test_3(self):
        self.assertEqual(['0000', '0001', '0752', '1110', '6321', '6322', '8000'], sortLibrary(['0752', '1110', '0001', '6322', '8000', '6321', '0000']))

unittest.main()
