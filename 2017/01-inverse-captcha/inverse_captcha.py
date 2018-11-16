#!/usr/bin/env python3
from collections import defaultdict


def read_first_line(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()[0]


def int_to_digit_list(number):
    return list(map(int, str(number)))


def calc_checksum_comprehension(input, neighbor_dist = 1):
    count = 0
    if not len(str(input)) < 2:
        input_list = int_to_digit_list(input)
        count = sum(n for idx, n in enumerate(input_list) if n == input_list[idx - neighbor_dist])
    return count


def calc_checksum_loop(input, neighbor_dist = 1):
    count = 0
    if not len(str(input)) < 2:
        input_list = int_to_digit_list(input)
        for idx, number in enumerate(input_list):
            if number == input_list[idx - neighbor_dist]:
                count += number
    return count


def main():
    input_data = read_first_line('inverse_captcha_input')
    print(f'Checksum for input (comprehension, neighbor distance = 1): {calc_checksum_comprehension(input_data)}')
    print(f'Checksum for input (loop, neighbor distance = 1): {calc_checksum_loop(input_data)}')
    print(f'Checksum for input (loop, neighbor distance = half input size): {calc_checksum_comprehension(input_data, len(input_data)//2)}')
    print(f'Checksum for input (loop, neighbor distance = half input size): {calc_checksum_loop(input_data, len(input_data)//2)}')


if __name__ == '__main__':
    main()