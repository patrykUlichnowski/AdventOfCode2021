data = []
dataFile = open("input.txt", "r")
for i in range(0, 100):
    data.append(dataFile.readline().strip())
dataFile.close()
lowPoints = 0
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
print("result", lowPoints)
print(data)
