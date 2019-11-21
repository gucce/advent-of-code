from collections import namedtuple

Step = namedtuple('Step', 'direction_change steps')
Point = namedtuple('Point', 'direction x y')


def readFile(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input_to_step(input):
    if input[0] == 'R':
        direction_change = 1
    elif input[0] == 'L':
        direction_change = -1
    else:
        exit(1)
    return Step(direction_change, int(input[1:]))


def walk(point, step):
    new_direction = (point.direction + step.direction_change) % 4
    new_x = point.x
    new_y = point.y
    if new_direction == 0:
        new_y += step.steps
    elif new_direction == 1:
        new_x += step.steps
    elif new_direction == 2:
        new_y -= step.steps
    elif new_direction == 3:
        new_x -= step.steps
    return Point(new_direction, new_x, new_y)


def walk_steps(steps):
    current = Point(direction=0, x=0, y=0)
    for s in steps:
        current = walk(current, s)
    print('Destination', current)
    return abs(current.x) + abs(current.y)


def map_input(input):
    steps = list(map(map_input_to_step, input.split(', ')))
    return steps


def main():
    input_ = readFile('input')
    print(walk_steps(map_input(input_)))


if __name__ == '__main__':
    main()
