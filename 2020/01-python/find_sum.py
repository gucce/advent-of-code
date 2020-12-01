from itertools import combinations as comb
import math


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()


def map_input(input_):
    return list(map(int, input_))


def part1(digits):
    for c in comb(digits, 2):
        if sum(c) == 2020:
            return math.prod(c)


def main():
    digits = map_input(read_file('input'))
    print('Part 1: ', part1(digits))


if __name__ == '__main__':
    main()
