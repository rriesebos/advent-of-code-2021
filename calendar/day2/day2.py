# https://adventofcode.com/2021/day/2

import re

# Part 1
with open('input.txt') as f:
    lines = f.read().splitlines()

    position = 0
    depth = 0
    for line in lines:
        command, distance = re.match(r'^([a-z]*) (\d)$', line).groups()
        distance = int(distance)

        if command == 'forward':
            position += distance
        elif command == 'down':
            depth += distance
        elif command == 'up':
            depth -= distance

    print(position * depth)


# Part 2
with open('input.txt') as f:
    lines = f.read().splitlines()

    position = 0
    depth = 0
    aim = 0
    for line in lines:
        command, distance = re.match(r'^([a-z]*) (\d)$', line).groups()
        distance = int(distance)

        if command == 'forward':
            position += distance
            depth += aim * distance
        elif command == 'down':
            aim += distance
        elif command == 'up':
            aim -= distance

    print(position * depth)
