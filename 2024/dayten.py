file = open("daytensample.txt")

map = []
starts = {}

row = 0
for line in file:
    rep = ""
    col = 0
    for char in line:
        if char != "\n":
            if char == "0":
                starts[str(row) + "-" + str(col)] = set()
            if char == ".":
                char = "0"
            rep += char
            col += 1
    row += 1
    map.append(rep)

def isHiking(pos, grid, org, trail):
    # print(pos)
    # print(grid[pos[0]])
    # print(grid[pos[0]][pos[1]])
    trail.append(pos)
    num = int(grid[pos[0]][pos[1]])
    if num == 9:
        starts[str(org[0]) + "-" + str(org[1])].add(str(trail))
        return True
    
    up = pos[0] - 1 >= 0 and int(grid[pos[0]-1][pos[1]]) == num + 1 and isHiking([pos[0]-1, pos[1]], grid, org, trail)
    right = pos[1] + 1 < col and int(grid[pos[0]][pos[1]+1]) == num + 1 and isHiking([pos[0], pos[1]+1], grid, org, trail)
    down = pos[0] + 1 < row and int(grid[pos[0]+1][pos[1]]) == num + 1 and isHiking([pos[0]+1, pos[1]], grid, org, trail)
    left = pos[1] - 1 >= 0 and int(grid[pos[0]][pos[1]-1]) == num + 1 and isHiking([pos[0], pos[1]-1], grid, org, trail)

sum = 0
for start in starts.keys():
    # print(start)
    startPos = [int(x) for x in start.split("-")]
    isHiking(startPos, map, startPos, startPos)
    sum += len(starts[start])

print(sum)
