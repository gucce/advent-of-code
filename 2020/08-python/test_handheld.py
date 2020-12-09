import unittest
import handheld as h


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

    def test_map_input(self):
        self.assertEqual(9, len(h.map_input(self.input_data)))

    def test_part1(self):
        self.assertEqual((5, False), h.part1(h.map_input(self.input_data), 0))

    def test_part2(self):
        self.assertEqual(8, h.part2(h.map_input(self.input_data)))


if __name__ == '__main__':
    unittest.main()
