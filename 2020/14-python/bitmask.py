def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


class Proc:

    def __init__(self, input_data: str):
        self.input_data = input_data
        self.memory = dict()
        self.mask = 'X' * 36

    def part1(self) -> int:
        return self.process(self.write_mem_p1)

    def part2(self) -> int:
        return self.process(self.write_mem_p2)

    def process(self, write_mem) -> int:
        for line in self.input_data.splitlines():
            if line.startswith('mask'):
                self.mask = line.split(' = ')[1]
            else:
                addr, val = self.parse_mem(line)
                write_mem(addr, val)
        return sum(self.memory.values())

    @staticmethod
    def parse_mem(mem_def: str):
        addr, val = mem_def.replace('mem[', '').replace(']', '').split(' = ')
        return int(addr), int(val)

    @staticmethod
    def to_binary_str(int_val, dec_places=36):
        format_def = '{0:0' + str(dec_places) + 'b}'
        return format_def.format(int_val)

    def write_mem_p1(self, addr, val):
        masked_val = ''.join(v if m == 'X' else m for m, v in zip(self.mask, self.to_binary_str(val)))
        self.memory[addr] = int(masked_val, 2)

    def write_mem_p2(self, addr, val):
        def mask_single(m: str, a: str):
            if m == '0':
                return a
            elif m == '1':
                return '1'
            else:
                return m

        masked_addr = ''.join(mask_single(m, a) for m, a in zip(self.mask, self.to_binary_str(addr)))
        x_count = masked_addr.count('X')
        for pos in range(2 ** x_count):
            # for zip to work the lists must be equally sized, hence the empty string at the end
            comb_list = list(self.to_binary_str(pos, x_count)) + list('')
            possible_addr = ''.join(a + c for a, c in zip(masked_addr.split('X'), comb_list))
            self.memory[int(possible_addr, 2)] = val


def main():
    s1 = Proc(read_file('input'))
    s2 = Proc(read_file('input'))
    print('Part 1: ', s1.part1())
    print('Part 2: ', s2.part2())


if __name__ == '__main__':
    main()
