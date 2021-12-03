def getData():
    for i in range(0, 1000):
        line = f.readline().strip()
        values.append(line)
        valuesCopy.append(line)


f = open("data.txt", "r")
values = []
valuesCopy = []
getData()
oxygen_generator_rating = 0
CO2_scrubber_rating = 0
i = 0

while len(values) != 1:
    counterOf0 = 0
    counterOf1 = 0
    filteredArrayMostCommon = []
    for j in range(0, len(values)):
        line = values[j]
        if int(line[i]) == 0:
            counterOf0 += 1
        else:
            counterOf1 += 1
    if counterOf0 > counterOf1:
        for k in range(0, len(values)):
            line = values[k]
            if int(line[i]) == 0:
                filteredArrayMostCommon.append(values[k])
    else:
        for k in range(0, len(values)):
            line = values[k]
            if int(line[i]) == 1:
                filteredArrayMostCommon.append(values[k])
    values = filteredArrayMostCommon
    i += 1
oxygen_generator_rating = values[0]
print("oxygen", oxygen_generator_rating)


i = 0
while len(valuesCopy) != 1:
    counterOf0 = 0
    counterOf1 = 0
    filteredArrayLeastCommon = []
    for j in range(0, len(valuesCopy)):
        line = valuesCopy[j]
        if int(line[i]) == 0:
            counterOf0 += 1
        else:
            counterOf1 += 1
    if counterOf0 <= counterOf1:
        for k in range(0, len(valuesCopy)):
            line = valuesCopy[k]
            if int(line[i]) == 0:
                filteredArrayLeastCommon.append(valuesCopy[k])
    else:
        for k in range(0, len(valuesCopy)):
            line = valuesCopy[k]
            if int(line[i]) == 1:
                filteredArrayLeastCommon.append(valuesCopy[k])
    valuesCopy = filteredArrayLeastCommon
    i += 1
CO2_scrubber_rating = valuesCopy[0]
print("co2", CO2_scrubber_rating)
print("result:", int(oxygen_generator_rating, 2)*int(CO2_scrubber_rating, 2))
f.close()
