#!/usr/bin/env python3
import unittest
import mass


class TestWalk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_ = mass.read_file('input')

    def test_calc_mass(self):
        self.assertEqual(2, mass.calc_fuel_for_mass(12))
        self.assertEqual(2, mass.calc_fuel_for_mass(14))
        self.assertEqual(654, mass.calc_fuel_for_mass(1969))
        self.assertEqual(33583, mass.calc_fuel_for_mass(100756))

    def test_calc_mass_recursive(self):
        self.assertEqual(2, mass.calc_fuel_for_mass_recursive(12))
        self.assertEqual(966, mass.calc_fuel_for_mass_recursive(1969))
        self.assertEqual(50346, mass.calc_fuel_for_mass_recursive(100756))

    def test_part1(self):
        self.assertEquals(3173518, mass.calc_fuel_for_modules(mass.map_input(self.input_), mass.calc_fuel_for_mass))

    def test_part2(self):
        self.assertEquals(4757427,
                          mass.calc_fuel_for_modules(mass.map_input(self.input_), mass.calc_fuel_for_mass_recursive))


if __name__ == '__main__':
    unittest.main()
