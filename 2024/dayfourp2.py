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

for x in range(1, len(grid) - 1):
    for y in range(1, len(grid[0]) - 1):
        letter = grid[x][y]
        if letter == "A":
            upRight = grid[x-1][y+1]
            downRight = grid[x+1][y+1]
            downLeft = grid[x+1][y-1]
            upLeft = grid[x-1][y-1]

            if sorted([upRight, downLeft]) == ["M","S"] and sorted([upLeft, downRight]) == ["M","S"]:
                matches += 1

print(matches)