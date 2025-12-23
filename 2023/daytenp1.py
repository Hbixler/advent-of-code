from enum import Enum

file = open("day_ten_input.txt")

map = []
startPos = []
distances = []
visited = set()
openLoop = set()

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

for line in file:
    if "S" in line:
        startPos = [len(map), line.index("S")]
        print(startPos)
    if "\n" in line:
        map.append(line[:-1])
        distances.append([-1 for _ in range(len(line) - 1)])
    else:
        map.append(line)
        distances.append([-1 for _ in range(len(line))])

currentPos = []
maxDistance = 0
visited.add(str(startPos))
# print(map[0])
# print(map[startPos[0]][startPos[1]])

# Check if connects up
if startPos[0] > 0:
    upPos = [startPos[0] - 1, startPos[1]]
    upIcon = map[upPos[0]][upPos[1]]
    if upIcon == "|" or upIcon == "7" or upIcon == "F":
        currentPos.append([upPos, Direction.UP])

# Check if connects right
if startPos[1] < len(map[0]) - 1:
    rightPos = [startPos[0], startPos[1] + 1]
    rightIcon = map[rightPos[0]][rightPos[1]]
    if rightIcon == "-" or rightIcon == "J" or rightIcon == "7":
        currentPos.append([rightPos, Direction.RIGHT])

# Check if connects down
if startPos[0] < len(map) - 1:
    downPos = [startPos[0] + 1, startPos[1]]
    downIcon = map[downPos[0]][downPos[1]]
    if downIcon == "|" or downIcon == "L" or downIcon == "J":
        currentPos.append([downPos, Direction.DOWN])

# Check if connects left
if startPos[1] > 0:
    leftPos = [startPos[0], startPos[1] - 1]
    leftIcon = map[leftPos[0]][leftPos[1]]
    if leftIcon == "-" or leftIcon == "F" or leftIcon == "L":
        currentPos.append([leftPos, Direction.LEFT])

while str(currentPos[0][0]) not in visited and str(currentPos[1][0]) not in visited:
    newPos = []
    maxDistance += 1
    for posPair in currentPos:
        pos = posPair[0]
        # print(pos)
        direction = posPair[1]
        distances[pos[0]][pos[1]] = maxDistance
        # print(maxDistance)
        mapIcon = map[pos[0]][pos[1]]
        nextDirection = Direction.UP
        visited.add(str(pos))

        # Determine next direction
        if mapIcon == "|" or mapIcon == "-":
            nextDirection = direction
        elif mapIcon == "L":
            if direction == Direction.DOWN:
                nextDirection = Direction.RIGHT
            elif direction == Direction.LEFT:
                nextDirection = Direction.UP
        elif mapIcon == "J":
            if direction == Direction.DOWN:
                nextDirection = Direction.LEFT
            elif direction == Direction.RIGHT:
                nextDirection = Direction.UP
        elif mapIcon == "7":
            if direction == Direction.RIGHT:
                nextDirection = Direction.DOWN
            elif direction == Direction.UP:
                nextDirection = Direction.LEFT
        elif mapIcon == "F":
            if direction == Direction.UP:
                nextDirection = Direction.RIGHT
            elif direction == Direction.LEFT:
                nextDirection = Direction.DOWN

        # Adjust next position accordingly
        if nextDirection == Direction.UP:
            newPos.append([[pos[0] - 1, pos[1]], Direction.UP])
        elif nextDirection == Direction.RIGHT:
            newPos.append([[pos[0], pos[1] + 1], Direction.RIGHT])
        elif nextDirection == Direction.DOWN:
            newPos.append([[pos[0] + 1, pos[1]], Direction.DOWN])
        elif nextDirection == Direction.LEFT:
            newPos.append([[pos[0], pos[1] - 1], Direction.LEFT])
        
    currentPos = newPos[:]

# print(maxDistance)

squares = 0
visitedArr = []
for pair in list(visited):
    rowNum = int(pair.split(",")[0][1:])
    colNum = int(pair.split(" ")[1][:-1])
    visitedArr.append([rowNum, colNum])
visitedArr.sort()

for row in range(len(map)):
    visitedInRow = []
    lastPair = []
    # print("ROW: " + str(row))
    for pair in visitedArr:
        rowNum = pair[0]
        if rowNum == row:
            # print(map[rowNum])
            colNum = pair[1]
            # print([rowNum, colNum])
            currentIcon = map[rowNum][colNum]
            if currentIcon != "-":
                if len(lastPair) > 0:
                    lastIcon = map[lastPair[0]][lastPair[1]]
                    # print("Last icon is " + lastIcon)
                    # print("Current icon is " + currentIcon)
                    if (lastIcon == "L" and currentIcon == "7") or (lastIcon == "F" and currentIcon == "J"):
                        visitedInRow.append([rowNum, colNum])
                    else:
                        visitedInRow.append(lastPair)
                        visitedInRow.append([rowNum, colNum])
                    lastPair = []
                else:
                    if currentIcon == "L" or currentIcon == "F":
                        lastPair = [rowNum, colNum]
                    else:
                        visitedInRow.append([rowNum, colNum])
    if len(lastPair) > 0:
        visitedInRow.append(lastPair)
    # print("ROW " + str(row))
    visitedInRow.sort()
    # print(visitedInRow)
    if len(visitedInRow) > 0:
        pairOne = visitedInRow[0]
        for x in range(1, len(visitedInRow)):
            if map[row][visitedInRow[x][1]] != "-":
                if len(pairOne) == 0:
                    pairOne = visitedInRow[x]
                else:
                    for col in range(pairOne[1] + 1, visitedInRow[x][1]):
                        if str([row, col]) not in visited:
                            print("Adding " + str([row, col]))
                            squares += 1
                    pairOne = []

print(squares)

        