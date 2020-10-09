from collections import namedtuple

Node = namedtuple('Node', ['name', 'depth', 'children'])


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def construct_tree(parent, tuples):
    remaining_tuples = [t for t in tuples if t[0] != parent.name]
    children = [Node(name=t[1], depth=parent.depth + 1, children=[]) for t in tuples if t[0] == parent.name]
    parent.children.extend(children)
    for c in parent.children:
        construct_tree(c, remaining_tuples)


def split_tuples(input_, sep=')'):
    lines = input_.splitlines()
    return [line.split(sep) for line in lines]


def count_orbits(node: Node):
    return node.depth + sum(map(count_orbits, node.children))


def part1(input_, root_name='COM'):
    root = Node(name=root_name, depth=0, children=[])
    tuples = split_tuples(input_)
    construct_tree(root, tuples)
    orbits = count_orbits(root)
    return root, orbits


def main():
    root, orbits = part1(read_file('input'))
    print('part1', orbits)


if __name__ == '__main__':
    main()
