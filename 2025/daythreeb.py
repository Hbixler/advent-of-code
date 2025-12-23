file = open("daythree.txt")

sum = 0
for line in file:
    finalNum = ""
    numArr = [int(x) for x in line if x != '\n']
    currentPos = -1
    for x in range(12,0,-1):
        sliceArr = numArr[currentPos+1:len(numArr)-x+1]
        #print("numArr is ", sliceArr)
        maxNum = max(sliceArr)
        #print("max is ", maxNum)
        currentPos = sliceArr.index(maxNum) + currentPos + 1
        finalNum += str(maxNum)
    
    print(finalNum)
    sum += int(finalNum)

print(sum)