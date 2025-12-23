from collections import defaultdict

file = open("day_three_input.txt")
lines = []
result = 0
map = defaultdict(lambda: [])

for line in file:
    if line[-1] == "\n":
        lines.append(line[:len(line) - 1])
    else:
        lines.append(line)

for row in range(len(lines)):
    line = lines[row]
    currentNum = ""
    currentGears = []
    for col in range(len(line)):
        char = line[col]
        # print(char)
        # print(char.isnumeric())
        if char == ".":
            if currentNum != "":
                # print("Num: " + currentNum)
                # print("Gears: " + str(currentGears))
                for gear in currentGears:
                    map[str(gear)].append(currentNum)
            currentNum = ""
            currentGears = []
        elif char.isnumeric():
            if currentNum == "" and col > 0:
                if row > 0:
                    # Back up diagonal
                    toCheck = [row-1,col-1]
                    # print("back up is " + toCheck)
                    if lines[toCheck[0]][toCheck[1]] == "*":
                        currentGears.append(toCheck)

                # Back
                toCheck = [row,col-1]
                # print("back up is " + toCheck)
                if lines[toCheck[0]][toCheck[1]] == "*":
                    currentGears.append(toCheck)

                if row < len(lines) - 1:
                    # Back down diagonal
                    toCheck = [row+1,col-1]
                    if lines[toCheck[0]][toCheck[1]] == "*":
                        currentGears.append(toCheck)

            if row > 0:
                # Up
                toCheck = [row-1,col]
                if lines[toCheck[0]][toCheck[1]] == "*":
                    currentGears.append(toCheck)
                
            if row < len(lines) - 1:
                # Down
                toCheck = [row+1,col]
                if lines[toCheck[0]][toCheck[1]] == "*":
                    currentGears.append(toCheck)
                
            # print("Line length is " + str(len(line)))
            # print(line[-1])
            if col < len(line) - 1 and not lines[row][col+1].isnumeric():
                if row > 0:
                    # Up right diagonal
                    toCheck = [row-1,col+1]
                    if lines[toCheck[0]][toCheck[1]] == "*":
                        currentGears.append(toCheck)
                    
                # Right
                toCheck = [row,col+1]
                if lines[toCheck[0]][toCheck[1]] == "*":
                        currentGears.append(toCheck)

                if row < len(lines) - 1:
                    # Down right diagonal
                    toCheck = [row+1,col+1]
                    if lines[toCheck[0]][toCheck[1]] == "*":
                        currentGears.append(toCheck)
                
            currentNum += char
        else:
            if currentNum != "":
                for gear in currentGears:
                    map[str(gear)].append(currentNum)
            currentNum = ""
            currentGears = []

    if currentNum != "":
        for gear in currentGears:
            map[str(gear)].append(currentNum)


for gear in map.keys():
    gearList = map[gear]
    # print("Gear: " + str(gear))
    # print("List: " + str(gearList))
    if len(gearList) == 2:
        # print("Multiplying: " + str(gearList))
        result += int(gearList[0]) * int(gearList[1])

print(result)




                
                    


