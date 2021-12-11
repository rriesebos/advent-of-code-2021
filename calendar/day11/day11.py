# https://adventofcode.com/2021/day/11


def get_neighbour_positions(values, position):
    x, y = position
    neighbour_positions = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) != (0, 0) and 0 <= x + dx < len(values[0]) and 0 <= y + dy < len(values):
                neighbour_positions.append((x + dx, y + dy))
    return neighbour_positions


# Part 1
with open('input.txt') as f:
    lines = f.readlines()
    energy_levels = [list(map(int, line.replace('\n', ''))) for line in lines]

    flashes = 0
    for step in range(100):
        energy_levels = [[level + 1 if level < 9 else 0 for level in levels] for levels in energy_levels]
        stack = [(x, y) for y in range(len(energy_levels)) for x in range(len(energy_levels[0]))
                 if energy_levels[y][x] == 0]
        flashes += len(stack)

        while stack:
            flash_position = stack.pop()
            flash_neighbour_positions = get_neighbour_positions(energy_levels, flash_position)
            for x, y in flash_neighbour_positions:
                energy_levels[y][x] += 0 if energy_levels[y][x] == 0 else 1
                if energy_levels[y][x] > 9:
                    energy_levels[y][x] = 0
                    stack.append((x, y))
                    flashes += 1

    print(flashes)


# Part 2
with open('input.txt') as f:
    lines = f.readlines()
    energy_levels = [list(map(int, line.replace('\n', ''))) for line in lines]

    step = 0
    flash_count = sum(row.count(0) for row in energy_levels)
    while flash_count < len(energy_levels) * len(energy_levels[0]):
        energy_levels = [[level + 1 if level < 9 else 0 for level in levels] for levels in energy_levels]
        stack = [(x, y) for y in range(len(energy_levels)) for x in range(len(energy_levels[0]))
                 if energy_levels[y][x] == 0]

        while stack:
            flash_position = stack.pop()
            flash_neighbour_positions = get_neighbour_positions(energy_levels, flash_position)
            for x, y in flash_neighbour_positions:
                energy_levels[y][x] += 0 if energy_levels[y][x] == 0 else 1
                if energy_levels[y][x] > 9:
                    energy_levels[y][x] = 0
                    stack.append((x, y))

        flash_count = sum(row.count(0) for row in energy_levels)
        step += 1

    print(step)
