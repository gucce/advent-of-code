import unittest
import find_sum


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_ = [1721, 979, 366, 299, 675, 1456]

    def test_part1(self):
        self.assertEqual(514579, find_sum.part1(self.input_))

    def test_part2(self):
        self.assertEqual(241861950, find_sum.part2(self.input_))


if __name__ == '__main__':
    unittest.main()
