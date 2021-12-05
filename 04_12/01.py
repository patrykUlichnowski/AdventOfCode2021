def checkForNumber(board, number):
    # this function will check if number exist in the board and if it does it will mark it as "w"
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == number:
                board[i][j] = "w"
            else:
                continue
    checkForWin(board)


def checkForWin(board):
    global boardThatWon, endOfTheGame
    # horizontal win
    for i in range(0, len(board)):
        counter = 0
        for j in range(0, len(board)):
            if board[i][j] == "w":
                counter += 1
        if counter == 5:
            boardThatWon = board
            endOfTheGame = True
    # vertical win
    for i in range(0, len(board)):
        counter = 0
        for j in range(0, len(board)):
            if board[j][i] == "w":
                counter += 1
        if counter == 5:
            boardThatWon = board
            endOfTheGame = True


allNumbers = [
    84, 28, 29, 75, 58, 71, 26, 6, 73, 74, 41, 39, 87, 37, 16, 79, 55, 60, 62, 80, 64, 95, 46, 15, 5, 47, 2, 35, 32, 78, 89, 90, 96, 33, 4, 69, 42, 30, 54, 85, 65, 83, 44, 63, 20, 17, 66, 81, 67,
    77, 36, 68, 82, 93, 10, 25, 9, 34, 24, 72, 91, 88, 11, 38, 3, 45, 14, 56, 22, 61, 97, 27, 12, 48, 18, 1, 31, 98, 86, 19, 99, 92, 8, 43, 52, 23, 21, 0, 7, 50, 57, 70, 49, 13, 51, 40, 76, 94, 53, 59
]
# setting up bingo boards to play
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

# main loop
lastNumber = 0
endOfTheGame = False
boardThatWon = []
for i in allNumbers:
    if endOfTheGame == False:
        lastNumber = i
        for j in range(0, len(bingoBoards)):
            checkForNumber(bingoBoards[j], lastNumber)

# total value of unchecked numbers on board
sum = 0
for i in range(0, len(boardThatWon)):
    for j in range(0, len(boardThatWon)):
        if boardThatWon[i][j] != "w":
            sum += boardThatWon[i][j]


print("result:", sum*lastNumber)
