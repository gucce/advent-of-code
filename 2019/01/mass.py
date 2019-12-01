def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def calc_fuel_for_mass_recursive(mass: int):
    fuel = calc_fuel_for_mass(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel_for_mass_recursive(fuel)


def calc_fuel_for_mass(mass: int):
    return int(mass/3) - 2


def calc_fuel_for_modules(module_masses, fuel_calculation):
    return sum(map(fuel_calculation, module_masses))


def map_input(input_):
    return list(map(int, input_.splitlines()))


def main():
    module_masses = map_input(read_file('input'))
    print(calc_fuel_for_modules(module_masses, calc_fuel_for_mass))
    print(calc_fuel_for_modules(module_masses, calc_fuel_for_mass_recursive))


if __name__ == '__main__':
    main()
