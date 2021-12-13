def part_1(command, position):
    if command[0] == "up":
        position[1] -= command[1]
    elif command[0] == "down":
        position[1] += command[1]
    elif command[0] == "forward":
        position[0] += command[1]

def part_2(command, position):
    if command[0] == "up":
        position[2] -= command[1]
    elif command[0] == "down":
        position[2] += command[1]
    elif command[0] == "forward":
        position[0] += command[1]
        position[1] += command[1] * position[2]

def solve(position, func):
    for command in commands:
        func(command, position)
    print(position[0] * position[1])

if __name__ == "__main__":
    lines = open("input_2.txt")
    commands = [[c[0], int(c[1])] for c in [l.strip().split(" ") for l in lines]]
    solve([0, 0], part_1)
    solve([0, 0, 0], part_2)
