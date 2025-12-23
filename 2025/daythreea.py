file = open("daythree.txt")

sum = 0
for line in file:
    finalNum = 0
    numArr = [int(x) for x in line if x != '\n']
    maxNum = max(numArr)

    # only edge case is if max is in last position
    if numArr.index(maxNum) == len(numArr) - 1:
        finalNum = max(numArr[:len(numArr)-1]) * 10 + maxNum
    else:
        finalNum = maxNum * 10 + max(numArr[numArr.index(maxNum)+1:])
    
    #print(finalNum)
    sum += finalNum

print(sum)