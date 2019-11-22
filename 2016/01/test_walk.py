#!/usr/bin/env python3
import unittest
import walk


class TestWalk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_ = walk.read_file('input')

    def test_walk_steps_1(self):
        distance = walk.walk_steps(walk.map_input('R2, L3'))
        self.assertEqual(5, distance)

    def test_walk_steps_2(self):
        distance = walk.walk_steps(walk.map_input('R2, R2, R2'))
        self.assertEqual(2, distance)

    def test_walk_steps_3(self):
        distance = walk.walk_steps(walk.map_input('R5, L5, R5, R3'))
        self.assertEqual(12, distance)

    def test_walk_visited_twice(self):
        self.assertEqual(4, walk.walk_steps(walk.map_input('R8, R4, R4, R8', single_steps=True), search_visited_twice=True))

    def test_part1(self):
        self.assertEquals(253, walk.walk_steps(walk.map_input(self.input_)))

    def test_part2(self):
        self.assertEquals(126, walk.walk_steps(walk.map_input(self.input_, single_steps=True), search_visited_twice=True))


if __name__ == '__main__':
    unittest.main()
