from functools import reduce
from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(input_data: str) -> List[List[str]]:
    return [group.splitlines() for group in input_data.split('\n\n')]


def part1(groups):
    return sum(all_answers_count(group) for group in groups)


def all_answers_count(person_answers: List[str]) -> int:
    return len(reduce(lambda p, n: p.union(set(n)), person_answers, set(person_answers[0])))


def distinct_answers_count(person_answers: List[str]) -> int:
    return len(reduce(lambda p, n: p.intersection(set(n)), person_answers, set(person_answers[0])))


def part2(groups):
    return sum(distinct_answers_count(group) for group in groups)


def main():
    mapped_data = map_input(read_file('input'))
    print('Part 1: ', part1(mapped_data))
    print('Part 2: ', part2(mapped_data))


if __name__ == '__main__':
    main()
