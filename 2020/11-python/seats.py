from copy import deepcopy
from functools import cache
from itertools import product
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


class Seats:

    def __init__(self, input_data):
        self.seats = self.map_input(input_data)
        self.dim = len(self.seats), len(self.seats[0])
        self.offsets = list(filter(lambda t: t != (0, 0), product([-1, 0, 1], [-1, 0, 1])))
        self.FREE = 'L'
        self.FLOOR = '.'
        self.OCC = '#'

    @staticmethod
    def map_input(input_data: str) -> List[List[str]]:
        return [[c for c in line] for line in input_data.splitlines()]

    def part1(self) -> int:
        while True:
            next_seats = deepcopy(self.seats)
            for row, col in product(range(self.dim[0]), range(self.dim[1])):
                next_seats[row][col] = self.next_state(row, col)
            if self.seats == next_seats:
                break
            self.seats = next_seats
        return self.count_occ_seats()

    def count_occ_seats(self) -> int:
        return sum(sum(1 for s in row if s == self.OCC) for row in self.seats)

    def next_state(self, row, col):
        seat = self.seats[row][col]
        if seat == self.FREE:
            if all(self.seats[s_id[0]][s_id[1]] != self.OCC for s_id in self.surrounding_seats(row, col)):
                return self.OCC
        elif seat == self.OCC:
            if sum(self.seats[s[0]][s[1]] == self.OCC for s in self.surrounding_seats(row, col)) >= 4:
                return self.FREE
        return seat

    @cache
    def surrounding_seats(self, row, col):
        def seat_is_valid(r, c):
            return 0 <= r < self.dim[0] and 0 <= c < self.dim[1]

        return list(filter(lambda s: seat_is_valid(*s), [(row + dr, col + dc) for dr, dc in self.offsets]))

    def part2(self) -> int:
        return 1

    def print_seats(self):
        [print(''.join(row)) for row in self.seats]
        print()


def main():
    s = Seats(read_file('input'))
    print('Part 1: ', s.part1())
    print('Part 2: ', s.part2())


if __name__ == '__main__':
    main()
