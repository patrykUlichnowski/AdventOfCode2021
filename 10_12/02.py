dataFile = open("data.txt", "r")
chunks = []
while True:
    line = dataFile.readline().strip()
    if not line:
        break
    else:
        chunks.append(line)
dataFile.close()

incomplete = []
corrupted = []
# search for corrupted
for chunk in chunks:
    stack = []
    for bracket in chunk:
        if bracket == "(" or bracket == "{" or bracket == "[" or bracket == "<":
            stack.append(bracket)
        else:
            if (stack[-1] == "(" and bracket == ")" or
                stack[-1] == "{" and bracket == "}" or
                stack[-1] == "[" and bracket == "]" or
                stack[-1] == "<" and bracket == ">"
                ):
                stack.pop(-1)
            else:
                corrupted.append(chunk)
                break
# clear chunks from corrupted lines
for chunk in chunks:
    flag = True
    for c in corrupted:
        if c == chunk:
            flag = False
    if flag == True:
        incomplete.append(chunk)

scores = []
for chunk in incomplete:
    stack = []
    result = 0
    for bracket in chunk:
        if bracket == "(" or bracket == "{" or bracket == "[" or bracket == "<":
            stack.append(bracket)
        else:
            if (stack[-1] == "(" and bracket == ")" or
                    stack[-1] == "{" and bracket == "}" or
                    stack[-1] == "[" and bracket == "]" or
                    stack[-1] == "<" and bracket == ">"
                ):
                stack.pop(-1)
    for bracket in reversed(stack):
        if bracket == "(":
            result *= 5
            result += 1
        elif bracket == "[":
            result *= 5
            result += 2
        elif bracket == "{":
            result *= 5
            result += 3
        elif bracket == "<":
            result *= 5
            result += 4
    scores.append(result)
scores.sort()
print("result", scores[(len(scores)//2)])
