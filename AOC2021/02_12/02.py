f = open("data.txt", "r")
depth = 0
horizontal = 0
aim = 0
for i in range(0, 1000):
    x = f.readline().split(" ")
    x[1] = int(x[1].strip())
    print(x)
    if x[0] == "down":
        # depth += x[1]
        aim += x[1]
    elif x[0] == "up":
        # depth -= x[1]
        aim -= x[1]
    elif x[0] == "forward":
        horizontal += x[1]
        if aim != 0:
            depth += x[1]*aim
print("depth:", depth)
print("aim:", aim)
print("horizontal:", horizontal)
print(depth*horizontal)
f.close()
