file = open("day_fourteen_sample.txt")

grid = []
map = {}

for line in file:
    if "\n" in line:
        grid.append(list(line[:-1]))
    else:
        grid.append(list(line))

origGrid = str(grid)
countToOrigGrid = 0

for x in range(1000000000):
    if x % 10000 == 0:
        print(x)
    if str(grid) == origGrid and x > 0:
        print("Count to orig grid: " + str(x))
        break
    if str(grid) in map:
        grid = eval(map[str(grid)])
        # print(grid)
        continue

    prevGrid = str(grid)

    # NORTH
    for col in range(len(grid[0])):
        toFill = -1
        for row in range(len(grid)):
            if grid[row][col] == "O":
                if toFill >= 0:
                    grid[toFill][col] = "O"
                    grid[row][col] = "."
                    toFill += 1
            elif grid[row][col] == "#":
                toFill = -1
            else:
                if toFill == -1:
                    toFill = row
    # WEST
    for row in range(len(grid)):
        toFill = -1
        for col in range(len(grid[0])):
            if grid[row][col] == "O":
                if toFill >= 0:
                    grid[row][toFill] = "O"
                    grid[row][col] = "."
                    toFill += 1
            elif grid[row][col] == "#":
                toFill = -1
            else:
                if toFill == -1:
                    toFill = col
    # SOUTH
    for col in range(len(grid[0])):
        toFill = -1
        for row in range(len(grid) - 1, -1, -1):
            if grid[row][col] == "O":
                if toFill >= 0:
                    grid[toFill][col] = "O"
                    grid[row][col] = "."
                    toFill -= 1
            elif grid[row][col] == "#":
                toFill = -1
            else:
                if toFill == -1:
                    toFill = row

    # EAST
    for row in range(len(grid)):
        toFill = -1
        for col in range(len(grid[0]) - 1, -1, -1):
            if grid[row][col] == "O":
                if toFill >= 0:
                    grid[row][toFill] = "O"
                    grid[row][col] = "."
                    toFill -= 1
            elif grid[row][col] == "#":
                toFill = -1
            else:
                if toFill == -1:
                    toFill = col
    

    map[prevGrid] = str(grid)
    
    if x % 10000 == 0:
        print(x)

sum = 0
for row in range(len(grid)):
    print(grid[row])
    mul = len(grid) - row
    sum += grid[row].count("O") * mul

print(sum)

