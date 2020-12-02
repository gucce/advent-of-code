import re


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()


def map_input(input_):
    return [re.split(r'[- :]+', line) for line in input_]


def check_psw_validity_part1(min_char, max_char, char, psw: str):
    return int(min_char) <= psw.count(char) <= int(max_char)


def check_psw_validity_part2(first, second, char, psw: str):
    first_idx = int(first) - 1
    sec_idx = int(second) - 1
    return (psw[first_idx] == char) != (psw[sec_idx] == char)


def part1(psw_list):
    return sum(map(lambda psw_params: check_psw_validity_part1(*psw_params), psw_list))


def part2(psw_list):
    return sum(map(lambda psw_params: check_psw_validity_part2(*psw_params), psw_list))


def main():
    psw_list = map_input(read_file('input'))
    print('Part 1: ', part1(psw_list))
    print('Part 2: ', part2(psw_list))


if __name__ == '__main__':
    main()
