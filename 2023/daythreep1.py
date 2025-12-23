file = open("day_three_input.txt")
lines = []
sum = 0

for line in file:
    if line[-1] == "\n":
        lines.append(line[:len(line) - 1])
    else:
        lines.append(line)

for row in range(len(lines)):
    line = lines[row]
    currentNum = ""
    isPartNum = False
    for col in range(len(line)):
        char = line[col]
        # print(char)
        # print(char.isnumeric())
        if char == ".":
            if isPartNum:
                print("adding " + currentNum)
                sum += int(currentNum)
            currentNum = ""
            isPartNum = False
        elif char.isnumeric():
            if not isPartNum:
                if currentNum == "" and col > 0:
                    if row > 0:
                        # Back up diagonal
                        toCheck = lines[row-1][col-1]
                        # print("back up is " + toCheck)
                        isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())

                    # Back
                    toCheck = lines[row][col-1]
                    # print("back is " + toCheck)
                    isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())

                    if row < len(lines) - 1:
                        # Back down diagonal
                        toCheck = lines[row+1][col-1]
                        # print("back down is " + toCheck)
                        isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())

                if row > 0:
                    # Up
                    toCheck = lines[row-1][col]
                    # print("up is " + toCheck)
                    isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())
                
                if row < len(lines) - 1:
                    # Down
                    toCheck = lines[row+1][col]
                    # print("down is " + toCheck)
                    isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())
                
                # print("Line length is " + str(len(line)))
                # print(line[-1])
                if col < len(line) - 1 and not lines[row][col+1].isnumeric():
                    if row > 0:
                        # Up right diagonal
                        toCheck = lines[row-1][col+1]
                        # print("up right is " + toCheck)
                        isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())
                    
                    # Right
                    toCheck = lines[row][col+1]
                    # print("right is " + toCheck)
                    isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())

                    if row < len(lines) - 1:
                        # Down right diagonal
                        # print(row + 1)
                        # print(col + 1)
                        toCheck = lines[row+1][col+1]
                        # print(" down right is " + toCheck)
                        isPartNum = isPartNum or  (toCheck != "." and not toCheck.isnumeric())
                
            currentNum += char
        else:
            if isPartNum:
                print("adding " + currentNum)
                sum += int(currentNum)
            currentNum = ""
            isPartNum = False

    if isPartNum:
        print("adding " + currentNum)
        sum += int(currentNum)
    
print(sum)
