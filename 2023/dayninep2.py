file = open("day_nine_input.txt")
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
    firstVals = []
    currentLine = sequence[:]
    while currentLine.count(0) != len(currentLine):
        newLine = []
        for x in range(len(currentLine)):
            # print(currentLine)
            num = currentLine[x]
            if x != len(currentLine) - 1:
                diff = currentLine[x+1] - num
                newLine.append(diff)
            if x == 0:
                firstVals.append(num)
        print(currentLine)
        currentLine = newLine[:]

    initialVal = firstVals[0]
    for x in range(1, len(firstVals)):
        if x % 2 == 0:
            initialVal += firstVals[x]
        else:
            initialVal -= firstVals[x]

    print("First Vals: " + str(firstVals))
    print("Seq: " + str(initialVal))
    seqSum += initialVal

print(seqSum)
