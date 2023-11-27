"""
Napište unit test pro metodu add(a, b) která má sčítat čísla.
Ověřte, zda-li správně sčítá celá čísla, desetinná čísla a komplexní čísla.
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
