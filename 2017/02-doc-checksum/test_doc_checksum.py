#!/usr/bin/env python3
import unittest, doc_checksum

class TestWordProcessor(unittest.TestCase):

    def test_calc_doc_checksum_min_max(self):
        test_input = """5 1 9 5
7 5 3
2 4 6 8"""
        self.assertEqual(doc_checksum.calc_doc_checksum_min_max(test_input), 18)


    def test_calc_doc_checksum_division(self):
        test_input = """5 9 2 8
9 4 7 3
3 8 6 5"""
        self.assertEqual(doc_checksum.calc_doc_checksum_division(test_input), 9)


if __name__ == '__main__':
    unittest.main()