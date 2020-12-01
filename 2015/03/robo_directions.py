from collections import namedtuple
from typing import List, Set

Point = namedtuple('Point', 'x y')
mapping = {
    "^": Point(0, 1),
    ">": Point(1, 0),
    "v": Point(0, -1),
    "<": Point(-1, 0),
}


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()[0]


def sum_points(first: Point, second: Point):
    return Point(first.x + second.x, first.y + second.y)


def visited_distinct_points(directions: str) -> Set[Point]:
    points: List[Point] = [Point(0, 0)]
    for direction in directions:
        points.append(sum_points(points[-1], mapping[direction]))
    return set(points)


def part_one(directions: str) -> int:
    return len(visited_distinct_points(directions))


def part_two(directions: str) -> int:
    return len(visited_distinct_points(directions[::2]).union(visited_distinct_points(directions[1::2])))


if __name__ == '__main__':
    input_data = read_file('input')
    print('part 1:', part_one(input_data))
    print('part 2:', part_two(input_data))
