# https://adventofcode.com/2021/day/15


import heapq


def get_adjacent_positions(values, position):
    x, y = position
    adjacent_coordinates = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    return [(x + dx, y + dy) for dx, dy in adjacent_coordinates
            if 0 <= x + dx < len(values[0]) and 0 <= y + dy < len(values)]


def dijkstra(nodes, start, end):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        cost, position = heapq.heappop(priority_queue)

        if position == end:
            return cost

        if position in visited:
            continue

        visited.add(position)

        for neighbour in get_adjacent_positions(nodes, position):
            neighbour_cost = nodes[neighbour[1]][neighbour[0]]
            heapq.heappush(priority_queue, (cost + neighbour_cost, neighbour))


with open('input.txt') as f:
    lines = f.readlines()
    risk_levels = [list(map(int, line.replace('\n', ''))) for line in lines]


# Part 1
risk = dijkstra(risk_levels, (0, 0), (len(risk_levels[0]) - 1, len(risk_levels) - 1))
print(risk)

# Part 2
start_height, start_width = len(risk_levels), len(risk_levels[0])

# Expand risk levels map to be 5 x 5
for _ in range(4):
    for row in risk_levels:
        row.extend([val + 1 if val < 9 else 1 for val in row[-start_height:]])

for _ in range(4):
    for row in risk_levels[-start_width:]:
        risk_levels.append([val + 1 if val < 9 else 1 for val in row])

risk = dijkstra(risk_levels, (0, 0), (len(risk_levels[0]) - 1, len(risk_levels) - 1))
print(risk)
