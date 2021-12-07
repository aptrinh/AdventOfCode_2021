#-------------
#   Day 7.1+2/50
#-------------
def read_puzzle(file):
    with open(file) as f:
        return sorted([int(x) for x in f.readline().split(',')])


def solve(puzzle):
    length = len(puzzle)
    mid = puzzle[length//2]
    part1 = sum(abs(x-mid) for x in puzzle)

    mean = sum(puzzle) // length
    gauss = lambda x: x * (x+1) // 2
    part2 = sum(gauss(abs(x-mean)) for x in puzzle)

    return part1, part2  


print(solve(read_puzzle("E:\Projects\Coding\AdventOfCode_2021\Day7\Day7Input.txt")))
