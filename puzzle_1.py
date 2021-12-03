def part_1():
    lines = open("input.txt")
    numbers = [int(n.strip()) for n in lines]
    c = 0 
    prev_number = 99999999999999999999
    for number in numbers:
        if number > prev_number:
            c = c + 1
        prev_number = number
    print(c)

def part_2():
    lines = open("input.txt")
    numbers = [int(n.strip()) for n in lines]
    c = 0 
    prev_value = 99999999999999999999
    for idx, number in enumerate(numbers):
        if idx + 3 <= len(numbers):
            value = sum(numbers[idx : idx+3])
            print(numbers[idx : idx+3])
            if value > prev_value:
                c = c + 1
            prev_value = value
    print(c)


if __name__ == "__main__":
    #part_1()
    part_2()