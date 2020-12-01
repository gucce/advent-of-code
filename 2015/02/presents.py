import math
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def parse(dim_list):
    return [[int(dim) for dim in line.split('x')] for line in dim_list.splitlines()]


def part_one(dim_list: List) -> int:
    return sum(calc_area(dim) for dim in dim_list)


def calc_area(dim: List):
    l, w, h = dim
    area = 2 * l * w + 2 * w * h + 2 * h * l
    min_dim = sorted(dim)[:2]
    slack = math.prod(min_dim)
    return area + slack


def calc_ribbon(dim: List):
    bow_length = math.prod(dim)
    min_dim = sorted(dim)[:2]
    ribbon_length = sum(x + x for x in min_dim)
    return bow_length + ribbon_length


def part_two(dim_list: list) -> int:
    return sum(calc_ribbon(dim) for dim in dim_list)


if __name__ == '__main__':
    parsed_input = parse(read_file('input'))
    print('part 1:', part_one(parsed_input))
    print('part 2:', part_two(parsed_input))
