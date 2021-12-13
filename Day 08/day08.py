import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

uniqDigits = 0
with open(fileName, 'r') as file:
    for line in file:
        (before, after) = line.split('|')
        digits = after.split()
        uniqDigits += len(list(filter(lambda d: (len(d) > 1 and len(d) < 5) or len(d) == 7, digits)))

print(uniqDigits)