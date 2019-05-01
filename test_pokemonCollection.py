from pokemonCollection import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(150, pokemonCollection(['Zubat']))
    def test_2(self):
        self.assertEqual(150, pokemonCollection(['Zubat', 'Zubat', 'Zubat', 'Zubat', 'Zubat', 'Zubat', 'Zubat', 'Zubat']))
    def test_3(self):
        self.assertEqual(149, pokemonCollection(['Zubat', 'Pikachu', 'Pikachu']))
    def test_4(self):
        self.assertEqual(147, pokemonCollection(['Zubat', 'Charmander', 'Caterpie', 'Pidgeot']))
    def test_5(self):
        self.assertEqual(146, pokemonCollection(['Charmander', 'Caterpie', 'Pidgeot', 'Rattata', 'Zubat', 'Zubat', 'Zubat']))

unittest.main()
