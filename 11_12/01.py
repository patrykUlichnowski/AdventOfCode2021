def split(word):
    return [char for char in word]


dataFile = open("data.txt", "r")
octopuses = []
for i in range(0, 10):
    octopuses.append(list(map(int, split(dataFile.readline().strip()))))
dataFile.close()

flashes = 0
for step in range(0, 100):
    # step 1; increase every octopus by 1
    for row in range(0, len(octopuses)):
        for octopus in range(0, len(octopuses[row])):
            octopuses[row][octopus] = octopuses[row][octopus] + 1
    # step 2; checking if octopus flashes(9)
    noMoreNines = False
    while noMoreNines != True:
        check = False
        for row in range(0, len(octopuses)):
            for octopus in range(0, len(octopuses[row])):
                if octopuses[row][octopus] > 9:
                    flashes += 1
                    check = True
                    # creating a map around the octopus and increasing them
                    octopuses[row][octopus] = 0
                    # left
                    if octopus != 0:
                        if octopuses[row][octopus - 1] != 0:
                            octopuses[row][octopus - 1] += 1
                    # right
                    if octopus != len(octopuses[row]) - 1:
                        if octopuses[row][octopus + 1] != 0:
                            octopuses[row][octopus + 1] += 1
                    # bottom
                    if row != len(octopuses) - 1:
                        if octopuses[row + 1][octopus] != 0:
                            octopuses[row + 1][octopus] += 1
                    # top
                    if row != 0:
                        if octopuses[row-1][octopus] != 0:
                            octopuses[row-1][octopus] += 1
                    # bottom left
                    if octopus != 0 and row != len(octopuses) - 1:
                        if octopuses[row+1][octopus - 1] != 0:
                            octopuses[row+1][octopus - 1] += 1
                    # top left
                    if octopus != 0 and row != 0:
                        if octopuses[row-1][octopus - 1] != 0:
                            octopuses[row-1][octopus - 1] += 1
                    # bottom right
                    if octopus != len(octopuses[row])-1 and row != len(octopuses) - 1:
                        if octopuses[row+1][octopus+1] != 0:
                            octopuses[row+1][octopus+1] += 1
                    # top right
                    if octopus != len(octopuses[row])-1 and row != 0:
                        if octopuses[row-1][octopus + 1] != 0:
                            octopuses[row-1][octopus + 1] += 1
        if check == False:
            noMoreNines = True
print("result", flashes)
