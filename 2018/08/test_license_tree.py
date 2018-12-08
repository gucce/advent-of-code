#!/usr/bin/env python3
import unittest
import license_tree

class TestStreamParser(unittest.TestCase):


    def test_sum_metadata(self):
        self.assertEqual(license_tree.sum_metadata('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'), 138)


    def test_root_value(self):
        self.assertEqual(license_tree.root_value('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'), 66)


if __name__ == '__main__':
    unittest.main()