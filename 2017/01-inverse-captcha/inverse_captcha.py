#!/usr/bin/env python3
from collections import defaultdict


def read_first_line(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()[0]


def int_to_digit_list(number):
    return list(map(int, str(number)))


def calc_checksum_comprehension(input):
    count = 0
    if not len(str(input)) < 2:
        input_list = int_to_digit_list(input)
        count = sum(n for idx, n in enumerate(input_list) if n == input_list[idx-1])
    return count


def calc_checksum_loop(input):
    count = 0
    if not len(str(input)) < 2:
        input_list = int_to_digit_list(input)
        for idx, number in enumerate(input_list):
            if number == input_list[idx-1]:
                count += number
    return count


def main():
    input_data = read_first_line('inverse_captcha_input')
    print(f'Checksum for input (comprehension): {calc_checksum_comprehension(input_data)}')
    print(f'Checksum for input (loop): {calc_checksum_loop(input_data)}')


if __name__ == '__main__':
    main()