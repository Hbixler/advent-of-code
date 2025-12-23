from enum import Enum

file = open("day_sixteen_input.txt")

"""
/ -> J for needs down right or F for needs up left
\ -> L for needs down left or 7 for needs up right
| -> |
- -> -
* else

"""

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

grid = []

for line in file:
    if "\n" in line:
        grid.append(list(line[:-1]))
    else:
        grid.append(list(line))

# beams = [[0, 0, Direction.DOWN]]

def getEnergy(beams, origGrid):
    visited = set()
    grid = eval(origGrid)
    while len(beams) > 0:
        newBeams = []
        for beam in beams:
            # print(beam)
            visited.add(str([beam[0], beam[1]]))
            direction = beam[2]
            nextIcon = ""
            if direction == Direction.RIGHT:
                # print("Right!")
                if beam[1] == len(grid[0]) - 1:
                    # print("over")
                    continue
                nextIcon = grid[beam[0]][beam[1] + 1]
                # print(nextIcon)
                if nextIcon == "*" or nextIcon == "F" or nextIcon == "L":
                    continue
                elif nextIcon == "-" or nextIcon == ".":
                    newBeams.append([beam[0], beam[1] + 1, Direction.RIGHT])
                elif nextIcon == "J" or nextIcon == "/":
                    if nextIcon == "J":
                        grid[beam[0]][beam[1] + 1] = "*"
                    else:
                        grid[beam[0]][beam[1] + 1] = "F"
                    newBeams.append([beam[0], beam[1] + 1, Direction.UP])
                elif nextIcon == "7" or nextIcon == "\\":
                    if nextIcon == "7":
                        grid[beam[0]][beam[1] + 1] = "*"
                    else:
                        grid[beam[0]][beam[1] + 1] = "L"
                    newBeams.append([beam[0], beam[1] + 1, Direction.DOWN])
                elif nextIcon == "|":
                    # print("Adjusting grid")
                    grid[beam[0]][beam[1] + 1] = "*"
                    newBeams.append([beam[0], beam[1] + 1, Direction.UP])
                    newBeams.append([beam[0], beam[1] + 1, Direction.DOWN])
            elif direction == Direction.DOWN:
                if beam[0] == len(grid) - 1:
                    continue
                nextIcon = grid[beam[0] + 1][beam[1]]
                if nextIcon == "*" or nextIcon == "7" or nextIcon == "F":
                    continue
                elif nextIcon == "|" or nextIcon == ".":
                    newBeams.append([beam[0] + 1, beam[1], Direction.DOWN])
                elif nextIcon == "J" or nextIcon == "/":
                    if nextIcon == "J":
                        grid[beam[0] + 1][beam[1]] = "*"
                    else:
                        grid[beam[0] + 1][beam[1]] = "F"
                    newBeams.append([beam[0] + 1, beam[1], Direction.LEFT])
                elif nextIcon == "L" or nextIcon == "\\":
                    if nextIcon == "L":
                        grid[beam[0] + 1][beam[1]] = "*"
                    else:
                        grid[beam[0] + 1][beam[1]] = "7"
                    newBeams.append([beam[0] + 1, beam[1], Direction.RIGHT])
                elif nextIcon == "-":
                    grid[beam[0] + 1][beam[1]] = "*"
                    newBeams.append([beam[0] + 1, beam[1], Direction.RIGHT])
                    newBeams.append([beam[0] + 1, beam[1], Direction.LEFT])
            elif direction == Direction.LEFT:
                if beam[1] == 0:
                    continue
                nextIcon = grid[beam[0]][beam[1] - 1]
                if nextIcon == "*" or nextIcon == "J" or nextIcon == "7":
                    continue
                elif nextIcon == "-" or nextIcon == ".":
                    newBeams.append([beam[0], beam[1] - 1, Direction.LEFT])
                elif nextIcon == "F" or nextIcon == "/":
                    if nextIcon == "F":
                        grid[beam[0]][beam[1] - 1] = "*"
                    else:
                        grid[beam[0]][beam[1] - 1] = "J"
                    newBeams.append([beam[0], beam[1] - 1, Direction.DOWN])
                elif nextIcon == "L" or nextIcon == "\\":
                    if nextIcon == "L":
                        grid[beam[0]][beam[1] - 1] = "*"
                    else:
                        grid[beam[0]][beam[1] - 1] = "7"
                    newBeams.append([beam[0], beam[1] - 1, Direction.UP])
                elif nextIcon == "|":
                    grid[beam[0]][beam[1] - 1] = "*"
                    newBeams.append([beam[0], beam[1] - 1, Direction.UP])
                    newBeams.append([beam[0], beam[1] - 1, Direction.DOWN])
            elif direction == Direction.UP:
                if beam[0] == 0:
                    continue
                nextIcon = grid[beam[0] - 1][beam[1]]
                if nextIcon == "*" or nextIcon == "L" or nextIcon == "J":
                    continue
                elif nextIcon == "|" or nextIcon == ".":
                    # print(beam)
                    # print([beam[0] - 1, beam[1], Direction.UP])
                    newBeams.append([beam[0] - 1, beam[1], Direction.UP])
                elif nextIcon == "F" or nextIcon == "/":
                    if nextIcon == "F":
                        grid[beam[0] - 1][beam[1]] = "*"
                    else:
                        grid[beam[0] - 1][beam[1]] = "J"
                    newBeams.append([beam[0] - 1, beam[1], Direction.RIGHT])
                elif nextIcon == "7" or nextIcon == "\\":
                    if nextIcon == "7":
                        grid[beam[0] - 1][beam[1]] = "*"
                    else:
                        grid[beam[0] - 1][beam[1]] = "L"
                    newBeams.append([beam[0] - 1, beam[1], Direction.LEFT])
                elif nextIcon == "-":
                    grid[beam[0] - 1][beam[1]] = "*"
                    newBeams.append([beam[0] - 1, beam[1], Direction.RIGHT])
                    newBeams.append([beam[0] - 1, beam[1], Direction.LEFT])
        beams = newBeams[:]

    # print("len is " + str(len(visited)))
    return len(visited)


maxEnergy = 0
# maxEnergy = getEnergy([[0, 3, Direction.DOWN]], grid)


# Top row
for x in range(len(grid[0])):
    # print("After looking at column : " + str(x))
    maxEnergy = max(maxEnergy, getEnergy([[0, x, Direction.DOWN]], str(grid)))
    # print(maxEnergy)

# Right column
for x in range(len(grid)):
    maxEnergy = max(maxEnergy, getEnergy([[x, len(grid[0]) - 1, Direction.LEFT]], str(grid)))

# Bottom row
for x in range(len(grid[0])):
    maxEnergy = max(maxEnergy, getEnergy([[len(grid) - 1, x, Direction.UP]], str(grid)))

# Right row
for x in range(len(grid)):
    maxEnergy = max(maxEnergy, getEnergy([[x, 0, Direction.RIGHT]], str(grid)))

          

"""
for x in range(len(grid)):
    toPrint = ""
    for y in range(len(grid[x])):
        item = grid[x][y]
        if str([x,y]) in visited:
            toPrint += "#"
        else:
            toPrint += item
    print(toPrint)
"""

        

print(maxEnergy)

