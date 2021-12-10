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

    scores = []
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
                    break
        else:
            # Add score if the line is not corrupt
            score = 0
            while stack:
                opening_symbol = stack.pop()
                closing_symbol = CHARACTER_PAIRS[opening_symbol]
                score = score * 5 + CHARACTER_SCORE[closing_symbol]
            scores.append(score)

    print(median(scores))
