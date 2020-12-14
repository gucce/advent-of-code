import unittest
import bitmask as b


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''
        self.input_data_part2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

    def test_part1(self):
        proc = b.Proc(self.input_data)
        self.assertEqual(165, proc.part1())

    def test_part2(self):
        proc = b.Proc(self.input_data_part2)
        self.assertEqual(208, proc.part2())


if __name__ == '__main__':
    unittest.main()
