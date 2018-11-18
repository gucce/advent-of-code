#!/usr/bin/env python3


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def increment_val(value, advanced = False):
    if advanced and value >= 3:
        return value - 1
    else:
        return value + 1


def jump(instructions, advanced = False):
    steps, current_idx = 0, 0
    while True:
        steps += 1
        next_idx = current_idx + instructions[current_idx] # jump
        if next_idx >= len(instructions):
            print(f'return current_idx {current_idx}, next_idx: {next_idx}')
            return steps
        instructions[current_idx] = increment_val(instructions[current_idx], advanced)
        current_idx = next_idx


def main():
    input = read_file('jump_list_input')
    print(jump([int(n) for n in input.splitlines()], advanced = False))
    print(jump([int(n) for n in input.splitlines()], advanced = True))


if __name__ == '__main__':
    main()
