from collections import defaultdict


crab_positions = sorted([int(n) for n in open("input.txt").read().strip().split(",")])
linear_fuel_cost_dict = defaultdict(int)
nonlinear_fuel_cost_dict = defaultdict(int)
for pos in range(max(crab_positions) + 1):
    for crab_pos in crab_positions:
        pos_diff = abs(pos - crab_pos)
        linear_fuel_cost_dict[pos] += abs(pos - crab_pos)
        if pos_diff > 0:
            nonlinear_fuel_cost_dict[pos] += sum(range(1, abs(pos - crab_pos) + 1))

print(min(linear_fuel_cost_dict.values()))
print(min(nonlinear_fuel_cost_dict.values()))
