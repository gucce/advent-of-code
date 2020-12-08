import unittest
import bags as b


class TestLayers(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.my_bag = b.Bag('shiny gold', 0)
        self.input_ = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
        self.rules = b.map_input(self.input_)
        self.input_part2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''
        self.rules_part2 = b.map_input(self.input_part2)

    def test_map_input(self):
        self.assertEqual(9, len(b.map_input(self.input_).keys()))

    def test_part1(self):
        self.assertEqual(4, b.part1(self.my_bag, self.rules))

    def test_part2(self):
        self.assertEqual(32, b.part2(self.my_bag, b.map_input(self.input_)))
        self.assertEqual(126, b.part2(self.my_bag, self.rules_part2))


if __name__ == '__main__':
    unittest.main()
