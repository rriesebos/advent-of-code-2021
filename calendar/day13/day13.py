# https://adventofcode.com/2021/day/13

import re
from operator import itemgetter


def pretty_print_dots(dots: set):
    x_max, y_max = max(dots, key=itemgetter(0))[0] + 1, max(dots, key=itemgetter(1))[1] + 1
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) in dots:
                print('▇', end=' ')
            else:
                print('.', end=' ')

        print()


def fold_paper(dots: set, instructions: list):
    for axis, pos in instructions:
        new_dots = set()
        for dot in dots:
            if dot[axis] <= pos:
                new_dots.add(dot)
                continue

            new_dot = [0] * 2
            # Reflect dot about axis, pos
            new_dot[axis] = pos - (dot[axis] - pos)
            new_dot[1 - axis] = dot[1 - axis]
            new_dots.add(tuple(new_dot))

        dots = new_dots.copy()

    return dots


with open('input.txt') as f:
    lines = f.readlines()

    split_index = lines.index('\n')
    dot_coordinates = set([tuple(map(int, line.strip().split(','))) for line in lines[:split_index]])
    fold_instructions = [re.match(r'^fold along ([xy])=(\d+)$', line).groups() for line in lines[split_index + 1:]]
    # Map x, y to 0, 1 respectively
    fold_instructions = [(['x', 'y'].index(axis), int(pos)) for axis, pos in fold_instructions]

# Part 1
final_dots = fold_paper(dot_coordinates, [fold_instructions[0]])
print(len(final_dots))

# Part 2
final_dots = fold_paper(dot_coordinates, fold_instructions)
pretty_print_dots(final_dots)
