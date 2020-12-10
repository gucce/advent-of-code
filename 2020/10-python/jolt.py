from collections import Counter
from typing import List, Dict


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


def map_input(input_data: str) -> List[int]:
    return [int(line) for line in input_data.splitlines()]


def part1(sorted_jolts: List[int]) -> int:
    c = Counter()
    c.update(sorted_jolts[idx + 1] - sorted_jolts[idx] for idx in range(len(sorted_jolts) - 1))
    print(c)
    return c[1] * c[3]


def part2(curr_idx: int, cache: Dict, sorted_jolts: List[int]) -> int:
    if curr_idx == len(sorted_jolts) - 1:
        return 1
    if curr_idx in cache:
        return cache[curr_idx]
    curr_poss = 0
    for next_idx in range(curr_idx + 1, len(sorted_jolts)):
        if sorted_jolts[next_idx] - sorted_jolts[curr_idx] <= 3:
            curr_poss += part2(next_idx, cache, sorted_jolts)
    cache[curr_idx] = curr_poss
    return curr_poss


def sort_jolts(jolts, start=0):
    sorted_jolts = sorted(jolts)
    sorted_jolts.insert(0, start)
    sorted_jolts.append(max(sorted_jolts) + 3)
    return sorted_jolts


def main():
    jolts = map_input(read_file('input'))
    start = 0
    sorted_jolts = sort_jolts(jolts, start)
    print('Part 1: ', part1(sorted_jolts))
    print('Part 2: ', part2(0, dict(), sorted_jolts))


if __name__ == '__main__':
    main()
