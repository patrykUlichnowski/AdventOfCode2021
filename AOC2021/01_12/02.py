f = open("data.txt", "r")
increase = 0
B = []
memorized = 0
for i in range(0, 2000):
    A = []
    result = 0
    if i == 0:
        A.append(int(f.readline().strip()))
        A.append(int(f.readline().strip()))
        A.append(int(f.readline().strip()))
        mem1 = A[1]
        mem2 = A[2]
    else:
        A = []
        A.append(mem1)
        A.append(mem2)
        A.append(int(f.readline().strip()))
        mem1 = A[1]
        mem2 = A[2]
    print("A:", A)
    for h in range(0, len(A)):
        result += A[h]
    if result > memorized and memorized != 0:
        increase += 1
    memorized = result
    print(increase)
f.close()
