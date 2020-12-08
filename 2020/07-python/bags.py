from collections import namedtuple
from typing import List, Dict

Bag = namedtuple('Bag', 'color size')


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def get_rule(bag_def: str) -> (str, List[Bag]):
    # 'vibrant aqua bags contain 1 shiny magenta bag, 2 muted teal bags, 1 dim magenta bag, 1 muted chartreuse bag.'
    # faded blue bags contain no other bags.
    allowed_bags = list()
    if bag_def.endswith(' bags contain no other bags.'):
        top_bag = bag_def.replace(' bags contain no other bags.', '')  # only the color as key
    else:
        bags = bag_def[:-1].replace(' bags contain', ',') \
            .replace(' bags', '') \
            .replace(' bag', '') \
            .split(',')
        allowed_bags = [Bag(color=bag[2:].strip(), size=int(bag[:2])) for bag in bags[1:]]
        top_bag = bags[0]
    return top_bag, allowed_bags


def map_input(bag_defs: str) -> Dict[str, List[Bag]]:
    return dict(get_rule(bag_def) for bag_def in bag_defs.splitlines())


def allowed_in(bag: Bag, bags: List[Bag]) -> bool:
    return any(b.color == bag.color for b in bags)


def contains_transitive(my_bag: Bag, bag_color: str, rules: Dict[str, List[Bag]]):
    nested_bags = rules[bag_color]
    return allowed_in(my_bag, nested_bags) or any(contains_transitive(my_bag, bag.color, rules) for bag in nested_bags)


def count_bags(bags: List[Bag], rules: Dict[str, List[Bag]]) -> int:
    return sum(bag.size + bag.size * count_bags(rules[bag.color], rules) for bag in bags)


def part1(my_bag: Bag, rules: Dict[str, List[Bag]]) -> int:
    return sum(contains_transitive(my_bag, color, rules) for color in rules.keys())


def part2(my_bag: Bag, rules: Dict[str, List[Bag]]) -> int:
    return count_bags(rules[my_bag.color], rules)


def main():
    rules = map_input(read_file('input'))
    print('Part 1: ', part1(Bag('shiny gold', 0), rules))
    print('Part 2: ', part2(Bag('shiny gold', 0), rules))


if __name__ == '__main__':
    main()
