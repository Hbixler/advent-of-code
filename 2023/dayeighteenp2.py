from collections import defaultdict

file = open("day_eighteen_input.txt")

mapPoints = defaultdict(lambda: {})
mapPoints[0] = {0: "D"}
minMaxX = [0, 0]
minMaxY = [0, 0]
currentPos = [0, 0]
currentDir = "D"


for line in file:
    if "\n" in line:
        line = line[:-1]

    code = line.split(" ")[2]
    num = int(code[2:-2], 16)
    dir = ""

    if code[-2] == "0":
        dir = "R"
    elif code[-2] == "1":
        dir = "D"
    elif code[-2] == "2":
        dir = "L"
    elif code[-2] == "3":
        dir = "U"
    else:
        print("Something is wrong")
    
    # print(code)
    # print(dir + " " + str(num))
    if len(mapPoints) == 1:
        print(dir)

    if dir == "U":
        currentDir = "U"
        mapPoints[currentPos[0]][currentPos[1]] = "U"
        if currentPos[0] - num < minMaxY[0]:
            minMaxY[0] = currentPos[0] - num
        for y in range(currentPos[0] - num, currentPos[0]):
            mapPoints[y][currentPos[1]] = currentDir
        currentPos = [currentPos[0] - num, currentPos[1]]
    elif dir == "R":
        if currentPos[1] + num > minMaxX[1]:
            minMaxX[1] = currentPos[1] + num
        for x in range(currentPos[1] + 1, currentPos[1] + num + 1):
            mapPoints[currentPos[0]][x] = currentDir
        currentPos = [currentPos[0], currentPos[1] + num]
    elif dir == "D":
        currentDir = "D"
        mapPoints[currentPos[0]][currentPos[1]] = "D"
        if currentPos[0] + num > minMaxY[1]:
            minMaxY[1] = currentPos[0] + num
        for y in range(currentPos[0] + 1, currentPos[0] + num + 1):
            mapPoints[y][currentPos[1]] = currentDir
        currentPos = [currentPos[0] + num, currentPos[1]]
    elif dir == "L":
        if currentPos[1] - num < minMaxX[0]:
            minMaxX[0] = currentPos[1] - num
        for x in range(currentPos[1] - num, currentPos[1]):
            mapPoints[currentPos[0]][x] = currentDir
        currentPos = [currentPos[0], currentPos[1] - num]

print(minMaxX)
print(minMaxY)
print(len(mapPoints))
# print(mapPoints)
sum = 0

for row in range(minMaxX[0], minMaxY[1] + 1):
    rowSum = 0
    lastPos = []
    rowDigs = list(mapPoints[row].keys())
    rowDigs.sort()
    # print(rowDigs)
    for dig in rowDigs:
        if len(lastPos) == 0:
            lastPos = [row, dig]
        else:
            if mapPoints[row][dig] != mapPoints[row][lastPos[1]]:
                if dig + 1 not in mapPoints[row]:
                    sum += dig - lastPos[1] + 1
                    rowSum += dig - lastPos[1] + 1
                    lastPos = []
    # print(rowSum)
        

print(sum)


