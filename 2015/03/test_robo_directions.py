import unittest
import robo_directions as r


class TestDayTwo(unittest.TestCase):
    def test_case_part_one(self):
        self.assertEqual(2, r.part_one(">"))
        self.assertEqual(4, r.part_one("^>v<"))
        self.assertEqual(2, r.part_one("^v^v^v^v^v"))

    def test_case_part_two(self):
        self.assertEqual(3, r.part_two("^v"))
        self.assertEqual(3, r.part_two("^>v<"))
        self.assertEqual(11, r.part_two("^v^v^v^v^v"))


if __name__ == '__main__':
    unittest.main()
