file = open("daysix.txt")

massiveArr = []
finalSum = 0
for line in file:

    if line[0] == "*" or line[0] == "+":
        # time to do the operations
        opps = [x for x in line.strip().split(" ") if len(x) > 0]

        tracker = 0
        currentOpp = opps[tracker]
        currentProdOrSum = 0 if currentOpp == "+" else 1

        for item in massiveArr:
            if len(item.strip()) == 0:
                if "\n" in item:
                    finalSum += currentProdOrSum
                    break

                # next opp
                # print("adding ", currentProdOrSum)
                finalSum += currentProdOrSum
                tracker += 1
                currentOpp = opps[tracker]
                currentProdOrSum = 0 if currentOpp == "+" else 1
                continue
            
            if currentOpp == "+":
                currentProdOrSum += int(item.strip())
            if currentOpp == "*":
                currentProdOrSum *= int(item.strip())
        break
    
    for x in range(len(line)):
        if (len(massiveArr) >= x + 1):
            massiveArr[x] += line[x]
        else:
            massiveArr.append(line[x])

    
#print(numsArr)
# print(massiveArr)
print(finalSum)


