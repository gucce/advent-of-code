import unittest
import seats as s


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
        self.seats = s.Seats(self.input_data)

    def test_map_input(self):
        self.assertEqual(10, len(self.seats.seats))

    def test_part1(self):
        self.assertEqual(37, self.seats.part1())

    def test_part2(self):
        self.assertEqual(8, s.Jolts(self.input_data).part2())
        self.assertEqual(19208, s.Jolts(self.input_data_extended).part2())


if __name__ == '__main__':
    unittest.main()
