import re


def fold_x(paper, position):
    folded_paper = [row[:position] for row in paper]
    for idx_y, row in enumerate(paper):
        for idx_x, val in enumerate(row[position+1:]):
            folded_paper[idx_y][(-1) - idx_x] += val
    return folded_paper


def fold_y(paper, position):
    paper = [list(x) for x in zip(*paper)]
    paper = fold_x(paper, position)
    return [list(x) for x in zip(*paper)]


def part_1(paper, fold_instruction):
    fold_pos = int(fold_instruction[1])
    paper = fold_x(paper, fold_pos) if fold_instruction[0] == "x" else fold_y(paper, fold_pos)
    print(sum([sum([1 for x in y if x > 0]) for y in paper]))


def part_2(paper, fold_instructions):
    for fold_instruction in fold_instructions:
        fold_dir = fold_instruction[0]
        fold_pos = int(fold_instruction[1])
        paper = fold_x(paper, fold_pos) if fold_dir == "x" else fold_y(paper, fold_pos)

    for row in [["X" if x > 0 else "0" for x in y] for y in paper]:
        print("".join(row))


if __name__ == "__main__":
    with open("input.txt") as f:
        inputs = f.read().split("\n\n")
    dots = [[int(x), int(y)] for x, y in [p.split(",") for p in inputs[0].split("\n")]]
    folds = [re.match(r"fold along (\w)=(\d+)", l).groups() for l in inputs[1].split("\n")]
    max_x = sorted([dot[0] for dot in dots])[-1]
    max_y = sorted([dot[1] for dot in dots])[-1]
    paper = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for dot in dots:
        paper[dot[1]][dot[0]] = 1

    part_1(paper, folds[0])
    part_2(paper, folds)
