import unittest
import password


class TestPassword(unittest.TestCase):

    def test_is_valid_passwd(self):
        self.assertEqual(True, password.is_valid_passwd(111111))
        self.assertEqual(False, password.is_valid_passwd(223450))
        self.assertEqual(False, password.is_valid_passwd(123789))
        self.assertEqual(True, password.is_valid_passwd(244444))

    def test_is_valid_passwd_part2(self):
        self.assertEqual(True, password.is_valid_passwd(112233, part2=True))
        self.assertEqual(False, password.is_valid_passwd(123444, part2=True))
        self.assertEqual(True, password.is_valid_passwd(111122, part2=True))
        self.assertEqual(True, password.is_valid_passwd(112222, part2=True))
        self.assertEqual(False, password.is_valid_passwd(777999, part2=True))


if __name__ == '__main__':
    unittest.main()
