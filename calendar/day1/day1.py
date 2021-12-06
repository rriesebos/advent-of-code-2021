# https://adventofcode.com/2021/day/1

# Part 1
with open('input.txt') as f:
    lines = f.read().splitlines()

    increasing = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            increasing += 1

    print(increasing)


# Part 2
with open('input.txt') as f:
    lines = f.read().splitlines()

    increasing = 0
    for i in range(3, len(lines)):
        if int(lines[i]) > int(lines[i - 3]):
            increasing += 1

    print(increasing)
