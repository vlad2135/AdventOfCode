import sys
import os

os.chdir(sys.path[0])
fileName = 'input_tst1'

def findContaining(patterns: list, digit: set) -> set:
    for pattern in patterns:
        if digit.issubset(pattern):
            return pattern

def findNotContaining(patterns: list, digit: set) -> set:
    for pattern in patterns:
        if not digit.issubset(pattern):
            return pattern


def findDigits(patterns: list) -> dict:
    one = set(list(filter(lambda d: len(d)==2, patterns))[0])
    four = set(list(filter(lambda d: len(d)==4, patterns))[0])
    seven = set(list(filter(lambda d: len(d)==3, patterns))[0])
    eight = set(list(filter(lambda d: len(d)==7, patterns))[0])

    allSixLenSet = list(map( lambda s: set(s), filter(lambda d: len(d) == 6, patterns)))
    six = findNotContaining(allSixLenSet, one)
    nine = findContaining(allSixLenSet, four)
    allFiveLenSet = list(map( lambda s: set(s), filter(lambda d: len(d) == 5, patterns)))
    three = findContaining(allFiveLenSet, seven)



    print('one', one)
    print('three', three)
    print('four', four)
    print('six', six)
    print('seven', seven)
    print('eight', eight)
    print('nine', nine)


uniqDigits = 0
with open(fileName, 'r') as file:
    for line in file:
        (before, after) = line.split('|')
        digits = after.split()
        uniqDigits += len(list(filter(lambda d: (len(d) > 1 and len(d) < 5) or len(d) == 7, digits)))
        patterns = before.split()
        p2dDict = findDigits(patterns)

print(uniqDigits)