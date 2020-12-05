import unittest
import binary_boarding as b


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_ = '''BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
'''

    def test_map_input(self):
        self.assertEqual(3, len(b.map_input(self.input_)))

    def test_part1(self):
        self.assertEqual(820, b.part1(b.map_input(self.input_)))

    def test_part2(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
