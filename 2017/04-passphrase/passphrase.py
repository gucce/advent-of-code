#!/usr/bin/env python3


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def contains_duplicates(line):
    return len(line) > len(set(line))


def count_valid_lines_duplicates(document):
    return(len([l for l in document.splitlines()
        if not contains_duplicates(l.split(' '))]))


def contains_anagram(line):
    for idx, w in enumerate(line):
        original_sorted = sorted(list(w))
        for other in line[(idx+1):]:
            if sorted(list(other)) == original_sorted:
                return True
    return False



def count_valid_lines_anagrams(document):
    return len([line for line in document.splitlines()
            if not contains_anagram(line.split(' '))])


def main():
    input = read_file('passphrase_input')
    print(count_valid_lines_duplicates(input))
    print(count_valid_lines_anagrams(input))


if __name__ == '__main__':
    main()
