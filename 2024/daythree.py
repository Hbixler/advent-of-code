import re

file = open("daythree.txt")
sum = 0
enabled = True
for line in file:
    dos = re.split("(do\(\))|(don't\(\))", line)
    for do in dos:
        if do == "do()":
            enabled = True
            continue
        elif do == "don't()":
            enabled = False
            continue
        if do != None and enabled:
            muls = re.findall("mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)", do)
            for mul in muls:
                nums = re.findall("(\([0-9]?[0-9]?[0-9])|([0-9]?[0-9]?[0-9]\))", mul)
                sum += int(nums[0][0][1:]) * int(nums[1][1][:-1])

print(sum)