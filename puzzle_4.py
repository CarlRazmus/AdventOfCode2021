bingo_boards = []

def remove_val_from_board(board, val, board_idx):
    for line in board:
        if val in line:
            line.remove(val)
            if len(line) == 0: # BINGO!!!
                score = get_score_of_board(board)
                bingo_boards.append(board_idx)
                print(str(val * score) + " score: " + str(score))

def get_score_of_board(board):
    return(sum(map(sum, board)))

if __name__ == "__main__":
    file = open("input.txt")
    lottery_nrs = [int(n) for n in file.readline().split(",")]
    row_boards = [[[int(n) for n in line.strip().split()] for line in board.split("\n")] for board in file.read().split("\n\n")]
    column_boards = [[list(i) for i in zip(*board)] for board in row_boards]

    for nr in lottery_nrs:
        for idx, row_board in enumerate(row_boards):
            if not idx in bingo_boards:
                remove_val_from_board(row_board, nr, idx)
        for idx, column_board in enumerate(column_boards):
            if not idx in bingo_boards:
                remove_val_from_board(column_board, nr, idx)