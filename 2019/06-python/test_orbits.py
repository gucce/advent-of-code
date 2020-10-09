import textwrap
import unittest
import orbits as o


class TestPassword(unittest.TestCase):
    def test_part1(self):
        input_ = textwrap.dedent("""
                    COM)B
                    B)C
                    C)D
                    D)E
                    E)F
                    B)G
                    G)H
                    D)I
                    E)J
                    J)K
                    K)L""")
        root, orbits = o.part1(input_)
        print(root)
        self.assertEqual(42, orbits)

    def test_part1_solution(self):
        _, orbits = o.part1(o.read_file('input'))
        self.assertEqual(135690, orbits)


if __name__ == '__main__':
    unittest.main()
