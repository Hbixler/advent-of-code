file = open("dayseven.txt")

def isValid(num1, index, arr, total):
    if index == len(arr):
        return num1 == total
    if num1 > total:
        return False
    num2 = arr[index]
    return isValid(num1 * num2, index + 1, arr, total) or isValid(num1 + num2, index + 1, arr, total) or isValid(int(str(num1) + str(num2)), index + 1, arr, total)

sumValues = 0
for line in file:
    numsSplit = line.split(":")
    total = int(numsSplit[0])
    nums = [int(x) for x in numsSplit[1].split(' ') if len(x) > 0]
    if isValid(nums[0], 1, nums, total):
        sumValues += total

print(sumValues)

    

