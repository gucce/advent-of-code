#!/usr/bin/env python3
import unittest, spiral_grid

class TestWordProcessor(unittest.TestCase):

    def test_distance_for_num(self):
        self.assertEqual(spiral_grid.distance_for_num(1), 0)
        self.assertEqual(spiral_grid.distance_for_num(12),3)
        self.assertEqual(spiral_grid.distance_for_num(23), 2)
        self.assertEqual(spiral_grid.distance_for_num(1024), 31)
        self.assertEqual(spiral_grid.distance_for_num(265149), 438)


if __name__ == '__main__':
    unittest.main()