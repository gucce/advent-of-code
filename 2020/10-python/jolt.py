from collections import Counter
from functools import cache
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


class Jolts:

    def __init__(self, input_data, start=0):
        self.jolts = self.map_input(input_data)
        self.jolts.insert(0, start)
        self.jolts.append(max(self.jolts) + 3)

    @staticmethod
    def map_input(input_data: str) -> List[int]:
        return sorted(int(line) for line in input_data.splitlines())

    def part1(self) -> int:
        c = Counter()
        c.update(self.jolts[idx] - self.jolts[idx - 1] for idx in range(1, len(self.jolts)))
        return c[1] * c[3]

    @cache
    def part2(self, curr_idx=0) -> int:
        # the last element has 1 possibility
        if curr_idx == len(self.jolts) - 1:
            return 1
        return sum(self.part2(next_idx) for next_idx in range(curr_idx + 1, len(self.jolts))
                   if self.jolts[next_idx] - self.jolts[curr_idx] <= 3)


def sort_jolts(jolts, start=0):
    sorted_jolts = sorted(jolts)
    sorted_jolts.insert(0, start)
    sorted_jolts.append(max(sorted_jolts) + 3)
    return sorted_jolts


def main():
    j = Jolts(read_file('input'))
    print('Part 1: ', j.part1())
    print('Part 2: ', j.part2())


if __name__ == '__main__':
    main()
