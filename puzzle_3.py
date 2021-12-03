def part1():
    gamma_rate = ""
    lines = [line.strip() for line in open("input.txt")]

    for idx in range(len(lines[0])):
        count = [0,0]
        for line in lines:
            count[int(line[idx])] = count[int(line[idx])] + 1
        gamma_rate += str((0 if count[0] > count[1] else 1))
    epsilon = ""
    for n in gamma_rate:
        epsilon += str(1 - int(n))
    print(int(str(gamma_rate), 2) * int(str(epsilon), 2))

def getMostCommonNumber(l, equal_nr):
    zeroes = l.count(0)
    ones = l.count(1)
    if zeroes == ones:
        return equal_nr
    else:
        return 1 if ones > zeroes else 0

def getLeastCommonNumber(l, equal_nr):
    zeroes = l.count(0)
    ones = l.count(1)
    if zeroes == ones:
        return equal_nr
    else:
        return 1 if ones < zeroes else 0

def calc_oxygen_generator_rating(input_matrix, idx):
    if len(input_matrix) == 1:
        return input_matrix[0]
    flipped_input_matrix = [list(i) for i in zip(*input_matrix)]
    most_common_nr = getMostCommonNumber(flipped_input_matrix[idx], 1)
    new_matrix = []
    for l in input_matrix:
        if most_common_nr == l[idx]:
            new_matrix.append(l) 

    return calc_oxygen_generator_rating(new_matrix, idx + 1)

def calc_other_rating(input_matrix, idx):
    if len(input_matrix) == 1:
        return input_matrix[0]
    flipped_input_matrix = [list(i) for i in zip(*input_matrix)]
    most_common_nr = getLeastCommonNumber(flipped_input_matrix[idx], 0)
    new_matrix = []
    for l in input_matrix:
        if most_common_nr == l[idx]:
            new_matrix.append(l) 
    return calc_other_rating(new_matrix, idx + 1)

def part2():
    input_lines = [line.strip() for line in open("input.txt")]
    input_matrix = []
    for l in input_lines:
        input_matrix.append([int(n) for n in l])

    oxygen_rate = int("".join(str(x) for x in calc_oxygen_generator_rating(input_matrix, 0)), 2)
    other_rate = int("".join(str(x) for x in calc_other_rating(input_matrix, 0)), 2)
    
    print(oxygen_rate * other_rate)

if __name__ == "__main__":
    part2()
