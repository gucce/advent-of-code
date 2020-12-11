from copy import deepcopy
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


class Seats:

    def __init__(self, input_data):
        self.seats = self.map_input(input_data)
        self.dim = len(self.seats), len(self.seats[0])
        self.FREE = 'L'
        self.FLOOR = '.'
        self.OCC = '#'

    @staticmethod
    def map_input(input_data: str) -> List[List[str]]:
        return [[c for c in line] for line in input_data.splitlines()]

    def part1(self) -> int:
        next_seats = deepcopy(self.seats)
        self.print_seats()
        while True:
            for row in range(self.dim[0]):
                for col in range(self.dim[1]):
                    next_seats[row][col] = self.next_state(row, col)
            if self.seats == next_seats:
                self.seats = next_seats
                self.print_seats()
                break
            else:
                self.seats = next_seats
                next_seats = deepcopy(self.seats)
                self.print_seats()
        return self.count_occ_seats()

    def count_occ_seats(self) -> int:
        return sum(sum(1 for s in row if s == self.OCC) for row in self.seats)

    def part2(self) -> int:
        return 1

    def next_state(self, row, col):
        seat = self.seats[row][col]
        if seat == self.FREE:
            if all(self.seats[seat[0]][seat[1]] != self.OCC for seat in self.surrounding_seats(row, col)):
                return self.OCC
        elif seat == self.OCC:
            if sum(self.seats[s[0]][s[1]] == self.OCC for s in self.surrounding_seats(row, col)) >= 4:
                return self.FREE
        return seat

    def surrounding_seats(self, row, col):
        adj_seats = list()
        for row_diff in [-1, 0, 1]:
            for col_diff in [-1, 0, 1]:
                if not (row_diff == 0 and col_diff == 0):
                    adj_row = row + row_diff
                    adj_col = col + col_diff
                    if 0 <= adj_row < self.dim[0] and 0 <= adj_col < self.dim[1]:
                        adj_seats.append((adj_row, adj_col))
        return adj_seats

    def print_seats(self):
        [print(''.join(row)) for row in self.seats]
        print()


def main():
    s = Seats(read_file('input'))
    print('Part 1: ', s.part1())
    print('Part 2: ', s.part2())


if __name__ == '__main__':
    main()
