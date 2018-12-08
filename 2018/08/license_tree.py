#!/usr/bin/env python3
from collections import namedtuple
from itertools import chain

def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read().strip()


Node = namedtuple('Node', 'metadata children')
NODE_LIST = []


def processChild(input_list):
    children_count, metadata_count = input_list[:2]
    tail = input_list[2:]
    children_list = []
    
    if children_count > 0:
        for _ in range(children_count):
            child, tail = processChild(tail)
            children_list.append(child)
    
    current_node = Node(metadata=tail[:metadata_count], children=children_list)
    NODE_LIST.append(current_node)
    
    return current_node, tail[metadata_count:]


def sum_metadata(file_input):
    numbers = list(map(int, file_input.split()))
    processChild(numbers)
    # 'chain' flattens the list of lists
    return sum(chain(*(map(lambda n: n.metadata, NODE_LIST))))

def main():
    file_input = readFile('input')
    print('Part 1:', sum_metadata(file_input))


if __name__ == '__main__':
    main()
