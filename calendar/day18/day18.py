# https://adventofcode.com/2021/day/18

import ast
import re
import itertools


def reduce(number: str):
    while True:
        exploded_number = explode(number)
        if exploded_number:
            number = exploded_number
            continue

        split_number = split(number)
        if split_number:
            number = split_number
            continue

        break

    return number


def split(number: str):
    match = re.search(r"\d{2,}", number)
    number_list = list(number)
    if match is not None:
        start = match.start()
        end = match.end()
        split_number = int(number[start:end])

        number_list[start:end] = ''
        number_list[start:start] = [
            '[', str(split_number // 2), ',', str(round(int(split_number / 2 + 0.5))), ']'
        ]
        return ''.join(number_list)

    return ''


def explode(number: str):
    number_list = list(number)

    depth = -1
    for i, c in enumerate(number):
        if c == '[' or c == ']':
            depth += int(c == '[')
            depth -= int(c == ']')
            continue

        if depth == 4:
            explode_number_match = re.match(r'^(\d+),(\d+)', number[i:])
            left, right = explode_number_match.groups()
            offset = explode_number_match.end()

            right_match = re.search(r'(\d+)', number[i + offset:])
            if right_match is not None:
                right_value = right_match.group(1)
                start = i + offset + right_match.start()
                end = start + len(right_value)
                number_list[start:end] = str(int(right_value) + int(right))

            number_list[i - 1:i + offset + 1] = '0'

            left_match = re.search(r'\d+(?=\D*$)', number[:i])
            if left_match is not None:
                left_value = left_match.group(1)
                start = left_match.start()
                end = start + len(left_value)
                number_list[start:end] = str(int(left_value) + int(left))

            return ''.join(number_list)

    return ''


def calculate_magnitude(number):
    if isinstance(number, int):
        return number

    return 3 * calculate_magnitude(number[0]) + 2 * calculate_magnitude(number[1])


# Part 1
with open('input.txt') as f:
    lines = f.readlines()

    reduced_sum = reduce(lines[0].strip())
    for line in lines[1:]:
        number_addition = '[' + reduced_sum + ',' + line.strip() + ']'
        number_addition = reduce(number_addition)
        reduced_sum = number_addition

    magnitude = calculate_magnitude(ast.literal_eval(reduced_sum))
    print(magnitude)


# Part 2
with open('input.txt') as f:
    lines = f.readlines()

    max_magnitude = max(
        [calculate_magnitude(ast.literal_eval(reduce(('[' + a.strip() + ',' + b.strip() + ']'))))
            for a, b in itertools.permutations(lines, 2)]
    )
    print(max_magnitude)
