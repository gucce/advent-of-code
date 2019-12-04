def is_valid_passwd(passwd, part2=False):
    def is_valid_part2(quadruple):
        return quadruple[0] != quadruple[1] and quadruple[1] == quadruple[2] and quadruple[2] != quadruple[3]

    def start_or_end(digits_):
        start = digits_[0] == digits_[1] and digits_[1] != digits_[2]
        end = digits_[-1] == digits_[-2] and digits_[-2] != digits_[-3]
        return start or end

    digits = list(map(int, str(passwd)))

    part1_result = all(
        [all((pair[0] <= pair[1]) for pair in zip(digits, digits[1:])),
         any((pair[0] == pair[1]) for pair in zip(digits, digits[1:]))]
    )
    if part1_result and part2:
        in_between = any(is_valid_part2(quadruple) for quadruple in zip(digits, digits[1:], digits[2:], digits[3:]))
        return in_between or start_or_end(digits)
    else:
        return part1_result


def solution(start, end, part2=False):
    if not part2:
        return len(list(filter(is_valid_passwd, range(start, end + 1))))
    else:
        return len(list(filter(lambda x: is_valid_passwd(x, True), range(start, end + 1))))


def main():
    start, end = 240298, 784956
    print('Part1: ', solution(start, end))
    print('Part2: ', solution(start, end, part2=True))


if __name__ == '__main__':
    main()
