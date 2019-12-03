#!/usr/bin/env python3
from collections import namedtuple
import re


CpuCalculation = namedtuple('CpuCalculation', 'before command after')

Register = namedtuple('Register', 'op a b c')

op_funcs = {
    'addr': lambda r: r[r.a] + r[r.b],
    'addi': lambda r: r[r.a] + r.b,
    'mulr': lambda r: r[r.a] * r[r.b],
    'muli': lambda r: r[r.a] * r.b,
    'banr': lambda r: r[r.a] & r[r.b],
    'bani': lambda r: r[r.a] & r.b,
    'borr': lambda r: r[r.a] | r[r.b],
    'bori': lambda r: r[r.a] | r.b,
    'setr': lambda r: r[r.a],
    'seti': lambda r: r.a,
    'gtir': lambda r: int(r.a > r[r.b]),
    'gtri': lambda r: int(r[r.a] > r.b),
    'gtrr': lambda r: int(r[r.a] > r[r.b]),
    'eqir': lambda r: int(r.a == r[r.b]),
    'eqri': lambda r: int(r[r.a] == r.b),
    'eqrr': lambda r: int(r[r.a] == r[r.b])
}


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read().strip()



def parseTrace(trace):
    numbers_regex = re.compile(r'\d+')
    before, cmd, after = [map(int, re.findall(numbers_regex, line)) for line in trace.splitlines()]
    return CpuCalculation(Register(*before), Register(*cmd), Register(*after))


def parseCpuTrace(input):
    first_part, second_part = input.split('\n\n\n')
    cpu_trace_list = first_part.split('\n\n')
    return cpu_trace_list


def executeStep(reg, op_func_name):
    # only ever 'c' changes
    return Register(op=reg.op, a=reg.a, b=reg.b, c=op_funcs[op_func_name](reg))


def evaluateCpuCalculation(cpu_calc):
    possible_funcs = []
    for key in op_funcs.keys():
        after = executeStep(cpu_calc.before, key)
        if after == cpu_calc.after:
            possible_funcs.append(key)
    return possible_funcs



def main():
    file_input = readFile('input')
    cpu_trace_list = parseCpuTrace(file_input)
    cpu_calc_list = [parseTrace(x) for x in cpu_trace_list]

    more_than_three_possibilities = []

    for cpu_calc in cpu_calc_list:
        possible_functions = evaluateCpuCalculation(cpu_calc)
        if len(possible_functions) >= 3:
            more_than_three_possibilities.append(cpu_calc)
    print('more_than_three_possibilities', more_than_three_possibilities)
    print('len(more_than_three_possibilities)', len(more_than_three_possibilities))

    


if __name__ == '__main__':
    main()
