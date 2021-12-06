# https://adventofcode.com/2021/day/3

# Part 1
with open('input.txt') as f:
    lines = f.read().splitlines()
    binary_length = len(lines[0])

    bit_counts = [0 for _ in range(binary_length)]
    for line in lines:
        for i, bit in enumerate(line):
            bit_counts[i] += int(bit)

    gamma_rate = [0 if bit_counts[i] < len(lines) / 2 else 1 for i in range(binary_length)]
    epsilon_rate = [1 - bit for bit in gamma_rate]

    gamma_rate = ''.join(map(str, gamma_rate))
    epsilon_rate = ''.join(map(str, epsilon_rate))

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)


# Part 2
def most_common_bit(lines, pos):
    bit_count = 0
    for line in lines:
        bit_count += int(line[pos])

    return 0 if bit_count < len(lines) / 2 else 1


def least_common_bit(lines, pos):
    bit_count = 0
    for line in lines:
        bit_count += int(line[pos])

    return 1 if bit_count < len(lines) / 2 else 0


def get_filtered_value(candidates, bit_criteria):
    for i in range(len(lines[0])):
        if len(candidates) == 1:
            break

        filter_bit = bit_criteria(candidates, i)
        candidates = list(filter(lambda l: int(l[i]) == filter_bit, candidates))

    return candidates[0]


with open('input.txt') as f:
    lines = f.read().splitlines()
    binary_length = len(lines[0])

    oxygen_generator_rating = get_filtered_value(lines, most_common_bit)
    co2_scrubber_rating = get_filtered_value(lines, least_common_bit)

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print(life_support_rating)
