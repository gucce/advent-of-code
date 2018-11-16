#!/usr/bin/env python3
import unittest, inverse_captcha

class TestWordProcessor(unittest.TestCase):

    def test_calc_checksum_comprehension(self):
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1), 0)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1122), 3)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1111), 4)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(1234), 0)
        self.assertEqual(inverse_captcha.calc_checksum_comprehension(91212129), 9)


    def test_calc_checksum_loop(self):
        self.assertEqual(inverse_captcha.calc_checksum_loop(1), 0)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1122), 3)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1111), 4)
        self.assertEqual(inverse_captcha.calc_checksum_loop(1234), 0)
        self.assertEqual(inverse_captcha.calc_checksum_loop(91212129), 9)


if __name__ == '__main__':
    unittest.main()