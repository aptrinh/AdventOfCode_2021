#-------------
#   Day 1.1/50
#-------------
from pathlib import Path

p = Path(__file__).with_name("Day1Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()

#print(lines)

depths = []
for line in lines:
    depths.append(int(line.strip()))

firstDepth = True
lastDepth = 0
depthCounter = 0

for depth in depths:
    if firstDepth:
        lastDepth = depth
        firstDepth = False
    
    depthDiff = depth - lastDepth
    lastDepth = depth

    if depthDiff > 0:
        depthCounter+=1

print(depthCounter)