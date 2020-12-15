import unittest
import game as g


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''0,3,6'''
        self.input_data_part2 = ''''''

    def test_part1(self):
        game = g.Game(self.input_data)
        self.assertEqual(436, game.part1())

    def test_part2(self):
        game = g.Game(self.input_data_part2)
        self.assertEqual(1, game.part2())


if __name__ == '__main__':
    unittest.main()
