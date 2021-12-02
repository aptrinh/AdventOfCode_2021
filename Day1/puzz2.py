#-------------
#   Day 1.2/50
#-------------
from pathlib import Path

p = Path(__file__).with_name("Day1Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()

#print(lines)

depths = []
trioSums = []

for line in lines:
    depths.append(int(line.strip()))

for i in range(len(depths) - 2):
    trioSum = depths[i] + depths[i+1] + depths[i+2]
    trioSums.append(trioSum)

firstTrio = True
lastTrio = 0
trioCounter = 0

for trio in trioSums:
    if firstTrio:
        lastTrio = trio
        firstTrio = False

    trioDiff = trio - lastTrio
    lastTrio = trio

    if trioDiff > 0:
        trioCounter+=1

print(trioCounter)