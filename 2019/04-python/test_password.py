import unittest
import password


class TestPassword(unittest.TestCase):

    def test_is_valid_passwd(self):
        self.assertEqual(True, password.is_valid_passwd(111111))
        self.assertEqual(False, password.is_valid_passwd(223450))
        self.assertEqual(False, password.is_valid_passwd(123789))
        self.assertEqual(True, password.is_valid_passwd(244444))


if __name__ == '__main__':
    unittest.main()
