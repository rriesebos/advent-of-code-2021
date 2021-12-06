# https://adventofcode.com/2021/day/4


def read_board(lines):
    board = [list(map(int, row.replace('\n', '').replace('  ', ' ').strip().split(' '))) for row in lines]
    board = [[(num, False) for num in row] for row in board]
    return board


def update_board(drawn_number, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            num = board[i][j][0]
            if num == drawn_number:
                board[i][j] = (num, True)


def has_bingo(board):
    for i in range(len(board)):
        row = board[i]
        col = [row[i] for row in board]
        if all([x[1] for x in row]) or all([x[1] for x in col]):
            return True

    return False


def calc_score(board, final_number):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][1]:
                continue

            score += board[i][j][0]

    return score * final_number


# Part 1
with open('input.txt') as f:
    lines = f.readlines()
    lines = list(filter(lambda x: x != '\n', lines))

    numbers = list(map(int, lines[0].split(',')))
    boards = []
    for i in range(1, len(lines), 5):
        board = read_board(lines[i:i+5])
        boards.append(board)

    winners = []
    final_number = -1
    for num in numbers:
        for i, board in enumerate(boards):
            update_board(num, board)
            if has_bingo(board):
                winners.append(i)

        if winners:
            final_number = num
            break

    max_score = max([calc_score(boards[i], final_number) for i in winners])
    print(max_score)


# Part 2
with open('input.txt') as f:
    lines = f.readlines()
    lines = list(filter(lambda x: x != '\n', lines))

    numbers = list(map(int, lines[0].split(',')))
    boards = []
    for i in range(1, len(lines), 5):
        board = read_board(lines[i:i+5])
        boards.append(board)

    winners = []
    final_number = -1
    for num in numbers:
        for i, board in enumerate(boards):
            if i in winners:
                continue

            update_board(num, board)
            if has_bingo(board):
                winners.append(i)

        if len(winners) == len(boards):
            final_number = num
            break

    last_winner = boards[winners[-1]]
    last_winner_score = calc_score(last_winner, final_number)
    print(last_winner_score)
