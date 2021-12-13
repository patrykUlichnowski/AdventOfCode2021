dataFile = open("data.txt", "r")
chunks = []
while True:
    line = dataFile.readline().strip()
    if not line:
        break
    else:
        chunks.append(line)
dataFile.close()

allResult = 0
for chunk in chunks:
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
            else:
                if bracket == ")":
                    result += 3
                elif bracket == "]":
                    result += 57
                elif bracket == "}":
                    result += 1197
                elif bracket == ">":
                    result += 25137
                break
    allResult += result
print("result", allResult)
