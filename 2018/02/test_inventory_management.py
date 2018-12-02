#!/usr/bin/env python3
import unittest
import inventory_management


class TestStreamParser(unittest.TestCase):


    def test_count_letter_groups(self):
        self.assertEqual(inventory_management.count_letter_groups('abcdef'), (0, 0))
        self.assertEqual(inventory_management.count_letter_groups('bababc'), (1, 1))
        self.assertEqual(inventory_management.count_letter_groups('abbcde'), (1, 0))
        self.assertEqual(inventory_management.count_letter_groups('abcccd'), (0, 1))
        self.assertEqual(inventory_management.count_letter_groups('aabcdd'), (1, 0))
        self.assertEqual(inventory_management.count_letter_groups('abcdee'), (1, 0))
        self.assertEqual(inventory_management.count_letter_groups('ababab'), (0, 1))


    def test_letter_checksum(self):
        input = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
        self.assertEqual(inventory_management.letter_checksum(input.splitlines()), 12)


    def test_check_similarity(self):
        self.assertEqual(inventory_management.check_similarity('abc', 'abd'), 'ab')
        self.assertEqual(inventory_management.check_similarity('fghij', 'fguij'), 'fgij')
        self.assertEqual(inventory_management.check_similarity('abc', 'adf'), False)


if __name__ == '__main__':
    unittest.main()