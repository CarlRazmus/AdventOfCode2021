
flashes = 0

def flash(octopuses, pos):
    global flashes
    flashes += 1
    octopuses[pos] = (0, True)
    for row in range(-1, 2):
        for col in range(-1, 2):
            neighbour_pos = (pos[0] + row, pos[1] + col)
            if neighbour_pos in octopuses.keys() and not octopuses[neighbour_pos][1]:
                new_energy = octopuses[neighbour_pos][0] + 1
                octopuses[neighbour_pos] = (new_energy, False)
                if new_energy > 9:
                    flash(octopuses, neighbour_pos)


def part_1(octopuses):
    global flashes
    for _ in range(100):
        octopuses = {key : (octopuses[key][0] + 1, False) for key in octopuses.keys()}
        for pos in octopuses.keys():
            if octopuses[pos][0] > 9 and not octopuses[pos][1]:
                flash(octopuses, pos)
    print(flashes)


def part_2(octopuses):
    count = 0
    while sum([o[0] for o in octopuses.values()]) > 0:
        count += 1
        octopuses = {key : (octopuses[key][0] + 1, False) for key in octopuses.keys()}
        for pos in octopuses.keys():
            if octopuses[pos][0] > 9 and not octopuses[pos][1]:
                flash(octopuses, pos)
    print(count)


if __name__ == "__main__":
    octopuses = {}
    for row, l in enumerate(open("input.txt")):
        for col, o in enumerate(l.strip()):
            octopuses[(row, col)] = (int(o), False)
    print(octopuses)
    #part_1(octopuses)
    part_2(octopuses)
