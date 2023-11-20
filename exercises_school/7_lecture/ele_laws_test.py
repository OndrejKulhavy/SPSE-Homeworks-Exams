import unittest
from ele_laws import OhmLaw, ColumbLaw


class TestOhmLaw(unittest.TestCase):
    def test_calculate_voltage(self):
        self.assertAlmostEqual(OhmLaw.calculate_voltage(0.002, 1000), 2.0, places=2)

    def test_calculate_current(self):
        self.assertAlmostEqual(OhmLaw.calculate_current(3, 1000), 0.003, places=3)

    def test_calculate_resistance(self):
        self.assertAlmostEqual(OhmLaw.calculate_resistance(3, 0.002), 1500.0, places=1)


class TestColumbLaw(unittest.TestCase):
    def test_calculate_charge(self):
        self.assertAlmostEqual(ColumbLaw.calculate_charge(0.002, 10), 0.02, places=2)



if __name__ == "__main__":
    unittest.main()
