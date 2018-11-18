#!/usr/bin/env python3


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def jump(instructions):
    steps, current_idx = 0, 0
    while True:
        steps += 1
        next_idx = current_idx + instructions[current_idx] # jump
        if next_idx >= len(instructions):
            print(f'return current_idx {current_idx}, next_idx: {next_idx}')
            return steps
        instructions[current_idx] += 1
        current_idx = next_idx


def main():
    input = read_file('jump_list_input')
    print(jump([int(n) for n in input.splitlines()]))


if __name__ == '__main__':
    main()
