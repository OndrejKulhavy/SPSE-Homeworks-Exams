"""
Přepište zadání úlohy 5.1. do formy unit testu a následně otestujte svůj vlastní kód z kapitoly 5.1.
a upravte buď test nebo kód tak, aby vše dopadlo tak jak má.
Nezpomeňte testovat nejen to co kód má dělat, ale i to , že nedělá to, co dělat nemá.
"""

import unittest
from exercise_3 import Bottle

class TestBottle(unittest.TestCase):
    def setUp(self):
        self.bottle = Bottle(2.0)

    def test_fill(self):
        self.bottle.fill(1.0)
        self.assertEqual(self.bottle.filled_liters, 1.0)

        with self.assertRaises(ValueError):
            self.bottle.fill(2.0)

        self.bottle.close()
        with self.assertRaises(ValueError):
            self.bottle.fill(0.5)

    def test_pour(self):
        self.bottle.fill(1.0)
        self.bottle.pour(0.5)
        self.assertEqual(self.bottle.filled_liters, 0.5)

        with self.assertRaises(ValueError):
            self.bottle.pour(1.0)

        self.bottle.close()
        with self.assertRaises(ValueError):
            self.bottle.pour(0.1)

    def test_get_volume_milliliters(self):
        self.bottle.fill(1.0)  # fill 1 liter
        self.assertEqual(self.bottle.get_volume_milliliters(), 1000.0)

    def test_close_open(self):
        self.bottle.close()
        self.assertTrue(self.bottle.isClosed)

        self.bottle.open()
        self.assertFalse(self.bottle.isClosed)