#!/usr/bin/env python3
import unittest
import guards

class TestStreamParser(unittest.TestCase):


    def test_guards(self):
        test_input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".splitlines()
        self.assertEqual(guards.most_asleep_guard(guards.guard_stats(test_input)), ('10', 50))
        self.assertEqual(guards.solution_part_1(test_input), 240)
        self.assertEqual(guards.solution_part_2(test_input), 4455)


if __name__ == '__main__':
    unittest.main()