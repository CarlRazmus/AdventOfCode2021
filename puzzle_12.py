import re
from collections import defaultdict
from collections import Counter

edges = [re.match(r"(\w+)-(\w+)", l).groups() for l in open("input.txt")]
graph = defaultdict(set)

for edge in edges:
    node1, node2 = edge
    graph[node1].add(node2)
    graph[node2].add(node1)

paths = list()


def paths_to_end(node, path, verifier):
    global paths
    if node == "end":
        paths.append(path)
        return
    for neighbour in graph[node]:
        if verifier(neighbour, path):
            new_path = path.copy()
            new_path.append(neighbour)
            paths_to_end(neighbour, new_path, verifier)


def part_2_verifier(node, path):
    if node == "start":
        return False
    if node not in path:
        return True
    if node.isupper():
        return True
    if not [n for n in path if n.islower() and path.count(n) > 1]:
        return True
    return False


def part_1_verifier(node, path):
    return node not in path or (node in path and node.isupper())


def part_1():
    paths_to_end("start", ["start"], part_1_verifier)
    print(len(paths))


def part_2():
    paths_to_end("start", ["start"], part_2_verifier)
    print(len(paths))


if __name__ == "__main__":
    #part_1()
    part_2()