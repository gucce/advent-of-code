#!/usr/bin/env python3


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read().strip()


def reduce_chain(chain):
    reduced_chain = [chain[0]]
    for s in chain[1:]:
        last_letter = reduced_chain[-1]
        if s != last_letter and s.lower() == last_letter.lower():
            reduced_chain.pop()
        else:
            reduced_chain.append(s)
    return ''.join(reduced_chain)


def main():
    input = readFile('input')
    input_reduction_1 = reduce_chain(input)
    print('Part 1: len(input_reduction_1)', len(input_reduction_1))


if __name__ == '__main__':
    main()
