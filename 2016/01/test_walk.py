#!/usr/bin/env python3
import unittest
import walk


class TestKnotHash(unittest.TestCase):
    def test_walk_steps_1(self):
        distance = walk.walk_steps(walk.map_input('R2, L3'))
        self.assertEqual(5, distance)

    def test_walk_steps_2(self):
        distance = walk.walk_steps(walk.map_input('R2, R2, R2'))
        self.assertEqual(2, distance)

    def test_walk_steps_3(self):
        distance = walk.walk_steps(walk.map_input('R5, L5, R5, R3'))
        self.assertEqual(12, distance)


if __name__ == '__main__':
    unittest.main()
