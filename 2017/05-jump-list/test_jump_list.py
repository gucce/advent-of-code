#!/usr/bin/env python3
import unittest
import jump_list


class TestWordProcessor(unittest.TestCase):

    def test_count_valid_lines_duplicates(self):
        self.assertEqual(jump_list.jump([int(n) for n in '0 3 0 1 -3'.split()], advanced = False), 5)
        self.assertEqual(jump_list.jump([int(n) for n in '0 3 0 1 -3'.split()], advanced = True), 10)


if __name__ == '__main__':
    unittest.main()