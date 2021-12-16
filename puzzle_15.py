from collections import defaultdict
import sys
import os
from numpy.core.shape_base import block
import psutil
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def reconstruct_path(preceding_nodes_dict, cave_map, start_node, node):
    current_node = node
    path_cost = 0
    while current_node != start_node:
        path_cost += cave_map[current_node]
        current_node = preceding_nodes_dict[current_node]
    memoryUsage.append(process.memory_info().rss / 1024)
    return path_cost


def manhattan_heuristic(node):
    return goal_node[0] - node[0] + goal_node[1] - node[1]


def get_neighbours(cave_map, node):
    neighbours = []
    for dimension in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbour = tuple(map(sum, zip(node, dimension)))
        if neighbour in cave_map.keys():
            neighbours.append(neighbour)
    return neighbours

def a_star(cave_map, start, goal, heuristic):
    queue = [start]
    preceding_nodes = {}

    g_score = defaultdict(lambda: sys.maxsize)
    g_score[start] = 0
    f_score = defaultdict(lambda: sys.maxsize)
    f_score[start] = heuristic(start)

    while queue is not None:
        memoryUsage.append(process.memory_info().rss / 1024)
        best_f_score = sys.maxsize
        for node in queue:
            if f_score[node] < best_f_score:
                best_f_score = f_score[node]
                current = node

        if current == goal:
            return reconstruct_path(preceding_nodes, cave_map, start, current)

        queue.remove(current)
        for neighbour in get_neighbours(cave_map, current):
            tentative_g_score = g_score[current] + cave_map[neighbour]
            if tentative_g_score < g_score[neighbour]:
                preceding_nodes[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour)
                if neighbour not in queue:
                    queue.append(neighbour)
    return None


def part_1(cave_map):
    print(a_star(cave_map, (0, 0), goal_node, manhattan_heuristic))


def part_2(cave_map):
    #memoryUsage.append(process.memory_info().rss / 1024)
    print(a_star(cave_map, (0, 0), new_goal_node, manhattan_heuristic))


def update_visual_graph():
    pass


if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    memoryUsage = list()
    cave_map_input = defaultdict(int)
    cave_map_visual_data = [[0 for _ in range(500)] for _ in range(500)]
    with open("input_15.txt") as f:
        for y_pos, row in enumerate(f.readlines()):
            for x_pos, danger_value in enumerate(row.strip()):
                cave_map_input[(x_pos, y_pos)] = int(danger_value)
                goal_node = (x_pos, y_pos)

    #part_1(cave_map_input)

    bigger_cave_map = {}
    start_height = sorted([y for x, y in cave_map_input.keys()])[-1] + 1
    start_width = sorted([x for x, y in cave_map_input.keys()])[-1] + 1
    for y in range(5):
        for x in range(5):
            for pos in cave_map_input.keys():
                x_pos_new = start_width * x + pos[0]
                y_pos_new = start_height * y + pos[1]
                added_value = x + y
                val_new = cave_map_input[pos] + added_value if cave_map_input[pos] + added_value <= 9 else cave_map_input[pos] + added_value - 9
                bigger_cave_map[x_pos_new, y_pos_new] = val_new
                new_goal_node = (x_pos_new, y_pos_new)

    for pos in bigger_cave_map.keys():
        cave_map_visual_data[pos[1]][pos[0]] = bigger_cave_map[pos] / 9

    c = ["darkgreen", "green", "palegreen", "red", "darkred"]
    v = [0, 0.1, 0.4, 0.6, 1]
    l = list(zip(v, c))
    cmap = colors.LinearSegmentedColormap.from_list('rg', l, N=256)
    fig, ax = plt.subplots()
    ax.imshow(cave_map_visual_data, cmap=cmap)
    #ax.matshow()

    axbackground = fig.canvas.copy_from_bbox(ax.bbox)
    plt.show()

    part_2(bigger_cave_map)
