import unittest
import xmas as x


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''

    def test_map_input(self):
        self.assertEqual(20, len(x.map_input(self.input_data)))

    def test_part1(self):
        self.assertEqual(127, x.part1(x.map_input(self.input_data), 5))

    def test_part2(self):
        self.assertEqual(62, x.part2(x.map_input(self.input_data), 127))


if __name__ == '__main__':
    unittest.main()
