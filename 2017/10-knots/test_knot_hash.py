#!/usr/bin/env python3
import unittest
import knot_hash


class TestKnotHash(unittest.TestCase):

    def test_group_sum(self):
        hash = knot_hash.hash([0, 1, 2, 3, 4], [3, 4, 1, 5])
        self.assertEqual(hash[0] * hash[1], 12)


if __name__ == '__main__':
    unittest.main()