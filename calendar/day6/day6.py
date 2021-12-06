# https://adventofcode.com/2021/day/6


def get_lanternfish_count(start_population, days):
    hist = {}
    for num in start_population:
        hist[num] = hist[num] + 1 if num in hist else 1

    for day in range(days):
        new_hist = {i: 0 for i in range(9)}
        for k, v in hist.items():
            if k == 0:
                new_hist[6] += v
                new_hist[8] += v
            else:
                new_hist[k - 1] += v

        hist = new_hist.copy()

    return sum(hist.values())


# Part 1
with open('input.txt') as f:
    lines = f.readlines()
    lanternfish = list(map(int, lines[0].split(',')))
    print(get_lanternfish_count(lanternfish, 80))


# Part 2
with open('input.txt') as f:
    lines = f.readlines()
    lanternfish = list(map(int, lines[0].split(',')))
    print(get_lanternfish_count(lanternfish, 256))
