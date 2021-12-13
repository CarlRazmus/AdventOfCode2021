def part_1():
    print(len([n for idx, n in enumerate(numbers[1:]) if n > numbers[idx]]))


def part_2():
    print(len([idx for idx in range(len(numbers)-2) if sum(numbers[idx+1:idx+4]) > sum(numbers[idx:idx+3])]))


if __name__ == "__main__":
    with open("input_1.txt") as f:
        numbers = [int(n.strip()) for n in f]
    part_1()
    part_2()
