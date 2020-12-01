import unittest
import santa_directions as sd


class TestDayOne(unittest.TestCase):
    def test_case_part_one(self):
        self.assertEqual(0, sd.part_one("(())"))
        self.assertEqual(0, sd.part_one("()()"))
        self.assertEqual(3, sd.part_one("((("))
        self.assertEqual(3, sd.part_one("(()(()("))

    def test_case_part_two(self):
        self.assertEqual(1, sd.part_two(")"))
        self.assertEqual(5, sd.part_two("()())"))


if __name__ == '__main__':
    unittest.main()
