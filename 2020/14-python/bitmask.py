from typing import List


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
        self.memory[addr] = self.mask_val(val)

    def write_mem_p2(self, addr, val):
        for masked_addr in self.mask_addr(addr):
            self.memory[masked_addr] = val

    def mask_addr(self, addr) -> List[int]:
        masked_addr = list()
        for m, a in zip(self.mask, self.to_binary_str(addr)):
            if m == '0':
                masked_addr.append(a)
            elif m == '1':
                masked_addr.append('1')
            else:
                masked_addr.append(m)
        masked_addr = ''.join(masked_addr)
        x_count = masked_addr.count('X')
        possible_addresses = list()
        for pos in range(2 ** x_count):
            comb_list = list(self.to_binary_str(pos, x_count))
            comb_list.append('')  # we need one more place at the end
            possible_addr = ''.join(a + c for a, c in zip(masked_addr.split('X'), comb_list))
            possible_addresses.append(int(possible_addr, 2))
        return possible_addresses

    def mask_val(self, val):
        bin_val = self.to_binary_str(val)
        masked_val = ''.join(v if m == 'X' else m for m, v in zip(self.mask, bin_val))
        return int(masked_val, 2)


def main():
    s1 = Proc(read_file('input'))
    s2 = Proc(read_file('input'))
    print('Part 1: ', s1.part1())
    print('Part 2: ', s2.part2())


if __name__ == '__main__':
    main()
