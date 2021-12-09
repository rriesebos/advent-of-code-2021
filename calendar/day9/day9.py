# https://adventofcode.com/2021/day/9


from math import prod


def get_adjacent_positions(values, position):
    x, y = position
    adjacent_coordinates = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    return [(x + dx, y + dy) for dx, dy in adjacent_coordinates
            if 0 <= x + dx < len(values[0]) and 0 <= y + dy < len(values)]


def get_adjacent_values(values, position):
    return [values[y][x] for x, y in get_adjacent_positions(values, position)]


# Part 1
with open('input.txt') as f:
    lines = f.readlines()

    heightmap = [list(map(int, line.replace('\n', ''))) for line in lines]
    risk_levels = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            adjacent = get_adjacent_values(heightmap, position=(j, i))

            # Found a low point, add its risk level (value + 1) to the list of risk levels
            if heightmap[i][j] < min(adjacent):
                risk_levels.append(heightmap[i][j] + 1)

    print(sum(risk_levels))


# Part 2
def find_basin_size(heightmap, low_point):
    # Use DFS (depth first search) to find basin size
    stack = [low_point]
    visited = [low_point]
    size = 1
    while stack:
        position = stack.pop()
        adjacent_positions = get_adjacent_positions(heightmap, position)

        for adjacent_position in adjacent_positions:
            if adjacent_position not in visited and heightmap[adjacent_position[1]][adjacent_position[0]] < 9:
                stack.append(adjacent_position)
                visited.append(adjacent_position)
                size += 1

    return size


with open('input.txt') as f:
    lines = f.readlines()

    heightmap = [list(map(int, line.replace('\n', ''))) for line in lines]
    basin_sizes = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            adjacent_values = get_adjacent_values(heightmap, position=(j, i))

            # Found a low point, find the size of the corresponding basin
            if heightmap[i][j] < min(adjacent_values):
                basin_size = find_basin_size(heightmap, low_point=(j, i))
                basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    three_largest_basins = basin_sizes[:3]
    print(prod(three_largest_basins))
