import unittest
import find_sum


class TestLayers(unittest.TestCase):

    def test_part1(self):
        input_ = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(514579, find_sum.part1(input_))


if __name__ == '__main__':
    unittest.main()
