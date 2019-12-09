def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().splitlines()[0]


def map_input(input_):
    return list(map(int, input_))


def part1(digits, width, height):
    layers = get_layers(digits, height, width)
    min_l_idx, _ = min(((l_idx, layer.count(0)) for l_idx, layer in enumerate(layers)), key=lambda t: t[1])
    min_layer = layers[min_l_idx]
    count1 = min_layer.count(1)
    count2 = min_layer.count(2)
    return count1 * count2


def part2(digits, width, height):
    layers = get_layers(digits, width, height)
    result = []
    for i in range(0, len(layers[0])):
        result.append(next(layer[i] for layer in layers if layer[i] != 2))

    rows = [result[l_i:l_i + width] for l_i in range(0, len(result), width)]
    for r in rows:
        print(''.join(map(str, r)).replace('0', ' '))
    return result


def get_layers(digits, width, height):
    layers = []
    step = width * height
    for index_t in range(0, len(digits), step):
        layers.append(digits[index_t:index_t + step])
    return layers


def main():
    digits = map_input(read_file('input'))
    print('Part 1: ', part1(digits, 25, 6))
    part2(digits, 25, 6)


if __name__ == '__main__':
    main()
