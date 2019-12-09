import unittest
import layers


class TestLayers(unittest.TestCase):

    def test_part1(self):
        input_ = '0222112222120000'
        digits = layers.map_input(input_)
        self.assertEqual([0, 1, 1, 0], layers.part2(digits, 2, 2))


if __name__ == '__main__':
    unittest.main()
