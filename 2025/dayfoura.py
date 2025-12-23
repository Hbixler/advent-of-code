file = open("dayfour.txt")

paperMap = []
numMap = []
for line in file:
    if line[-1] == '\n':
        paperMap.append(line[:-1])
        numMap.append([0 for x in line[:-1]])
    else:
        paperMap.append(line)
        numMap.append([0] * len(line))

for y in range(0,len(numMap)):
    for x in range(0,len(numMap[0])):
        # x,y is coordinate we are looking at

        if paperMap[y][x] != "@":
            continue

        for offY in range(-1,2):
            for offX in range(-1,2):
                # offY, offX is the one we are marking

                if offY == 0 and offX == 0:
                    continue

                if y + offY >= 0 and x + offX >= 0 and y + offY < len(numMap) and x + offX < len(numMap[0]):
                    #print("off y ", numMap[y + offY])
                    #print("off x ", numMap[y + offY][x + offX])
                    numMap[y + offY][x + offX] += 1

fourCounter = 0
for y in range(0,len(numMap)):
    for x in range(0,len(numMap[0])):
        if paperMap[y][x] == "@" and numMap[y][x] < 4:
            fourCounter += 1

print(fourCounter)

