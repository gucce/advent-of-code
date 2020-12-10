import unittest
import jolt as j


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.input_data = '''16
10
15
5
1
11
7
19
6
12
4'''
        self.input_data_extended = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

    def test_map_input(self):
        self.assertEqual(11, len(j.map_input(self.input_data)))

    def test_part1(self):
        self.assertEqual(7 * 5, j.part1(j.map_input(self.input_data)))
        self.assertEqual(22 * 10, j.part1(j.map_input(self.input_data_extended)))

    def test_part2(self):
        self.assertEqual(62, j.part2(j.map_input(self.input_data), 127))


if __name__ == '__main__':
    unittest.main()
