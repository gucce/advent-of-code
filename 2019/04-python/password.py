def is_valid_passwd(passwd, part2=False):
    def double_digits_in_center(quadruple):
        return quadruple[0] != quadruple[1] and quadruple[1] == quadruple[2] and quadruple[2] != quadruple[3]

    def pad_digits(digits_):
        padding = [-1]
        padded_digits_ = padding
        padded_digits_.extend(digits_)
        padded_digits_.extend(padding)
        return padded_digits_

    digits = list(map(int, str(passwd)))

    part1_result = all(
        [all((pair[0] <= pair[1]) for pair in zip(digits, digits[1:])),
         any((pair[0] == pair[1]) for pair in zip(digits, digits[1:]))]
    )
    if part1_result and part2:
        # to account for double digits at the beginning or at the end we add a -1 before and after the digits
        padded_digits = pad_digits(digits)
        return any(double_digits_in_center(quadruple) for quadruple in
                   zip(padded_digits, padded_digits[1:], padded_digits[2:], padded_digits[3:]))
    else:
        return part1_result


def solution(start, end, part2=False):
    return len(list(filter(lambda x: is_valid_passwd(passwd=x, part2=part2), range(start, end + 1))))


def main():
    start, end = 240298, 784956
    print('Part1: ', solution(start, end))
    print('Part2: ', solution(start, end, part2=True))


if __name__ == '__main__':
    main()
