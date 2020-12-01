import unittest
import presents as p


class TestDayTwo(unittest.TestCase):
    def test_case_part_one(self):
        self.assertEqual(58, p.part_one([[2, 3, 4]]))
        self.assertEqual(43, p.part_one([[1, 1, 10]]))

    def test_case_part_two(self):
        self.assertEqual(34, p.part_two([[2, 3, 4]]))
        self.assertEqual(14, p.part_two([[1, 1, 10]]))
        self.assertEqual(48, p.part_two([[2, 3, 4], [1, 1, 10]]))


if __name__ == '__main__':
    unittest.main()
