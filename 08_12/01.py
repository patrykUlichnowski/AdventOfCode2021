# reading strings from file
dataFile = open("data.txt", "r")
data = []
for i in range(0, 200):
    base = dataFile.readline().strip().split(" | ")
    data.append(base[1].split(" "))
dataFile.close()
# counting numbers
clock1 = 0
clock4 = 0
clock7 = 0
clock8 = 0
for row in range(0, len(data)):
    for column in range(0, len(data[row])):
        if len(data[row][column]) == 2:
            clock1 += 1
        elif len(data[row][column]) == 4:
            clock4 += 1
        elif len(data[row][column]) == 3:
            clock7 += 1
        elif len(data[row][column]) == 7:
            clock8 += 1
print("result", clock1+clock4+clock7+clock8)
