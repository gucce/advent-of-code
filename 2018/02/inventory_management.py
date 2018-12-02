#!/usr/bin/env python3
from itertools import combinations


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read()


def count_letter_groups(letters):
    two_letters = three_letters = False
    for l in set(letters):
        if letters.count(l) == 2:
            two_letters = True
        elif letters.count(l) == 3:
            three_letters = True
        if two_letters and three_letters:
            break;
    return (int(two_letters), int(three_letters))


def letter_checksum(lines):
    two_letter_score = three_letter_score = 0
    for l in lines:
        letter_groups = count_letter_groups(l)
        two_letter_score += letter_groups[0]
        three_letter_score += letter_groups[1]
    return two_letter_score * three_letter_score


def check_similarity(id_1, id_2):
    diff_count = 0
    identical_letters = []
    for idx, s in enumerate(id_1):
        if s != id_2[idx]:
            diff_count += 1
            if diff_count > 1:
                return False
        else:
            identical_letters.append(s)
    return ''.join(identical_letters)


def find_similar_ids(ids):
    similar_ids = []
    for id_1, id_2 in combinations(ids, 2):
        identical_letters = check_similarity(id_1, id_2)
        if identical_letters:
            similar_ids.append((id_1, id_2, identical_letters))
    return similar_ids


def main():
    input = readFile('input', True)
    print('letter_checksum(input)', letter_checksum(input))
    print('find_similar_ids(input)', find_similar_ids(input))


if __name__ == '__main__':
    main()
