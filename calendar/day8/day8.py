# https://adventofcode.com/2021/day/8

SEGMENT_COUNT_DIGIT_MAP = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

# Part 1
with open('input.txt') as f:
    lines = f.readlines()

    count = 0
    unique_counts = [k for k, v in SEGMENT_COUNT_DIGIT_MAP.items() if len(v) == 1]
    for line in lines:
        signal_patterns, output_patterns = map(lambda x: x.strip().split(), line.split('|'))
        count += len([digit_pattern for digit_pattern in output_patterns if len(digit_pattern) in unique_counts])

    print(count)


# Part 2
def get_signal_mapping(signal_patterns):
    digit_signal_map = {}

    for signal_pattern in signal_patterns:
        possible_digits = SEGMENT_COUNT_DIGIT_MAP[len(signal_pattern)]
        # Only one digit with the number of segments exists (2, 4, 7)
        if len(possible_digits) == 1:
            digit_signal_map[possible_digits[0]] = signal_pattern

    for signal_pattern in signal_patterns:
        signal_pattern_set = set(signal_pattern)
        # Three digits with 6 segments exist (0, 6, 9), differentiate them using the following rules:
        #   - The signal pattern represents a 6 if it is not a superset of 1
        #   - The signal pattern represents a 9 if it is a superset of 4
        #   - Else the signal pattern represents a 0
        if len(signal_pattern) == 6:
            if not set(digit_signal_map[1]) < signal_pattern_set:
                digit_signal_map[6] = signal_pattern
            elif set(digit_signal_map[4]) < signal_pattern_set:
                digit_signal_map[9] = signal_pattern
            else:
                digit_signal_map[0] = signal_pattern

    for signal_pattern in signal_patterns:
        signal_pattern_set = set(signal_pattern)
        # Three digits with 5 segments exist (2, 3, 5), differentiate them using the following rules:
        #   - The signal pattern represents a 3 if it is a superset of 1
        #   - The signal pattern represents a 5 if it is a subset of 9
        #   - Else the signal pattern represents a 2
        if len(signal_pattern) == 5:
            if set(digit_signal_map[1]) < signal_pattern_set:
                digit_signal_map[3] = signal_pattern
            elif signal_pattern_set < set(digit_signal_map[9]):
                digit_signal_map[5] = signal_pattern
            else:
                digit_signal_map[2] = signal_pattern

    return digit_signal_map


with open('input.txt') as f:
    lines = f.readlines()

    output_sum = 0
    for line in lines:
        signal_patterns, output_patterns = map(lambda x: x.strip().split(), line.split('|'))
        digit_signal_map = get_signal_mapping(signal_patterns)

        output = ''
        for digit_pattern in output_patterns:
            output += str(next(filter(
                lambda x: set(digit_signal_map[x]) == set(digit_pattern),
                digit_signal_map.keys())
            ))

        output_sum += int(output)

    print(output_sum)
