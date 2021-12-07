# https://adventofcode.com/2021/day/7

# Part 1
with open('input.txt') as f:
    lines = f.readlines()
    positions = list(map(int, lines[0].split(',')))

    low = min(positions)
    high = max(positions)

    hist = {i: 0 for i in range(low, high)}
    for pos in positions:
        for i in range(low, high):
            hist[i] += abs(pos - i)

    print(min(hist.values()))


# Part 2
with open('input.txt') as f:
    lines = f.readlines()
    positions = list(map(int, lines[0].split(',')))

    low = min(positions)
    high = max(positions)

    hist = {i: 0 for i in range(low, high)}
    for pos in positions:
        for i in range(low, high):
            # Add the nth (n = distance) partial sum
            distance = abs(pos - i)
            hist[i] += int(distance * (distance + 1) / 2)

    print(min(hist.values()))
