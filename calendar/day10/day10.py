# https://adventofcode.com/2021/day/10

from statistics import median

CHARACTER_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

# Part 1
with open('input.txt') as f:
    CHARACTER_SCORE = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    lines = f.readlines()

    illegal_counts = {c: 0 for c in CHARACTER_PAIRS.values()}
    for line in lines:
        chunks = line.replace('\n', '')

        stack = []
        for c in chunks:
            if c in CHARACTER_PAIRS:
                stack.append(c)
            else:
                opening_symbol = stack.pop()
                closing_symbol = CHARACTER_PAIRS[opening_symbol]
                # Incorrect closing symbol, chunk is corrupted
                if closing_symbol != c:
                    illegal_counts[c] += 1
                    break

    print(sum(CHARACTER_SCORE[k] * v for k, v in illegal_counts.items()))


# Part 2
with open('input.txt') as f:
    CHARACTER_SCORE = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    lines = f.readlines()

    completion_strings = []
    for line in lines:
        chunks = line.replace('\n', '')

        stack = []
        corrupt = False
        for c in chunks:
            if c in CHARACTER_PAIRS:
                stack.append(c)
            else:
                opening_symbol = stack.pop()
                closing_symbol = CHARACTER_PAIRS[opening_symbol]
                # Incorrect closing symbol, chunk is corrupted
                if closing_symbol != c:
                    corrupt = True
                    break

        if not corrupt:
            # Add completion string if the line is not corrupt
            completion_strings.append([CHARACTER_PAIRS[c] for c in reversed(stack)])

    scores = []
    for completion_string in completion_strings:
        score = 0
        for c in completion_string:
            score *= 5
            score += CHARACTER_SCORE[c]
        scores.append(score)

    print(median(scores))
