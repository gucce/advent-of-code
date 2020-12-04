import re
from typing import List, Dict


def check_height(height_str: str):
    unit_type = height_str[-2:]
    height = int(height_str[:-2])
    if unit_type == 'cm':
        return 150 <= height <= 193
    elif unit_type == 'in':
        return 59 <= height <= 76
    else:
        return False


REQ_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
RULES = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': check_height,
    'hcl': lambda v: bool(re.search(r'^#[0-9a-f]{6}$', v)),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: bool(re.search(r'^\d{9}$', v))
}


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input(passports: str) -> List[Dict]:
    p_key_values = [re.split(r'[\n ]', p_data) for p_data in passports.split('\n\n')]
    return [dict(p_kv.split(':') for p_kv in p_kv_list) for p_kv_list in p_key_values]


def has_req_fields(p: Dict):
    return all(field in p.keys() for field in REQ_FIELDS)


def part1(passports: List[Dict]):
    return sum(has_req_fields(p) for p in passports)


def has_valid_fields(p: Dict):
    return all(rule(p.get(field)) for field, rule in RULES.items() if field in p.keys())


def part2(passports: List[Dict]):
    return sum(has_req_fields(p) and has_valid_fields(p) for p in passports)


def main():
    passports = map_input(read_file('input'))
    print('Part 1: ', part1(passports))
    print('Part 2: ', part2(passports))


if __name__ == '__main__':
    main()
