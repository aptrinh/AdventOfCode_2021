#-------------
#   Day 5.1+2/50
#-------------

import re
points, part2 = dict(), False
for x1,y1,x2,y2 in [[int(i) for i in re.split(' -> |,', line.strip())] for line in open("E:\Projects\Coding\AdventOfCode_2021\Day5\Day5Input.txt").readlines()]:
    if x1==x2 or y1==y2 or (part2 and abs(x2-x1) == abs(y2-y1)):
        rx = range(x1, x2 - 1 if x2 < x1 else x2 + 1, 1 if x2 > x1 else -1) if x1 != x2 else [x1] * (abs(y2-y1) + 1)
        ry = range(y1, y2 - 1 if y2 < y1 else y2 + 1, 1 if y2 > y1 else -1) if y1 != y2 else [y1] * (abs(x2-x1) + 1)
        for r in zip(rx, ry):
            points[r] = points.get(r, 0) + 1
print(sum(0 if i < 2 else 1 for i in points.values()))