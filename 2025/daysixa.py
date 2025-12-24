file = open("daysix.txt")

numsArr = []
finalSum = 0
for line in file:
    if line[0] == "*" or line[0] == "+":
        # time to do the operations
        opps = [x for x in line.strip().split(" ") if len(x) > 0]
        for x in range(len(opps)):
            if opps[x] == "*":
                product = 1
                for num in numsArr[x]:
                    product *= num
                finalSum += product
            if opps[x] == "+":
                finalSum += sum(numsArr[x])
        break
    
    numChars = [x for x in line.strip().split(" ") if len(x) > 0]
    for x in range(len(numChars)):
        if (len(numsArr) >=  x + 1):
            numsArr[x].append(int(numChars[x]))
        else:
            numsArr.append([int(numChars[x])])
    
#print(numsArr)
print(finalSum)

