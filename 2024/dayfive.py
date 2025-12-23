from collections import defaultdict
from functools import cmp_to_key

file = open("dayfive.txt")

ruleMap = defaultdict(list)
sum = 0
badSum = 0

def compare(a, b):
    if a in ruleMap[b]:
        return 1
    elif b in ruleMap[a]:
        return -1
    else:
        return 0

for line in file:
    if "," in line:
        # solution
        good = True
        nums = [int(x) for x in line.split(",")]
        for x in range(len(nums)):
            num = nums[x]
            follows = ruleMap[num]
            for follow in follows:
                if follow in nums[:x]:
                    good = False
                    break
        if good:
            # print(nums[len(nums) // 2])
            sum += nums[len(nums) // 2]
        else:
            nums.sort(key=cmp_to_key(compare))
            badSum += nums[len(nums) // 2]
    elif "|" in line:
        # rules
        rule = line.split("|")
        ruleMap[int(rule[0])].append(int(rule[1]))

# print(ruleMap)
print(badSum)
