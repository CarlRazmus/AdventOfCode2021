from collections import defaultdict

def breedBruteForce(jellyfishes):
    new_jellies = []
    for idx, jelly in enumerate(jellyfishes):
        if jelly > 0:
            jellyfishes[idx] = jelly - 1
        else:
            jellyfishes[idx] = 6
            new_jellies.append(8)
    jellyfishes += new_jellies

def breedSmart(jelly_dict):
    new_jellies = jelly_dict[0]
    
    for age in range(8):
        jelly_dict[age] = jelly_dict[age + 1]
    jelly_dict[6] += new_jellies
    jelly_dict[8] = new_jellies

def part_1(jellyfishes):
    for _ in range(80):
        breedBruteForce(jellyfishes)
    print(len(jellyfishes))

def part_2(jelly_dict):
    for _ in range(256):
        breedSmart(jelly_dict)
    print(sum([n for n in jelly_dict.values()]))
        
if __name__ == "__main__":
    jellyfishes = [int(n) for n in open("input.txt").read().split(",")]
    jelly_dict = defaultdict(int)
    for jelly in jellyfishes:
        jelly_dict[jelly] += 1
        
    part_1(jellyfishes)
    part_2(jelly_dict)