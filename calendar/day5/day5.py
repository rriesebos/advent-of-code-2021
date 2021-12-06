# https://adventofcode.com/2021/day/5

import re

# Part 1
with open('input.txt') as f:
    lines = f.readlines()

    hist = {}
    for line in lines:
        start_x, start_y, end_x, end_y = map(int, re.match(r'^(\d+),(\d+) -> (\d+),(\d+)$', line).groups())
        if start_x == end_x:
            for i in range(min(start_y, end_y), max(start_y + 1, end_y + 1)):
                hist[(start_x, i)] = hist[(start_x, i)] + 1 if (start_x, i) in hist else 1

        if start_y == end_y:
            for i in range(min(start_x, end_x), max(start_x + 1, end_x + 1)):
                hist[(i, start_y)] = hist[(i, start_y)] + 1 if (i, start_y) in hist else 1

    print(len({k: v for k, v in hist.items() if v > 1}))


# Part 2
with open('input.txt') as f:
    lines = f.readlines()

    hist = {}
    for line in lines:
        start_x, start_y, end_x, end_y = map(int, re.match(r'^(\d+),(\d+) -> (\d+),(\d+)$', line).groups())

        dir_x = 1 if start_x < end_x else -1 if start_x > end_x else 0
        dir_y = 1 if start_y < end_y else -1 if start_y > end_y else 0
        while start_x != end_x + dir_x or start_y != end_y + dir_y:
            hist[(start_x, start_y)] = hist[(start_x, start_y)] + 1 if (start_x, start_y) in hist else 1
            start_x += dir_x
            start_y += dir_y

    print(len({k: v for k, v in hist.items() if v > 1}))
