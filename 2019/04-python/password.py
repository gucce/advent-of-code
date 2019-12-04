def is_valid_passwd(passwd):
    digits = list(map(int, str(passwd)))
    return all(
        [all((pair[0] <= pair[1]) for pair in zip(digits, digits[1:])),
         any((pair[0] == pair[1]) for pair in zip(digits, digits[1:]))]
    )


def part1(start, end):
    return len(list(filter(is_valid_passwd, range(start, end + 1))))


def main():
    start, end = 240298, 784956
    print('Part1: ', part1(start, end))


if __name__ == '__main__':
    main()
