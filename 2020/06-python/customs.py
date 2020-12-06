from typing import List


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(input_data: str):
    return input_data.split('\n\n')


def part1(groups):
    return sum(len(set(group.replace('\n', ''))) for group in groups)


def distinct_answers_count(person_answers: List[str]):
    distinct = set(person_answers[0])
    for a in person_answers:
        distinct = distinct.intersection(set(a))
    return len(distinct)


def part2(groups):
    return sum(distinct_answers_count(group.splitlines()) for group in groups)


def main():
    mapped_data = map_input(read_file('input'))
    print('Part 1: ', part1(mapped_data))
    print('Part 2: ', part2(mapped_data))


if __name__ == '__main__':
    main()
