file = open("day_fourteen_input.txt")

grid = []

for line in file:
    if "\n" in line:
        grid.append(list(line[:-1]))
    else:
        grid.append(list(line))
    
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

sum = 0
for row in range(len(grid)):
    mul = len(grid) - row
    sum += grid[row].count("O") * mul

print(sum)

