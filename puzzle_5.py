def addLine(board, line, skip_diagonals):
    start = [int(n) for n in line[0]]
    end = [int(n) for n in line[1]]
    direction = [end[0] - start[0], end[1] - start[1]]
    length = max(abs(direction[0]), abs(direction[1]))
    normalized_direction = [int(direction[0] / length), int(direction[1] / length)]
    if skip_diagonals and normalized_direction[0] != 0 and normalized_direction[1] != 0:
        return 
    for i in range(length + 1):
        x_pos = start[0] + i * normalized_direction[0]
        y_pos = start[1] + i * normalized_direction[1]
        board[y_pos][x_pos] = board[y_pos][x_pos] + 1

def sum_of_board(board):
    nr_overlaps = 0
    for row in board:
        for x in row:
            if x > 1:
                nr_overlaps += 1
    print("nr_overlaps " + str(nr_overlaps))
    return sum([sum([1 for x in y if x > 1]) for y in board])      

def part_1(board):
    for line in lines:
        addLine(board, line, True)
    print(sum_of_board(board))

def part_2(board):
    for line in lines:
        addLine(board, line, False)
    print(sum_of_board(board))

if __name__ == "__main__":
    lines = [[p[0].split(","), p[1].split(",")] for p in [l.strip().split(" -> ") for l in open("input.txt").readlines()]]
    #lines = [map(int, z) for z in [y for y in [x for x in lines]]]
    #lines = [[[int(n) for n in z] for z in [y for y in [x for x in lines]]]]
    max_y = 0
    max_x = 0
    for line in lines:
        for pos in line:
            if int(pos[0]) > max_x:
                max_x = int(pos[0])
            if int(pos[1]) > max_y:
                max_y = int(pos[1])
    board1 = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]   
    board2 = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]   
    
    part_1(board1)
    part_2(board2)




