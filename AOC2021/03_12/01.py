f = open("data.txt", "r")
values = []
gamma = ""
epsilon = ""
for i in range(0, 1000):
    values.append(f.readline().strip())
for i in range(0, 12):
    counterOf0 = 0
    counterOf1 = 0
    for j in range(0, len(values)):
        linia = values[j]
        if int(linia[i]) == 1:
            counterOf1 += 1
        else:
            counterOf0 += 1
    if counterOf1 > counterOf0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
decimal1 = int(gamma, 2)
decimal2 = int(epsilon, 2)
print("result:", decimal1*decimal2)
f.close()
