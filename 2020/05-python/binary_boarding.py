import math

MAPPING = {
    'F': 0,
    'B': 1,
    'L': 0,
    'R': 1
}

ROWS = 128
COLS = 8


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(input_data: str):
    return [(line[:7], line[7:]) for line in input_data.splitlines()]


def bin_search(definition, start_range):
    curr_range = start_range
    for d in definition:
        div_idx = math.ceil(len(curr_range) / 2)
        ranges = [curr_range[:div_idx], curr_range[div_idx:]]
        curr_range = ranges[MAPPING[d]]
    return list(curr_range)[0]


def get_seat(data):
    row_def, col_def = data
    return bin_search(row_def, range(ROWS)), bin_search(col_def, range(COLS))


def get_seat_id(row, col):
    return row * 8 + col


def part1(mapped_data):
    return max(get_seat_id(*get_seat(data)) for data in mapped_data)


def part2(mapped_data):
    sorted_ids = sorted(get_seat_id(*get_seat(data)) for data in mapped_data if 0 < get_seat(data)[0] < 127)
    return next(seat_id + 1 for idx, seat_id in enumerate(sorted_ids) if
                idx + 1 < len(sorted_ids) and seat_id + 1 != sorted_ids[idx + 1])


def main():
    mapped_data = map_input(read_file('input'))
    print('Part 1: ', part1(mapped_data))
    print('Part 2: ', part2(mapped_data))


if __name__ == '__main__':
    main()
