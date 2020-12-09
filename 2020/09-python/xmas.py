from itertools import combinations
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(input_data: str) -> List[int]:
    return [int(line) for line in input_data.splitlines()]


def part1(input_data: List[int], pre_size: int) -> int:
    for idx in range(pre_size, len(input_data) - pre_size):
        if not any(sum(c) == input_data[idx] for c in combinations(input_data[idx - pre_size:idx], 2)):
            return input_data[idx]


def part2(input_data: List[int], invalid_number) -> int:
    for window_size in range(2, len(input_data)):
        for idx in range(len(input_data) - window_size + 1):
            current_window = input_data[idx:idx + window_size]
            if sum(current_window) == invalid_number:
                return min(current_window) + max(current_window)


def main():
    numbers = map_input(read_file('input'))
    invalid_number = part1(numbers, 25)
    print('Part 1: ', invalid_number)
    print('Part 2: ', part2(numbers, invalid_number))


if __name__ == '__main__':
    main()
