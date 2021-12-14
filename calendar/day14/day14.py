# https://adventofcode.com/2021/day/14

import re
from collections import Counter


with open('input.txt') as f:
    lines = f.readlines()

    polymer_template = lines[0].strip()
    pair_insertion_rules = {}
    for line in lines[2:]:
        pair, insert = re.match(r'^([A-Z]{2}) -> ([A-Z])$', line).groups()
        pair_insertion_rules[pair] = insert


# Part 1
polymer = polymer_template
for step in range(10):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        new_polymer += (pair[0] if i == 0 else "") + pair_insertion_rules[pair] + pair[1]
    polymer = new_polymer

frequencies = Counter(polymer)
print(frequencies.most_common()[0][1] - frequencies.most_common()[-1][1])

# Part 2
pair_frequencies = {k: polymer_template.count(k) for k in pair_insertion_rules.keys()}
frequencies = Counter(polymer_template)
for step in range(40):
    new_pair_frequencies = {k: 0 for k in pair_insertion_rules.keys()}
    for pair, count in pair_frequencies.items():
        if count == 0:
            continue

        insert_value = pair_insertion_rules[pair]
        for new_pair in [pair[0] + insert_value, insert_value + pair[1]]:
            new_pair_frequencies[new_pair] += count

        frequencies[insert_value] += count

    pair_frequencies = new_pair_frequencies.copy()

print(max(frequencies.values()) - min(frequencies.values()))
