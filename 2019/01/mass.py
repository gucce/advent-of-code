from collections import namedtuple
import itertools

Step = namedtuple('Step', 'direction_change steps')
Point = namedtuple('Point', 'direction x y')


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def calc_fuel_for_mass(mass: int):
    return int(mass/3) - 2


def calc_fuel_for_modules(module_masses):
    return sum(map(calc_fuel_for_mass, module_masses))


def main():
    input_ = read_file('input')
    module_masses = map(int, input_.splitlines())
    print(calc_fuel_for_modules(module_masses))


if __name__ == '__main__':
    main()
