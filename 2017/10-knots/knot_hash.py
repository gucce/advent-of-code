def readFile(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def hash(hash_base, knot_lengths):
    hash_length = len(hash_base)
    pos = skip = 0
    for length in knot_lengths:
        indices = list(map(lambda x: x % hash_length, range(pos, pos+length)))
        reverted_range = [hash_base[i] for i in indices]
        reverted_range.reverse()
        for idx, idx_indices in enumerate(indices):
            hash_base[idx_indices] = reverted_range[idx]
        pos += length + skip
        skip += 1
    return hash_base


def main():
    input = readFile('input')
    input_ints = map(int, input.split(','))
    hash_base = [x for x in range(0, 256)]
    result = hash(hash_base, input_ints)
    print('result', result[0] * result[1])


if __name__ == '__main__':
    main()
