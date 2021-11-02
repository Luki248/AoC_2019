# Advent of Code
# Day 1
# https://adventofcode.com/2019/day/1

import math

input = [int(line.rstrip('\n')) for line in open("input.txt")]

# Puzzle 1
sum = 0
for mass in input:
    fuel = math.floor(mass / 3) - 2
    sum += fuel
print("First Puzzle:", sum)


def calc_fuel(mass):
    sum = math.floor(mass / 3) - 2
    if sum <= 0:
        return 0
    else:
        return sum + calc_fuel(sum)

# Puzzle 2
sum = 0
for mass in input:
    sum += calc_fuel(mass)
print("Second Puzzle:", sum)