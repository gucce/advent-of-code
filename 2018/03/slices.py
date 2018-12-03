#!/usr/bin/env python3
from collections import namedtuple
from collections import defaultdict
import re

Point = namedtuple('Point', 'x y')
Rectangle = namedtuple('Rectangle', 'id min_x max_x min_y max_y')


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read()


def parse_rectangle(line):
    rec_id, x, y, width, height = map(int, re.findall(r'\d+', line))
    return Rectangle(id = rec_id, min_x = x, max_x = x + width, min_y = y, max_y = y + height)


def rec_coordinates(rec):
    coordinates = set()
    for x in range(rec.min_x, rec.max_x):
        for y in range(rec.min_y, rec.max_y):
            coordinates.add(Point(x, y))
    return coordinates


def coordinate_claims(rectangles):
    claims = defaultdict(list)
    for rec in rectangles:
        for p in rec_coordinates(rec):
            claims[p].append(rec.id)
    return claims


def non_overlapping(rectangles, claims):
    single_claims = []
    for rec in rectangles:
        if all(len(claims[p]) == 1 for p in rec_coordinates(rec)):
            single_claims.append(rec)
    return single_claims


def main():
    input = readFile('input', True)
    rectangles = list(map(parse_rectangle, input))
    claims = coordinate_claims(rectangles)
    single_claims = non_overlapping(rectangles, claims)
    print('Overlapping inches', sum(1 for v in claims.values() if len(v) > 1))
    print('Single claims', single_claims)


if __name__ == '__main__':
    main()
