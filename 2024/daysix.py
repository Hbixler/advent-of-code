file = open("daysix.txt")

originalDir = ""
originalGuardPos = ()
obstacles = []

row = 0
for line in file:
    col = 0
    for item in line:
        if item == "^":
            originalGuardPos = (row, col)
            originalDir = "N"
        elif item == ">":
            originalGuardPos = (row, col)
            originalDir = "E"
        elif item == "v":
            originalGuardPos = (row, col)
            originalDir = "S"
        elif item == "<":
            originalGuardPos = (row, col)
            originalDir = "W"
        elif item == "#":
            obstacles.append((row, col))
        col += 1
    row += 1

def getCovered(newObstacles):
    covered = set()
    guardPos = (originalGuardPos[0], originalGuardPos[1])
    currentDir = originalDir
    while guardPos[0] >= 0 and guardPos[0] < row and guardPos[1] >= 0 and guardPos[1] < col:
        covered.add(guardPos)
        nextPos = ()
        guardRow = guardPos[0]
        guardCol = guardPos[1]
        if currentDir == "N":
            nextPos = (guardRow - 1, guardCol)
            if nextPos in obstacles:
                currentDir = "E"
                continue
        elif currentDir == "E":
            nextPos = (guardRow, guardCol + 1)
            if nextPos in obstacles:
                currentDir = "S"
                continue
        elif currentDir == "S":
            nextPos = (guardRow + 1, guardCol)
            if nextPos in obstacles:
                currentDir = "W"
                continue
        else:
            nextPos = (guardRow, guardCol - 1)
            if nextPos in obstacles:
                currentDir = "N"
                continue
        guardPos = nextPos
    return covered

covered = getCovered(obstacles)
print(len(covered))

def isInLoop(newObstacles):
    covered = set()
    guardPos = (originalGuardPos[0], originalGuardPos[1])
    currentDir = originalDir
    while guardPos[0] >= 0 and guardPos[0] < row and guardPos[1] >= 0 and guardPos[1] < col:
        if (guardPos, currentDir) in covered:
            # print("FOUND IN COVERED: " + str(guardPos))
            return True
        nextPos = ()
        guardRow = guardPos[0]
        guardCol = guardPos[1]
        if currentDir == "N":
            nextPos = (guardRow - 1, guardCol)
            if nextPos in newObstacles:
                # print("ADDING TO COVERED: " + str(guardPos) + ", " + currentDir)
                covered.add((guardPos, currentDir))
                currentDir = "E"
                continue
        elif currentDir == "E":
            nextPos = (guardRow, guardCol + 1)
            if nextPos in newObstacles:
                # print("ADDING TO COVERED: " + str(guardPos) + ", " + currentDir)
                covered.add((guardPos, currentDir))
                currentDir = "S"
                continue
        elif currentDir == "S":
            nextPos = (guardRow + 1, guardCol)
            if nextPos in newObstacles:
                # print("ADDING TO COVERED: " + str(guardPos) + ", " + currentDir)
                covered.add((guardPos, currentDir))
                currentDir = "W"
                continue
        else:
            nextPos = (guardRow, guardCol - 1)
            if nextPos in newObstacles:
                # print("ADDING TO COVERED: " + str(guardPos) + ", " + currentDir)
                covered.add((guardPos, currentDir))
                currentDir = "N"
                continue
        # print("ADDING TO COVERED: " + str(guardPos) + ", " + currentDir)
        covered.add((guardPos, currentDir))
        guardPos = nextPos
    return False

sum = 0
num = 0
for pos in list(covered):
    if (num % 100 == 0):
        print(num)
    if originalGuardPos == pos or pos in obstacles:
            continue
    else:
        # test out with this pos as an obstacle
        newObstacles = obstacles.copy()
        newObstacles.append(pos)
        if isInLoop(newObstacles):
            sum += 1
    num += 1

print(sum)