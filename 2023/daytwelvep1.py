"""

STR ? STR ? STR ? STR ? STR

Find STR, ?STR, STR?, and ?STR?

OPTIONS

STR? + STR? + STR? + STR? + STR

STR? + STR? + STR? + STR + ?STR


STR + ?STR? + STR? + STR? + STR

"""

import itertools

file = open("day_twelve_sample.txt")

rows = []
for line in file:
    if "\n" in line:
        rows.append(line[:-1])
    else:
        rows.append(line)

def isValidCombo(nonoStr, numsArr):
    nonoNums = [ len(x) for x in nonoStr.split(".") if len(x) > 0 ]
    return nonoNums == numsArr

comboSum = 0

for row in rows:
    rowSum = 0
    numsStr = row.split(" ")[1]
    origNumsArr = [int(x) for x in numsStr.split(",")]
    origNonoStr = row.split(" ")[0]

    nonoStr = origNonoStr[:]
    numsArr = origNumsArr[:]

    """
    nonoStr = ""
    numsArr = []

    for _ in range(5):
        if len(nonoStr) > 0:
            nonoStr += "?"
        nonoStr += origNonoStr[:]
        numsArr += origNumsArr[:]
    """

    print(nonoStr)
    print(numsArr)

    strList = [nonoStr, "?" + nonoStr, nonoStr + "?", "?" + nonoStr + "?"]

    for item in strList:

        itemCount = 0
        toAdd = sum(numsArr) - item.count("#")
        canAdd = []
        
        for x in range(len(item)):
            if item[x] == "?":
                canAdd.append(x)
        
        nonoCombos = list(itertools.combinations(canAdd, toAdd))

        print(len(nonoCombos))

        for combo in nonoCombos:
            completeStr = list(item)
            for x in range(len(completeStr)):
                if completeStr[x] == "?":
                    if x in combo:
                        completeStr[x] = "#"
                    else:
                        completeStr[x] = "."
            completeStr = "".join(completeStr)
            # print(completeStr)
            # print(numsArr)
            if isValidCombo(completeStr, numsArr):
                # print(completeStr)
                # print(numsArr)
                # print("valid!")
                rowSum += 1
                itemCount += 1
                comboSum += 1
        
        print("str is " + item)
        print("count is " + str(itemCount))
    
    print("row has " + str(rowSum))
    
print(comboSum)
    

