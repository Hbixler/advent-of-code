file = open("day_thirteen_input.txt")

grids = []
currentGrid = []

for line in file:
    if "#" in line or "." in line:
        if "\n" in line:
            currentGrid.append(line[:-1])
        else:
            currentGrid.append(line)
    else:
        grids.append(currentGrid)
        currentGrid = []

grids.append(currentGrid)
sum = 0

for grid in grids:
    # Check for row reflections
    for row in range(len(grid) - 1):

        smudgeUsed = False
        rowAbove = row
        rowBelow = row + 1

        while grid[rowAbove] == grid[rowBelow] or not smudgeUsed:
            if grid[rowAbove] != grid[rowBelow]:
                for x in range(len(grid[rowAbove])):
                    if grid[rowAbove][x] != grid[rowBelow][x]:
                        if not smudgeUsed:
                            smudgeUsed = True
                        else:
                            rowAbove += 1
                            rowBelow -= 1
                            break

            rowAbove -= 1
            rowBelow += 1

            if (rowAbove < 0 or rowBelow > len(grid) - 1):
                if smudgeUsed:
                    print('found reflection in row ' + str(row))
                    sum += 100 * (row + 1)
                break
    
    # Check for col reflections
    for col in range(len(grid[0]) - 1):

        smudgeUsed = False
        leftCol = col
        rightCol = col + 1

        while [x[leftCol] for x in grid] == [x[rightCol] for x in grid] or not smudgeUsed:
            leftColArr = [x[leftCol] for x in grid]
            rightColArr = [x[rightCol] for x in grid]
            if leftColArr != rightColArr:
                for x in range(len(leftColArr)):
                    if leftColArr[x] != rightColArr[x]:
                        if not smudgeUsed:
                            smudgeUsed = True
                        else:
                            leftCol += 1
                            rightCol -= 1
                            break

            leftCol -= 1
            rightCol += 1

            if leftCol < 0 or rightCol > len(grid[0]) - 1:
                if smudgeUsed:
                    sum += col + 1
                break
    
print(sum)