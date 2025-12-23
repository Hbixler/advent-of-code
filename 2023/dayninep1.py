file = open("Dec9Input.txt")
sequences = []
seqSum = 0

for line in file:
    lineArr = []
    splitSpace = line.split(" ")
    for item in splitSpace:
        if len(item) > 0:
            lineArr.append(int(item))
    sequences.append(lineArr)

for sequence in sequences:
    lastVals = []
    currentLine = sequence[:]
    print(currentLine)
    # print(currentLine.count(0))
    while currentLine.count(0) != len(currentLine):
        newLine = []
        for x in range(len(currentLine)):
            # print(currentLine)
            num = currentLine[x]
            if x != len(currentLine) - 1:
                diff = currentLine[x+1] - num
                newLine.append(diff)
            else:
                lastVals.append(num)
        # print(currentLine)
        currentLine = newLine[:]

    # print("Last Vals: " + str(lastVals))
    print("Seq: " + str(sum(lastVals)))
    seqSum += sum(lastVals)

print("Total: " + str(seqSum))
