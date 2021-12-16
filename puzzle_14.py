from collections import defaultdict
import re


def part_1():
    solver(10)


def part_2():
    solver(40)


def solver(iterations):
    pair_count = input_pair_count
    for _ in range(iterations):
        pair_count = update_pair_count(pair_count)
    alphabet_count = defaultdict(int)
    for pair in pair_count:
        alphabet_count[pair[0]] += pair_count[pair]
        alphabet_count[pair[1]] += pair_count[pair]
    sorted_values = sorted(alphabet_count.values())
    print(int((sorted_values[-1] - sorted_values[0] + 1) / 2))


def update_pair_count(pair_count):
    new_pair_count = defaultdict(int)
    for pair in pair_count.keys():
        if pair in rules.keys():
            new_pair_count[pair[0] + rules[pair]] += pair_count[pair]
            new_pair_count[rules[pair] + pair[1]] += pair_count[pair]
        else:
            new_pair_count[pair] += pair_count[pair]
    return new_pair_count


if __name__ == "__main__":
    with open("input_14.txt") as f:
        polymer = f.readline().strip()
        f.readline()
        rules = {x: y for x, y in [re.match(r"(\w\w) -> (\w)", rule).groups() for rule in f.readlines()]}
        input_pair_count = defaultdict(int)
        for idx in range(len(polymer) - 1):
            input_pair_count[polymer[idx:idx+2]] += 1
    part_1()
    part_2()
