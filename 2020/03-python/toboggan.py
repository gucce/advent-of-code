import math
from collections import namedtuple
from typing import List

TREE = '#'

Point = namedtuple('Point', 'x y')


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(input_list):
    return [[char for char in row] for row in input_list.splitlines()]


def add_point(first: Point, second: Point, width: int):
    return Point((first.x + second.x) % width, first.y + second.y)


def count_trees(input_matrix: List, step: Point):
    height = len(input_matrix)
    width = len(input_matrix[0])
    current = Point(0, 0)
    tree_count = 0
    while current.y < height:
        if input_matrix[current.y][current.x] == TREE:
            tree_count += 1
        current = add_point(current, step, width)
    return tree_count


def mul_trees(input_matrix, steps: List[Point]):
    return math.prod(count_trees(input_matrix, p) for p in steps)


def main():
    input_map = map_input(read_file('input'))
    print('Part 1: ', count_trees(input_map, step=Point(3, 1)))
    print('Part 2: ', mul_trees(input_map, steps=[Point(1, 1), Point(3, 1), Point(5, 1), Point(7, 1), Point(1, 2)]))


if __name__ == '__main__':
    main()
