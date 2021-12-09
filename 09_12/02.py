def checkForBasins(row, column):
    global sizeOfBasin
    if dataInString[row][column] == "9":
        return 0
    else:
        dataInString[row][column] = "1" + dataInString[row][column]
        sizeOfBasin += 1
        # up
        if row != 0 and int(dataInString[row-1][column]) < 10:
            checkForBasins(row-1, column)
        # down
        if row != len(data)-1 and int(dataInString[row+1][column]) < 10:
            checkForBasins(row+1, column)
        # left
        if column != 0 and int(dataInString[row][column-1]) < 10:
            checkForBasins(row, column-1)
        # right
        if column != len(dataInString[row])-1 and int(dataInString[row][column+1]) < 10:
            checkForBasins(row, column+1)


def split(word):
    return [char for char in word]


data = []
lowPointsCords = []
dataFile = open("input.txt", "r")
for i in range(0, 100):
    data.append(dataFile.readline().strip())
dataFile.close()
lowPoints = 0
# searching for lowpoints
for row in range(0, len(data)):
    for column in range(0, len(data[row])):
        top = int(data[row-1][column]) if row != 0 else 10000
        bottom = int(data[row+1][column]) if row != len(data)-1 else 10000
        right = int(data[row][column+1]
                    ) if column != len(data[row])-1 else 10000
        left = int(data[row][column-1]) if column != 0 else 10000
        if (top > int(data[row][column]) and
            bottom > int(data[row][column]) and
            left > int(data[row][column]) and
                right > int(data[row][column])):
            lowPoints += int(data[row][column])+1
            cordsOfLowPoint = [row, column]
            lowPointsCords.append(cordsOfLowPoint)
# copying data into new list as strings
dataInString = []
for i in range(0, len(data)):
    string = str(data[i])
    dataInString.append(split(string))
print(dataInString)
# checking for basins
basins = []
dataInt = list(map(int, data))
sizeOfBasin = 0
for i in range(0, len(lowPointsCords)):
    row = lowPointsCords[i][0]
    column = lowPointsCords[i][1]
    checkForBasins(row, column)
    basins.append(sizeOfBasin)
    sizeOfBasin = 0
basins.sort()
print("result", basins[-1]*basins[-2]*basins[-3])
