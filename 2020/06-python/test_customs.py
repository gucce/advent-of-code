import unittest
import customs as c


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_ = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

    def test_part1(self):
        self.assertEqual(11, c.part1(c.map_input(self.input_)))

    def test_part2(self):
        self.assertEqual(6, c.part2(c.map_input(self.input_)))


if __name__ == '__main__':
    unittest.main()
