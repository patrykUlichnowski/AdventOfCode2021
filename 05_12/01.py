dataFile = open("data.txt", "r")
dataList = []
for i in range(0, 500):
    y = dataFile.readline().strip().split(" -> ")
    for i in y:
        dataList.append(list(map(int, i.split(","))))
dataFile.close()

valueList = []
for i in range(0, 1000):
    x = []
    for j in range(0, 1000):
        x.append(0)
    valueList.append(x)

for i in range(0, len(dataList), 2):
    x1 = dataList[i][0]
    y1 = dataList[i][1]
    x2 = dataList[i+1][0]
    y2 = dataList[i+1][1]
    # horizontal
    if y1 == y2:
        if x2 > x1:
            for j in range(x1, x2+1):
                valueList[y1][j] += 1
        else:
            for j in range(x2, x1+1):
                valueList[y1][j] += 1
    # vertical
    elif x1 == x2:
        if y2 > y1:
            for j in range(y1, y2+1):
                valueList[j][x1] += 1
        else:
            for j in range(y2, y1+1):
                valueList[j][x1] += 1

atLeastTwo = 0
for i in range(0, len(valueList)):
    for j in range(0, len(valueList)):
        if valueList[i][j] > 1:
            atLeastTwo += 1


print('result', atLeastTwo)
