#-------------
#   Day 3.1/50
#-------------
from pathlib import Path
from typing import Match

strippedLines = []
p = Path(__file__).with_name("Day3Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for i in lines: strippedLines.append(i.strip())


gamma = '' # most common bit
epsi = ''  # reverse (least common)

for i in range(0,12):
    checkValue = 0
    for line in strippedLines:
        if line[i] == '1': checkValue +=1
        else: checkValue -= 1
    if checkValue > 0:
        gamma += '1'
        epsi += '0'
    else: 
        gamma += '0'
        epsi += '1'

print(int(gamma, 2) * int(epsi, 2))

# # Debug zone    
# print(len("master")) # 6
# w = "master"
# for i in range(len("master")): print(w[i]) # master
