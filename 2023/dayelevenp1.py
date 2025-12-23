file = open("day_eleven_input.txt")

grid = []
cols = []

for line in file:
    if "\n" in line:
        line = line[:-1]
    grid.append(line)
    if len(cols) == 0:
        cols  = [False] * len(line)
    for x in range(len(line)):
        if line[x] == "#":
            cols[x] = True

for row in grid:
    print(row)

print(cols)

galaxies = []

rowOffset = 0
for row in range(len(grid)):
    if grid[row].count(".") == len(grid[row]):
        rowOffset += 999999
    colOffset = 0
    for col in range(len(grid[0])):
        if not cols[col]:
            colOffset += 999999
        if grid[row][col] == "#":
            galaxies.append([row + rowOffset, col + colOffset])

sum = 0
print(galaxies)

for x in range(len(galaxies)):
    for y in range(x + 1, len(galaxies)):
        sum += abs(galaxies[x][0] - galaxies[y][0]) + abs(galaxies[x][1] - galaxies[y][1])

print(sum)