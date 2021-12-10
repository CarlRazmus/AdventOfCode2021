lines = [[c for c in l.strip()] for l in open("input.txt").readlines()]
corresponding_endings = {"(" : ")", 
                         "[" : "]",
                         "<" : ">",
                         "{" : "}"}
failure_values = {")" : 3,
                  "]" : 57,
                  "}" : 1197,
                  ">" : 25137}
complete_points = {")" : 1,
                   "]" : 2,
                   "}" : 3,
                   ">" : 4}

def verify_chunks(chunks):
    expected_endings = list()
    for c in chunks:
        if c in corresponding_endings.keys():
            expected_endings.append(corresponding_endings[c])
        else:
            expected_chunk_ending = expected_endings.pop()
            if c != expected_chunk_ending:
                return failure_values[c]
    return 0

def complete_and_calc_score(chunks):
    total_points = 0
    expected_endings = list()
    for c in chunks:
        if c in corresponding_endings.keys():
            expected_endings.append(corresponding_endings[c])
        else:
            expected_endings.pop()
    for c in reversed(expected_endings):
        total_points *= 5
        total_points += complete_points[c]
    return total_points

def part_1():
    print(sum([verify_chunks(chunks) for chunks in lines]))

def part_2():
    incomplete_chunks = [chunks for chunks in lines if verify_chunks(chunks) == 0]
    scores = sorted([complete_and_calc_score(chunks) for chunks in incomplete_chunks])
    print(scores[int(len(scores) / 2 )])

if __name__ == "__main__":
    part_1() #436497
    part_2() #2377613374

