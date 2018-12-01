#!/usr/bin/env python3


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read()


def to_int_list(string_list):
    return [int(s) for s in string_list]


def string_sum(string_list):
    return sum(to_int_list(string_list))


def find_first_duplicate(string_list):
    int_list = to_int_list(string_list)
    frequency_history = []
    current_frequency = 0
    while True:
        for i in int_list:
            next_frequency = current_frequency + i
            if next_frequency in frequency_history:
                frequency_history.append(next_frequency)
                return next_frequency
            else:
                frequency_history.append(current_frequency)
                current_frequency = next_frequency


def main():
    input = readFile('input', True)
    print('string_sum(input)', string_sum(input))
    print('find_first_duplicate(input)', find_first_duplicate(input))


if __name__ == '__main__':
    main()
