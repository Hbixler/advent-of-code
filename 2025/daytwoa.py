file = open("daytwo.txt")

doubleCounter = 0
ranges = []
for line in file:
    nums = line.split(",")
    for num in nums:
        vals = num.split("-")
        ranges.append([int(vals[0]), int(vals[1])])

for rangey in ranges:
    print("range is ", rangey)
    for x in range(rangey[0],rangey[1]+1):
        isDouble = False
        for danumber in range(1,len(str(x))):
            if len(str(x)) % danumber == 0:
                wordArr = []
                pointer = 0
                while pointer < len(str(x)):
                    wordArr.append(str(x)[pointer:pointer+danumber])
                    pointer += danumber
                if len(set(wordArr)) == 1:
                    print("found double at ", x)
                    isDouble = True
            if isDouble:
                doubleCounter += x
                break

print(doubleCounter)