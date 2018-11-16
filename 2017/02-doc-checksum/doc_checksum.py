#!/usr/bin/env python3
from collections import defaultdict
import re
from itertools import combinations

no_whitespace_regex = re.compile(r'[^\w]+')


def checksum_min_max(numbers):
    return max(numbers) - min(numbers)


def checksum_division(numbers):
    checksum = 0
    for n, m in combinations(numbers, 2):
        if n % m == 0 or m % n == 0:
            div_pair = (n, m)
    if (div_pair):
        return max(div_pair) / min(div_pair)
    else:
        raise RuntimeError(f'No division pair found for numbers: {numbers}')


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def calc_line_checksum(line, calc_checksum_func):
    numbers = list(map(int, no_whitespace_regex.split(line)))
    checksum = calc_checksum_func(numbers)
    return checksum


def calc_doc_checksum(input, calc_checksum_func):
    return sum(calc_line_checksum(line, calc_checksum_func) for line in input.splitlines())


def calc_doc_checksum_min_max(input):
    return calc_doc_checksum(input, checksum_min_max)


def calc_doc_checksum_division(input):
    return calc_doc_checksum(input, checksum_division)


def main():
    input_max_min = """5 1 9 5
7 5 3
2 4 6 8"""
    input_division = """5 9 2 8
9 4 7 3
3 8 6 5"""
    input_from_file = read_file('input_doc_checksum')
    print(f'Doc checksum (min, max): {calc_doc_checksum_min_max(input_from_file)}')
    print(f'Doc checksum (division): {calc_doc_checksum_division(input_from_file)}')


if __name__ == '__main__':
    main()