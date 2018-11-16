#!/usr/bin/env python3
import unittest, inverse_captcha

class TestWordProcessor(unittest.TestCase):

    def test_calc_checksum_comprehension(self):
        # neighbor distance 1
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1), 0)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1122), 3)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1111), 4)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1234), 0)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(91212129), 9)
        # neighbor distance half input size
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1212, 2), 6)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1221, 2), 0)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(123425, 3), 4)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(123123, 3), 12)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(12131415, 4), 4)



    def test_calc_checksum_loop(self):
        # neighbor distance 1
        self.assertEqual(inverse_captcha.calc_checksum_loop(1), 0)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1122), 3)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1111), 4)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1234), 0)
        self.assertEqual(inverse_captcha.calc_checksum_loop(91212129), 9)
        # neighbor distance half input size
        self.assertEqual(inverse_captcha.calc_checksum_loop(1212, 2), 6)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1221, 2), 0)
        self.assertEqual(inverse_captcha.calc_checksum_loop(123425, 3), 4)
        self.assertEqual(inverse_captcha.calc_checksum_loop(123123, 3), 12)
        self.assertEqual(inverse_captcha.calc_checksum_loop(12131415, 4), 4)


if __name__ == '__main__':
    unittest.main()