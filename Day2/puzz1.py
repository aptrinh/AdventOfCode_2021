#-------------
#   Day 2.1/50
#-------------
from pathlib import Path
from typing import Match

p = Path(__file__).with_name("Day2Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()

horizontalSum = 0
depthSum = 0

for line in lines:
    if line.strip().lower().startswith('d'):
        dist = line.split("down")
        depthSum += int(dist[1])
    if line.strip().lower().startswith('u'):
        dist = line.split("up")
        depthSum -= int(dist[1])
    if line.strip().lower().startswith('f'):
        dist = line.split("forward")
        horizontalSum += int(dist[1])

print(horizontalSum * depthSum)

