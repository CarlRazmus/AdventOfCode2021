import operator

def getMostOrLeastCommonNr(l, op):
    return 0 if op(l.count(0), l.count(1)) else 1

def calc_rating(input_matrix, op, idx):
    if len(input_matrix) == 1:
        return input_matrix[0]
    flipped_input_matrix = [list(i) for i in zip(*input_matrix)]
    most_or_least_common_nr = getMostOrLeastCommonNr(flipped_input_matrix[idx], op)
    new_matrix = [l for l in input_matrix if most_or_least_common_nr == l[idx]]
    return calc_rating(new_matrix, op, idx + 1)

def part1():
    input_matrix = [[int(n) for n in l] for l in [line.strip() for line in open("input.txt")]]
    flipped_input_matrix = [list(i) for i in zip(*input_matrix)]
    gamma_rate = "".join([str(getMostOrLeastCommonNr(l, operator.gt)) for l in flipped_input_matrix])
    epsilon = "".join([str(getMostOrLeastCommonNr(l, operator.lt)) for l in flipped_input_matrix])
    print(int(str(gamma_rate), 2) * int(str(epsilon), 2))

def part2():
    input_matrix = [[int(n) for n in l] for l in [line.strip() for line in open("input.txt")]]
    oxygen_rate = int("".join(str(x) for x in calc_rating(input_matrix, operator.gt, 0)), 2)
    other_rate = int("".join(str(x) for x in calc_rating(input_matrix, operator.le, 0)), 2)
    print(oxygen_rate * other_rate)

if __name__ == "__main__":
    part1()
    part2()