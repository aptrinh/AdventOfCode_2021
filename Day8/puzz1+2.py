#-------------
#   Day 8.1+2/50
#-------------
from collections import Counter


with open("E:\Projects\Coding\AdventOfCode_2021\Day8\Day8Input.txt") as d:
    data = [x.strip().split("|") for x in d.readlines()]

# Each segment appears a certain number of times in the digits 0--9
# Each number has a unique pattern of segment occurences.

# So first, build a dictionary mapping segment occurence patterns to
# the numbers they represent.


def occurence_counter(s):
    return Counter(list(s.replace(" ", "")))

def occurence_pattern(s, ctr):
    return tuple(sorted([ctr[x] for x in s]))

# Digits 0--9 in order according to a particular labelling of segments
canonical_pattern = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
canonical_dict = occurence_counter(canonical_pattern)

# Build the translator dictionary using the canonical pattern to give segment occurences
translator = {}
for i, x in enumerate(canonical_pattern.split(" ")):
    translator[occurence_pattern(x, canonical_dict)] = i

# Then put it to work.


def process_line(ls):
    outputs = ls[1].strip()
    occ_dict = occurence_counter(ls[0])
    return [translator[occurence_pattern(x, occ_dict)] for x in outputs.split(" ")]


part_one = 0
part_two = 0
for line in data:
    p = process_line(line)
    part_one += len([x for x in p if x in [1, 4, 7, 8]])
    part_two += int("".join([str(x) for x in p]))


print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")