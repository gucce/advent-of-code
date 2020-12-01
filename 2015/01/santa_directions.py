def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_direction(char):
    return 1 if char == "(" else -1


def part_one(directions: str) -> int:
    return sum(map_direction(d) for d in directions)


def part_two(directions: str) -> int:
    level = 0
    for idx, d in enumerate(directions):
        level += map_direction(d)
        if level == -1:
            return idx + 1


if __name__ == '__main__':
    input_data = read_file('input')
    print('part 1:', part_one(input_data))
    print('part 2:', part_two(input_data))
