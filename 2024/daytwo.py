file = open("daytwosample.txt")

def isReportSafe(report):
    removeLevel = False
    nums = [int(x) for x in report]
    prevNum = nums[1]
    currentDiff = nums[1] - nums[0]
    print(nums)
    if abs(currentDiff) < 1 or abs(currentDiff) > 3:
        removeLevel = True
    for x in range(2,len(nums)):
        diff = nums[x] - prevNum
        if abs(diff) < 1 or abs(diff) > 3:
            # print("going to remove level")
            if (removeLevel):
                return False
            else:
                removeLevel = True
                continue
        if diff * currentDiff < 0:
            if (removeLevel):
                return False
            else:
                removeLevel = True
                continue
        currentDiff = diff
        prevNum = nums[x]
    print(nums)
    return True

numSafe = 0
for line in file:
    nums = line.split(" ")
    if isReportSafe(nums):
        numSafe += 1

print("num safe: " + str(numSafe))