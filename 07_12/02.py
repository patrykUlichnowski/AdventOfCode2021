dataFile = open("data.txt", "r")
data = list(map(int, dataFile.readline().split(",")))
dataFile.close()
data.sort()
maxDataNumber = data[-1]
minDataNumber = data[0]
bestOption = 0
howMuchFuel = 0
for i in range(minDataNumber, maxDataNumber):
    sum = 0
    for j in range(0, len(data)):
        byStep = 0
        if i > data[j]:
            for step in range(0, i - data[j]):
                byStep += step
            result = i + byStep - data[j]
        else:
            for step in range(0, data[j]-i):
                byStep += step
            result = data[j] + byStep - i
        sum += result
    if howMuchFuel == 0:
        bestOption = i
        howMuchFuel = sum
    else:
        if sum < howMuchFuel:
            bestOption = i
            howMuchFuel = sum
print("best number is", bestOption)
print("amount of fuel is", howMuchFuel)
