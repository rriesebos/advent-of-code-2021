# https://adventofcode.com/2021/day/12

connections = {}
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        start, to = line.replace('\n', '').split('-')
        connections[start] = connections[start] + [to] if start in connections else [to]
        connections[to] = connections[to] + [start] if to in connections else [start]


# Part 1
def find_paths(connections, node, visited, path, paths):
    visited[node] = node.islower()
    path.append(node)

    if node == 'end':
        # Could be replaced with global count variable (if only path count is needed)
        paths.append(path.copy())
    else:
        for neighbour in connections[node]:
            if not visited[neighbour]:
                find_paths(connections, neighbour, visited, path, paths)

    path.pop()
    visited[node] = False


paths = []
visited = {k: False for k in connections.keys()}
find_paths(connections, 'start', visited, [], paths)
print(len(paths))


# Part 2
def find_paths(connections, node, visited, visited_twice, path, paths):
    visited[node] += 1 if node.islower() else 0
    path.append(node)

    if node == 'end':
        paths.append(path.copy())
    else:
        for neighbour in connections[node]:
            if visited[neighbour] == 0:
                find_paths(connections, neighbour, visited, visited_twice, path, paths)
            elif neighbour != 'start' and neighbour != 'end' and not visited_twice:
                # If the neighbour has been visited, and no node has been visited twice
                # recur with the neighbour as visited twice
                find_paths(connections, neighbour, visited, neighbour, path, paths)

    path.pop()
    visited[node] -= 1 if node.islower() else 0


paths = []
visited = {k: 0 for k in connections.keys()}
find_paths(connections, 'start', visited, '', [], paths)

print(len(paths))
