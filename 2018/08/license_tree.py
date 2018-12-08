#!/usr/bin/env python3
from collections import namedtuple


def readFile(file_path, split_lines = False):
    with open(file_path, 'r', encoding="UTF-8") as f:
        if split_lines:
            return f.read().splitlines()
        else:
            return f.read().strip()


Node = namedtuple('Node', 'metadata children value')


def processNodes(input_list, node_list = []):
    children_count, metadata_count = input_list[:2]
    tail = input_list[2:]
    children_list = []
    
    # process children first
    for _ in range(children_count):
        child, tail = processNodes(tail, node_list)
        children_list.append(child)
    
    metadata_list = tail[:metadata_count]
    node_value = sum_metadata_recursive(metadata_list, children_list)
    current_node = Node(metadata=metadata_list, children=children_list, value=node_value)
    # keep track of all nodes
    node_list.append(current_node)
    return current_node, tail[metadata_count:]


def sum_metadata_recursive(metadata_list, children):
    if len(children) == 0:
        return sum(metadata_list)
    else:
        return sum(
            map(lambda m: children[m-1].value, 
                filter(lambda m: m <= len(children),  metadata_list)))


def root_value(file_input):
    numbers = list(map(int, file_input.split()))
    root, _ = processNodes(numbers)
    return root.value


def sum_metadata(file_input):
    numbers = list(map(int, file_input.split()))
    node_list = []
    processNodes(numbers, node_list)
    return sum(map(lambda n: sum(n.metadata), node_list))

def main():
    file_input = readFile('input')
    print('Part 1:', sum_metadata(file_input))
    print('Part 2:', root_value(file_input))


if __name__ == '__main__':
    main()
