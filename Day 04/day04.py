import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

winNums = list()
boards = list()
with open(fileName, 'r') as file:
    winNums = [ int(s) for s in file.readline().split(',')]

    while True:
        space = file.readline()
        board = list()

        for i in range(0, 5):
            line = file.readline()
            if line == '':
                break
            board.append([(int(s), False) for s in line.split()])

        if len(board) < 1:
            break

        boards.append((board, False))


def markNumber(board: list, num: int):
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column][0] == num:
                board[row][column] = (num, True)


def isWinnerBoard(board: list) -> bool:
    for row in range(0, len(board)):
        isWinner = True
        for column in range(0, len(board[row])):
            if board[row][column][1] == False:
                isWinner = False
        if isWinner:
            return isWinner

    for column in range(0, len(board[0])):
        isWinner = True
        for row in range(0, len(board)):
            if board[row][column][1] == False:
                isWinner = False
        if isWinner:
            return isWinner

    return False


def calcWinScore(board: list, winNumber: int) -> int:
    sum = 0
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column][1] == False:
                sum += board[row][column][0]

    return sum * winNumber


for i in range(0, 4):
    retrievedNumber = winNums[i]
    for b in boards:
        markNumber(b[0], retrievedNumber)

winFlag = False
lastToWin = None

for i in range(4, len(winNums)):
    retrievedNumber = winNums[i]
    for b in boards:
        markNumber(b[0], retrievedNumber)

    winningBoard = list(filter(lambda b: isWinnerBoard(b[0]), boards))
    if len(winningBoard) > 0 and not winFlag:
        print(calcWinScore(winningBoard[0][0], retrievedNumber))
        winFlag = True

    boards = list(filter(lambda b: not isWinnerBoard(b[0]), boards))
    if len(boards) == 1:
        lastToWin = boards[0][0]

    if len(boards) == 0:
        print(calcWinScore(lastToWin, retrievedNumber))
        sys.exit()
