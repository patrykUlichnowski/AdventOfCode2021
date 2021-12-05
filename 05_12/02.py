dataFile = open("data.txt", "r")
dataFromFile = []
for i in range(0, 500):
    y = dataFile.readline().strip().split(" -> ")
    for i in y:
        dataFromFile.append(list(map(int, i.split(","))))
dataFile.close()

hydrotermalMap = []
for i in range(0, 1000):
    x = []
    for j in range(0, 1000):
        x.append(0)
    hydrotermalMap.append(x)

for i in range(0, len(dataFromFile), 2):
    x1 = dataFromFile[i][0]
    y1 = dataFromFile[i][1]
    x2 = dataFromFile[i+1][0]
    y2 = dataFromFile[i+1][1]
    # horizontal
    if y1 == y2:
        if x2 > x1:
            for j in range(x1, x2+1):
                hydrotermalMap[y1][j] += 1
        else:
            for j in range(x2, x1+1):
                hydrotermalMap[y1][j] += 1
    # vertical
    elif x1 == x2:
        if y2 > y1:
            for j in range(y1, y2+1):
                hydrotermalMap[j][x1] += 1
        else:
            for j in range(y2, y1+1):
                hydrotermalMap[j][x1] += 1
    # diagonal
    diagX = 0
    diagY = 0
    if x2 > x1:
        diagX = x2-x1
    elif x1 > x2:
        diagX = x1-x2
    if y2 > y1:
        diagY = y2-y1
    elif y1 > y2:
        diagY = y1-y2
    if diagY == diagX and diagY != 0 and diagX != 0:
        print("x1", x1, "y1", y1, "x2", x2, "y2", y2)
        if y1 < y2:  # y is higher
            if x1 < x2:  # x is more to the left so it need to go right
                dW = 0
                while dW < y2-y1+1:
                    hydrotermalMap[y1+dW][x1+dW] += 1
                    dW += 1
            else:  # x is more to the right so it need to go left
                dW = 0
                while dW < y2-y1+1:
                    hydrotermalMap[y1+dW][x1-dW] += 1
                    dW += 1
        elif y2 < y1:  # y is lower
            if x2 < x1:  # x is more to the left so it need to go right
                dW = 0
                while dW < y1-y2+1:
                    hydrotermalMap[y2+dW][x2+dW] += 1
                    dW += 1
            else:  # x is more to the right so it need to go left
                dW = 0
                while dW < y1-y2+1:
                    hydrotermalMap[y2+dW][x2-dW] += 1
                    dW += 1

atLeastTwo = 0
for i in range(0, len(hydrotermalMap)):
    for j in range(0, len(hydrotermalMap)):
        if hydrotermalMap[i][j] > 1:
            atLeastTwo += 1

for i in range(0, len(hydrotermalMap)):
    print(hydrotermalMap[i])

print('result', atLeastTwo)

# 17488 too low
# 17702 too low
