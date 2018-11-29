#!/usr/bin/env python3
import unittest
import stream_parser


class TestStreamParser(unittest.TestCase):

    def test_group_sum(self):
        self.assertEqual(stream_parser.group_sum(r'{}'), 1)
        self.assertEqual(stream_parser.group_sum(r'{{{}}}'), 6)
        self.assertEqual(stream_parser.group_sum(r'{{},{}}'), 5)
        self.assertEqual(stream_parser.group_sum(r'{{{},{},{{}}}}'), 16)
        self.assertEqual(stream_parser.group_sum(r'{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(stream_parser.group_sum(r'{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(stream_parser.group_sum(r'{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(stream_parser.group_sum(r'{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

    def test_count_garbage(self):
        self.assertEqual(stream_parser.count_garbage(r'<>'), 0)
        self.assertEqual(stream_parser.count_garbage(r'<random characters>'), 17)
        self.assertEqual(stream_parser.count_garbage(r'<<<<>'), 3)
        self.assertEqual(stream_parser.count_garbage(r'<{!>}>'), 2)
        self.assertEqual(stream_parser.count_garbage(r'<!!>'), 0)
        self.assertEqual(stream_parser.count_garbage(r'<!!!>>'), 0)
        self.assertEqual(stream_parser.count_garbage(r'<{o"i!a,<{i<a>'), 10)


if __name__ == '__main__':
    unittest.main()