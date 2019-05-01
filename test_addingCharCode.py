from addingCharCode import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(97, addingCharCode('a'))
    def test_2(self):
        self.assertEqual(98, addingCharCode('b'))
    def test_3(self):
        self.assertEqual(65, addingCharCode('A'))
    def test_4(self):
        self.assertEqual(417, addingCharCode('ifpb'))
    def test_5(self):
        self.assertEqual(543, addingCharCode('lorem'))
    def test_6(self):
        self.assertEqual(1133, addingCharCode('lorem ipsum'))

unittest.main()
