from collections import namedtuple
import itertools

Step = namedtuple('Step', 'direction_change steps')
Point = namedtuple('Point', 'direction x y')


def read_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as f:
        return f.read()


def map_input_to_step(input_, single_steps=False):
    if input_[0] == 'R':
        direction_change = 1
    elif input_[0] == 'L':
        direction_change = -1
    else:
        raise RuntimeError(f"{input_} can't be mapped")

    step_count = int(input_[1:])
    if single_steps:
        steps = [Step(direction_change, 1)]
        steps.extend([Step(0, 1) for _ in range(1, step_count)])
        return steps
    else:
        return Step(direction_change, step_count)


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


def walk_steps(steps, search_visited_twice=False):
    current = Point(direction=0, x=0, y=0)
    visited = []
    for s in steps:
        if not search_visited_twice:
            current = walk(current, s)
        else:
            visited.append(current)
            current = walk(current, s)
            if any(p for p in visited if p.x == current.x and p.y == current.y):
                break
    print('Destination', current)
    return abs(current.x) + abs(current.y)


def map_input(input_, single_steps=False):
    if single_steps:
        steps = []
        for i in input_.split(', '):
            steps.extend(map_input_to_step(i, True))
    else:
        steps = list(map(map_input_to_step, input_.split(', ')))
    return steps


def main():
    input_ = read_file('input')
    print(walk_steps(map_input(input_)))
    print(walk_steps(map_input(input_, single_steps=True), search_visited_twice=True))


if __name__ == '__main__':
    main()
