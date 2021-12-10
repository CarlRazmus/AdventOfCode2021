rows = [[x.strip().split(), y.strip().split()] for x, y in [l.split("|") for l in  open("input.txt").readlines()]]
unique_lengths = {1 : 2,
                  4 : 4,
                  7 : 3,
                  8 : 7}


def part_1():
    sum = 0
    for row in rows:    
        for output_string in row[1]:
            if len(output_string) in unique_lengths.values():
                sum += 1
    print(sum)

def isSubSegment(segment, sub_segment):
    for s in sub_segment:
        if not s in segment:
            return False
    return True

def get_value(inputs, outputs):
    answer_dict = {}
    for id in unique_lengths.keys():
         answer_dict[id] = ["".join(sorted(n)) for n in inputs if len(n) == unique_lengths[id]][0]
    
    #find 9 first since it is needed later
    for segment in ["".join(sorted(i)) for i in inputs]:
        if len(segment) == 6:
            if isSubSegment(segment, answer_dict[4]):
                answer_dict[9] = segment

    for segment in ["".join(sorted(i)) for i in inputs]:
        if len(segment) == 6:
            if isSubSegment(segment, answer_dict[4]):
                answer_dict[9] = segment
            elif isSubSegment(segment, answer_dict[1]):
                answer_dict[0] = segment
            else:
                answer_dict[6] = segment
        elif len(segment) == 5:
            if isSubSegment(segment, answer_dict[7]):
                answer_dict[3] = segment
            elif isSubSegment(answer_dict[9], segment):
                answer_dict[5] = segment
            else:
                answer_dict[2] = segment

    return_val = ""
    for output in ["".join(sorted(o)) for o in outputs]:
        
        return_val += str(list(answer_dict.keys())[list(answer_dict.values()).index(output)])
    #print(return_val)
    return return_val
    

def part_2():
    sum = 0
    for row in rows:
        sum += int(get_value(row[0], row[1]))
    print(sum)

if __name__ == "__main__":
    part_1()
    part_2()