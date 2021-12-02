#-------------
#   Day 2.2/50
#-------------
from pathlib import Path
from typing import Match

p = Path(__file__).with_name("Day2Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()

# "Aim" means adjusting the vector that the sub plans to go towards. Sub won't go
# until forward is called. Before that, the aim can only go up or down, so
# down 5, forward 8 from 0,0 means we're getting down to hori8, depth40

horizontalSum = 0
depth = 0
aim = 0


for line in lines:
    if line.strip().lower().startswith('d'):
        dist = line.split("down")
        aim += int(dist[1])
    if line.strip().lower().startswith('u'):
        dist = line.split("up")
        aim -= int(dist[1])
    if line.strip().lower().startswith('f'):
        dist = line.split("forward")
        horizontalSum += int(dist[1])
        depth += int(dist[1])*aim

print(horizontalSum*depth)