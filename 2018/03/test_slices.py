#!/usr/bin/env python3
import unittest
import slices

class TestStreamParser(unittest.TestCase):


    def test_parse_rectangle(self):
        self.assertEqual(slices.parse_rectangle('#1 @ 935,649: 22x22'), slices.Rectangle(id = 1, min_x = 935, max_x = 957, min_y = 649, max_y = 671))


if __name__ == '__main__':
    unittest.main()