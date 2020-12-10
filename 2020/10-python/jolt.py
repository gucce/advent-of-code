from collections import Counter
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


def map_input(input_data: str) -> List[int]:
    return [int(line) for line in input_data.splitlines()]


def part1(jolts: List[int], start=0) -> int:
    c = Counter()
    sorted_jolts = sorted(jolts)
    sorted_jolts.insert(0, start)
    sorted_jolts.append(max(sorted_jolts) + 3)
    for idx in range(len(sorted_jolts) - 1):
        diff = sorted_jolts[idx + 1] - sorted_jolts[idx]
        if diff > 3:
            print('Problem:', sorted_jolts[idx], sorted_jolts[idx + 1])
        c.update({diff})
    print(c)
    return c[1] * c[3]


def part2(jolts: List[int]) -> int:
    pass


def main():
    jolts = map_input(read_file('input'))
    print('Part 1: ', part1(jolts))
    print('Part 2: ', part2(jolts))


if __name__ == '__main__':
    main()
