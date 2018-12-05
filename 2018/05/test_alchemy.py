#!/usr/bin/env python3
import unittest
import alchemy

class TestStreamParser(unittest.TestCase):


    def test_reduce_chain(self):
        self.assertEqual(alchemy.reduce_chain('dabAcCaCBAcCcaDA'), 'dabCBAcaDA')


if __name__ == '__main__':
    unittest.main()