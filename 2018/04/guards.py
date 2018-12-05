#!/usr/bin/env python3
from collections import namedtuple
from collections import defaultdict
from collections import Counter
import re

Timelog = namedtuple('Timelog', 'id date minutes action')


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read()


def parse_log(time_log):
    id_match = re.search(r'#(\d+)', time_log)
    guard_id = ''
    if id_match:
        guard_id = id_match.group(1)
    matches = re.search(r'\[([\d-]+)\s\d+\:(\d+)\]\s(.*)', time_log)
    return Timelog(guard_id, matches.group(1), matches.group(2), matches.group(3))


def guard_stats(input):
    input.sort()
    current_guard = ''
    start_minute = end_minute = 0
    time_statistics = defaultdict(Counter)
    for t_log in map(parse_log, input):
        if t_log.id != '':
            current_guard = t_log.id
        if 'falls asleep' in t_log.action:
            start_minute = int(t_log.minutes)
        elif 'wakes up' in t_log.action:
            end_minute = int(t_log.minutes)
            time_statistics[current_guard].update(range(start_minute , end_minute))
    return time_statistics


def most_asleep_guard(time_stats):
    guard_sleep_time = {guard: len(list(counter.elements())) for (guard, counter) in time_stats.items()}
    return max(guard_sleep_time.items(), key=lambda it: it[1])


def solution_part_1(input):
    time_stats = guard_stats(input)
    guard_id, sleep_minutes = most_asleep_guard(time_stats)
    most_asleep_minute, sleep_times_per_minute = time_stats[guard_id].most_common(1)[0]
    return int(guard_id) * most_asleep_minute


def solution_part_2(input):
    time_stats = guard_stats(input)
    guard_top_minutes = {guard: counter.most_common(1)[0] for (guard, counter) in time_stats.items()}
    # sort by minute count, which is within the tuple (guard_id, (minute, min_count))
    guard_id, (minute, times) = max(guard_top_minutes.items(), key=lambda it: it[1][1])
    return int(guard_id) * minute


def main():
    input = readFile('input', True)
    print('solution_part_1(input)', solution_part_1(input))
    print('solution_part_2(input)', solution_part_2(input))


if __name__ == '__main__':
    main()
