# https://adventofcode.com/2021/day/7

import statistics

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


# Part 1, alternative (using median)
with open('input.txt') as f:
    lines = f.readlines()
    positions = list(map(int, lines[0].split(',')))

    median = statistics.median(positions)
    print(int(sum([(abs(pos - median)) for pos in positions])))


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
            hist[i] += distance * (distance + 1) // 2

    print(min(hist.values()))


# Part 2, alternative (using mean)
with open('input.txt') as f:
    lines = f.readlines()
    positions = list(map(int, lines[0].split(',')))

    def partial_sum(n):
        return n * (n + 1) // 2

    mean = round(statistics.mean(positions))
    print(min(sum([int(partial_sum(abs(pos - (mean - 1)))) for pos in positions]),
              sum([int(partial_sum(abs(pos - mean))) for pos in positions])))
