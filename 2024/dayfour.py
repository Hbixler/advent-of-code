file = open("dayfour.txt")

word = "XMAS"
nextPos = 1
matches = 0

grid = []

for line in file:
    if line[-1] == "\n":
        grid.append(line[:-1])
    else:
        grid.append(line)

def isMatch(gridPos, dir, letterNum):
    # print("letterNum: " + str(letterNum))
    if letterNum == len(word):
        return True
    newPos = []
    if dir == "R":
        newPos = [gridPos[0], gridPos[1] + 1]
    if dir == "RD":
        newPos = [gridPos[0] + 1, gridPos[1] + 1]
    if dir == "D":
        newPos = [gridPos[0] + 1, gridPos[1]]
    if dir == "LD":
        newPos = [gridPos[0] + 1, gridPos[1] - 1]
    if dir == "L":
        newPos = [gridPos[0], gridPos[1] - 1]
    if dir == "LU":
        newPos = [gridPos[0] - 1, gridPos[1] - 1]
    if dir == "U":
        newPos = [gridPos[0] - 1, gridPos[1]]
    if dir == "RU":
        newPos = [gridPos[0] - 1, gridPos[1] + 1]
    return gridPos[0] >= 0 and gridPos[0] < len(grid) and gridPos[1] >= 0 and gridPos[1] < len(grid[0]) and word[letterNum] == grid[gridPos[0]][gridPos[1]] and isMatch(newPos, dir, letterNum + 1)

dirArr = ["R", "RD", "D", "LD", "L", "LU", "U", "RU"]
for x in range(len(grid)):
    for y in range(len(grid[0])):
        letter = grid[x][y]
        if letter == word[0]:
            for item in dirArr:
                # print("checking pos " + str([x,y]) + " with dir " + item)
                if isMatch([x,y], item, 0):
                    matches += 1

print(matches)