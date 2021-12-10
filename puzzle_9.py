cave = [[int(n) for n in l.strip()] for l in open("input.txt").readlines()]
print(cave)

def check_if_low_point(x, y, height):
    sum_surrounding_points = 0
    if x > 0:
        if height < cave[y][x-1]:
            sum_surrounding_points += cave[y][x-1]
        else:
            return False
    if x < len(cave[0]) - 1:
        if height < cave[y][x+1]:
            sum_surrounding_points += cave[y][x+1]
        else:
            return False
    if y > 0:
        if height < cave[y-1][x]:
            sum_surrounding_points += cave[y-1][x]
        else:
            return False
    if y < len(cave) - 1:
        if height < cave[y+1][x]:
            sum_surrounding_points += cave[y+1][x]
        else:
            return False
    return True

def part_1():
    total_score = 0
    for y, row in enumerate(cave):
        for x, height in enumerate(row):
            if check_if_low_point(x, y, height):
                total_score += 1 + cave[y][x]
    print(total_score)

def get_nr_neighbours(location, non_explored_locations):
    non_explored_locations.remove(location)
    x, y = location
    if cave[y][x] == 9:
        return 0
    nr_neighbours = 0
    for x_next, y_next in [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]:
        if x_next > 0 and x_next < len(cave[0]) - 1 and y_next > 0 and y_next < len(cave) - 1:
            if (x_next, y_next) in non_explored_locations:
                nr_neighbours += get_nr_neighbours((x_next, y_next), non_explored_locations)
    return 1 + nr_neighbours

def part_2():
    non_explored_locations = []
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            non_explored_locations.append((x,y))
    basin_sizes = []
    while len(non_explored_locations) > 0:
        basin_sizes.append(get_nr_neighbours(non_explored_locations[0], non_explored_locations))
    basin_sizes.sort()
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])

if __name__ == "__main__":
    part_1()
    part_2()