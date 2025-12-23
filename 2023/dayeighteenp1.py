file = open("day_eighteen_input.txt")

mapPoints = {str([0, 0]): "D"}
minMaxX = [0, 0]
minMaxY = [0, 0]
currentPos = [0, 0]
currentDir = "D"


for line in file:
    splitLine = line.split(" ")
    dir = splitLine[0]
    num = int(splitLine[1])

    if dir == "U":
        currentDir = "U"
        mapPoints[str(currentPos)] = "U"
        if currentPos[0] - num < minMaxY[0]:
            minMaxY[0] = currentPos[0] - num
        for y in range(currentPos[0] - num, currentPos[0]):
            mapPoints[str([y, currentPos[1]])] = currentDir
        currentPos = [currentPos[0] - num, currentPos[1]]
    elif dir == "R":
        if currentPos[1] + num > minMaxX[1]:
            minMaxX[1] = currentPos[1] + num
        for x in range(currentPos[1] + 1, currentPos[1] + num + 1):
            mapPoints[str([currentPos[0], x])] = currentDir
        currentPos = [currentPos[0], currentPos[1] + num]
    elif dir == "D":
        currentDir = "D"
        mapPoints[str(currentPos)] = "D"
        if currentPos[0] + num > minMaxY[1]:
            minMaxY[1] = currentPos[0] + num
        for y in range(currentPos[0] + 1, currentPos[0] + num + 1):
            mapPoints[str([y, currentPos[1]])] = currentDir
        currentPos = [currentPos[0] + num, currentPos[1]]
    elif dir == "L":
        if currentPos[1] - num < minMaxX[0]:
            minMaxX[0] = currentPos[1] - num
        for x in range(currentPos[1] - num, currentPos[1]):
            mapPoints[str([currentPos[0], x])] = currentDir
        currentPos = [currentPos[0], currentPos[1] - num]

# print(minMaxX)
# print(minMaxY)
        
sum = 0

for row in range(minMaxX[0], minMaxY[1] + 1):
    rowSum = 0
    lastPos = []
    rowDigs = [eval(x) for x in mapPoints.keys() if eval(x)[0] == row]
    rowDigs.sort()
    # print(rowDigs)
    for dig in rowDigs:
        if len(lastPos) == 0:
            lastPos = dig[:]
        else:
            if mapPoints[str(dig)] != mapPoints[str(lastPos)]:
                if str([dig[0], dig[1] + 1]) not in mapPoints:
                    sum += dig[1] - lastPos[1] + 1
                    rowSum += dig[1] - lastPos[1] + 1
                    lastPos = []
    # print(rowSum)
        

print(sum)


