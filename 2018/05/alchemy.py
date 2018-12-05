#!/usr/bin/env python3


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read().strip()


def find_smallest_chain(chain):
    lower_case_letters = set(map(lambda s: s.lower(), chain))
    return min([reduce_chain(chain.replace(l, '').replace(l.upper(), '')) for l in lower_case_letters])


def reduce_chain(chain):
    reduced_chain = []
    for s in chain:
        if len(reduced_chain) > 1:
            last_letter = reduced_chain[-1]
        else:
            last_letter = ''
        if s != last_letter and s.lower() == last_letter.lower():
            reduced_chain.pop()
        else:
            reduced_chain.append(s)
    return len(reduced_chain)


def main():
    input = readFile('input')
    input_reduction = reduce_chain(input)
    print('Part 1:', input_reduction)
    print('Part 2', find_smallest_chain(input))


if __name__ == '__main__':
    main()
