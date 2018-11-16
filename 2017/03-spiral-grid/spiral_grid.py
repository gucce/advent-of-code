#!/usr/bin/env python3
from itertools import cycle


# definition of spiral movement
move_right = lambda x, y: (x + 1, y)
move_down = lambda x, y: (x, y - 1)
move_left = lambda x, y: (x - 1, y)
move_up = lambda x, y: (x, y + 1)
moves = [move_right, move_up, move_left, move_down]


def manhatten_distance(pos1, pos2):
    dist = 0
    for i in range(2):
        dist += abs(pos1[i] - pos2[i])
    return dist


def gen_spiral(end):
    """copied from here: https://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python"""
    _moves = cycle(moves)
    n = 1
    pos = 0, 0
    steps_to_move = 1

    yield n, pos

    while True:
        # we always have to move the same amout of steps two time
        # before incrementing the steps
        for _ in range(2):
            move = next(_moves)
            for _ in range(steps_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos

        steps_to_move += 1


def distance_for_num(num):
    spiral_dict = {entry[0]: entry[1] for entry in gen_spiral(num)}
    return manhatten_distance((0,0), spiral_dict.get(num))


def main():
    print(distance_for_num(1))
    print(distance_for_num(12))
    print(distance_for_num(23))
    print(distance_for_num(1024))
    print(distance_for_num(265149))


if __name__ == '__main__':
    main()
