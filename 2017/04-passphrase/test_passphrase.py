#!/usr/bin/env python3
import unittest
import passphrase


class TestWordProcessor(unittest.TestCase):

    def test_count_valid_lines_duplicates(self):
        self.assertEqual(passphrase.count_valid_lines_duplicates('aa bb cc dd ee'), 1)
        self.assertEqual(passphrase.count_valid_lines_duplicates('aa bb cc dd aa'), 0)
        self.assertEqual(passphrase.count_valid_lines_duplicates('aa bb cc dd aaa'), 1)


    def test_count_valid_lines_anagrams(self):
        self.assertEqual(passphrase.count_valid_lines_anagrams('abcde fghij'), 1)
        self.assertEqual(passphrase.count_valid_lines_anagrams('abcde xyz ecdab'), 0)
        self.assertEqual(passphrase.count_valid_lines_anagrams('a ab abc abd abf abj'), 1)
        self.assertEqual(passphrase.count_valid_lines_anagrams('iiii oiii ooii oooi oooo'), 1)
        self.assertEqual(passphrase.count_valid_lines_anagrams('oiii ioii iioi iiio'), 0)


if __name__ == '__main__':
    unittest.main()