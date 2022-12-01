import sys
import os
from collections import defaultdict

os.chdir(sys.path[0])
fileName = 'input'

dots = set()
instructions = []
with open(fileName, 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue

        if ',' in line:
            (x,y) = [int(c) for c in line.split(',')]
            dots.add((x,y))
        else:
            (f,a,data) = line.split()
            (coord, val) = data.split('=')
            instructions.append([coord, int(val)])

for instr in instructions:#[0:1]:
    newDots = set()
    for dot in dots:
        if instr[0] == 'y':
            newDots.add((dot[0],instr[1] - abs(instr[1] - dot[1])))
        else:
            newDots.add((instr[1] - abs(instr[1] - dot[0]), dot[1]))
    dots = newDots

print(len(dots))

matrix = [[' '] * 41 for yy in range(0, 8)]

for dot in dots:
    matrix[dot[1]][dot[0]] = 'x'

for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y])):
        print(matrix[y][x],end='')
    print()



