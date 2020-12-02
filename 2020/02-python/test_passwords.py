import unittest
import passwords as p


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_ = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.splitlines()

    def test_part1(self):
        self.assertEqual(2, p.part1(p.map_input(self.input_)))

    def test_part2(self):
        self.assertEqual(1, p.part2(p.map_input(self.input_)))


if __name__ == '__main__':
    unittest.main()
