f = open("data.txt", "r")
mem = 0
increase = 0
for i in range(0, 2000):
    x = f.readline()
    x = int(x.strip())
    if mem != 0 and x > mem:
        increase += 1
    mem = x
print(increase)
f.close()
