from dataclasses import dataclass
from typing import List


@dataclass
class Op:
    name: str = ''
    signed_int: str = ''
    exec_cnt: int = 0


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read().strip()


def map_input(input_data: str) -> List[Op]:
    return [Op(*line.split(' ')) for line in input_data.splitlines()]


def part1(ops: List[Op], acc: int) -> (int, bool):
    idx = 0
    while idx < len(ops):
        current_op = ops[idx]
        if current_op.exec_cnt > 0:
            return acc, False
        value = int(current_op.signed_int)
        current_op.exec_cnt += 1
        if current_op.name == 'acc':
            acc += value
        elif current_op.name == 'jmp':
            idx += value - 1
        idx += 1
    return acc, True


def part2(ops: List[Op]) -> int:
    for replacement in [('jmp', 'nop'), ('nop', 'jmp')]:
        for op_idx in [idx for idx, op in enumerate(ops) if op.name == replacement[0]]:
            org = ops[op_idx]
            temp_ops = ops.copy()
            temp_ops[op_idx] = Op(name=replacement[1], signed_int=org.signed_int, exec_cnt=org.exec_cnt)
            acc, terminated = part1(temp_ops, 0)
            reset_cnt(temp_ops)
            if terminated:
                return acc


def reset_cnt(ops):
    for op in ops:
        op.exec_cnt = 0


def main():
    print('Part 1: ', part1(map_input(read_file('input')), 0))
    print('Part 2: ', part2(map_input(read_file('input'))))


if __name__ == '__main__':
    main()
