#!/usr/bin/env python3
import unittest
import chronal_calibration


class TestStreamParser(unittest.TestCase):


    def test_group_sum(self):
        self.assertEqual(chronal_calibration.string_sum('+1, +1, +1'.split(', ')), 3)
        self.assertEqual(chronal_calibration.string_sum('+1, +1, -2'.split(', ')), 0)
        self.assertEqual(chronal_calibration.string_sum('-1, -2, -3'.split(', ')), -6)


    def test_find_first_duplicate(self):
        self.assertEqual(chronal_calibration.find_first_duplicate('+1, -1'.split(', ')), 0)
        self.assertEqual(chronal_calibration.find_first_duplicate('+3, +3, +4, -2, -4'.split(', ')), 10)
        self.assertEqual(chronal_calibration.find_first_duplicate('-6, +3, +8, +5, -6'.split(', ')), 5)
        self.assertEqual(chronal_calibration.find_first_duplicate('+7, +7, -2, -7, -4'.split(', ')), 14)


if __name__ == '__main__':
    unittest.main()