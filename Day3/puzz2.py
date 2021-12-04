#-------------
#   Day 3.2/50
#-------------
from pathlib import Path
import collections

strippedLines = []
p = Path(__file__).with_name("Day3Input.txt")
with p.open('r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for i in lines: strippedLines.append(i.strip())

# Sadge
gamma = strippedLines[::]
for i in range(len(strippedLines[0])):
    most = collections.Counter([r[i] for r in gamma])
    # for r in gamma:
    #     most = collections.Counter(r[i])
    most = '1' if most['1'] >= most['0'] else '0'
    gamma = list(filter(lambda x: x[i] == most, gamma))
    if len(gamma) == 1:
        break

epsilon = strippedLines[::]
for i in range(len(strippedLines[0])):
    least = collections.Counter([r[i] for r in epsilon])
    least = '0' if least['1'] >= least['0'] else '1'
    epsilon = list(filter(lambda x: x[i] == least, epsilon))
    if len(epsilon) == 1:
        break

epsilon_rate = int(epsilon[0], 2)
gamma_rate = int(gamma[0], 2)
print(f'Ans: {gamma_rate * epsilon_rate}')