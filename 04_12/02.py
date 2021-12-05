def checkForNumber(board, number, indexInBingoBoards):
    # this function will check if number exist in the board and if it does it will mark it as "w"
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == number:
                board[i][j] = "w"
            else:
                continue
    # also it checks if that board have already won and if so it wont pass it to next function
    checkForWin(board, indexInBingoBoards)


def checkForWin(board, index):
    global winningBoard
    # horizontal win
    for i in range(0, len(board)):
        counter = 0
        for j in range(0, len(board)):
            if board[i][j] == "w":
                counter += 1
        if counter == 5:
            if len(indexesOfBoardsThatWon) != 0:
                alreadyChecked = False
                for k in range(0, len(indexesOfBoardsThatWon)):
                    if index == indexesOfBoardsThatWon[k]:
                        alreadyChecked = True
                if alreadyChecked == False:
                    indexesOfBoardsThatWon.append(index)
            else:
                indexesOfBoardsThatWon.append(index)
    # vertical win
    for i in range(0, len(board)):
        counter = 0
        for j in range(0, len(board)):
            if board[j][i] == "w":
                counter += 1
        if counter == 5:
            if len(indexesOfBoardsThatWon) != 0:
                alreadyChecked = False
                for k in range(0, len(indexesOfBoardsThatWon)):
                    if index == indexesOfBoardsThatWon[k]:
                        alreadyChecked = True
                if alreadyChecked == False:
                    indexesOfBoardsThatWon.append(index)
            else:
                indexesOfBoardsThatWon.append(index)


# setting up bingo boards to play
allNumbers = [
    84, 28, 29, 75, 58, 71, 26, 6, 73, 74, 41, 39, 87, 37, 16, 79, 55, 60, 62, 80, 64, 95, 46, 15, 5, 47, 2, 35, 32, 78, 89, 90, 96, 33, 4, 69, 42, 30, 54, 85, 65, 83, 44, 63, 20, 17, 66, 81, 67,
    77, 36, 68, 82, 93, 10, 25, 9, 34, 24, 72, 91, 88, 11, 38, 3, 45, 14, 56, 22, 61, 97, 27, 12, 48, 18, 1, 31, 98, 86, 19, 99, 92, 8, 43, 52, 23, 21, 0, 7, 50, 57, 70, 49, 13, 51, 40, 76, 94, 53, 59
]
bingoBoards = []
dataFile = open("data.txt", "r")
for i in range(0, 100):
    x = []
    for i in range(0, 5):
        y = list(map(int, dataFile.readline().strip().split()))
        x.append(y)
    dataFile.readline()
    bingoBoards.append(x)
dataFile.close()

# main loop that will look for 99 boards that have won
lastNumber = 0
indexesOfBoardsThatWon = []
for i in allNumbers:
    if len(indexesOfBoardsThatWon) != 99:
        lastNumber = i
        for j in range(0, len(bingoBoards)):
            if len(indexesOfBoardsThatWon) != 0:
                alreadyChecked = False
                for k in range(0, len(indexesOfBoardsThatWon)):
                    if j == indexesOfBoardsThatWon[k]:
                        alreadyChecked = True
                if alreadyChecked == False:
                    checkForNumber(bingoBoards[j], lastNumber, j)
            else:
                checkForNumber(bingoBoards[j], lastNumber, j)

# now we gonna search for the last board
winningBoard = []
indexesOfBoardsThatWon.sort()
for j in range(0, len(bingoBoards)):
    if j != indexesOfBoardsThatWon[j]:
        winningBoard = bingoBoards[j]
        break


# total value of unchecked numbers on board
sum = 0
for i in range(0, len(winningBoard)):
    for j in range(0, len(winningBoard)):
        if winningBoard[i][j] != "w":
            sum += winningBoard[i][j]

print("how many won", len(indexesOfBoardsThatWon))
print("board that lost", winningBoard)
print("result:", sum*lastNumber)
