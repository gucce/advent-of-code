import re


garbage_regex = re.compile(r'<.*?>')
escape_regex = re.compile(r'\!.|[^!]*')


def readFile(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def remove_escapes(input):
    escape_list = re.findall(escape_regex, input)
    return ''.join([t for t in escape_list if t and t[0] != '!'])


def extract_braces(input):
    no_escapes = remove_escapes(input)    
    no_garbage = re.sub(garbage_regex, '', no_escapes)
    only_braces = ''.join([t for t in no_garbage if t in ['{', '}']])
    return only_braces


def count_garbage(input):
    no_escapes = remove_escapes(input)
    garbage = re.findall(garbage_regex, no_escapes)
    garbage_count_without_brackets = sum([len(g[1:-1]) for g in garbage])
    return garbage_count_without_brackets


def group_sum(input):
    groups = extract_braces(input)
    sum, level = 0, 0
    for g in groups:
        if g == '{':
            level += 1
        elif g == '}':
            sum += level
            level -= 1
    return sum


def main():
    input = readFile('stream_matching_input')
    print('group_sum', group_sum(input))
    print('garbage_count', count_garbage(input))


if __name__ == '__main__':
    main()
