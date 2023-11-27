"""
Napište unit test pro metodu z příkladu 11.1, který zkontroluje, že metoda nesčítá co sčítat nemá.
Metoda má sčítat pouze čísla, tedy ne stringy, ne třídy, kolekce apod.
"""

import unittest

from exercise_1 import add


class TestAdd(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_float(self):
        self.assertEqual(add(1.0, 2.0), 3.0)

    def test_add_complex(self):
        self.assertEqual(add(1 + 1j, 2 + 2j), 3 + 3j)

    def test_add_str(self):
        self.assertRaises(TypeError, add, "1", "2")

