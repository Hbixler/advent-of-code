file = open("day_four_input.txt")
sum = 0

for line in file:
    nums = line.split("|")
    nums[0] = [x for x in nums[0].split(":")[1].strip().split(" ") if len(x) > 0]
    nums[1] = [x for x in nums[1].strip().split(" ") if len(x) > 0]
    score = 0

    # print("Winning nums: " + str(nums[0]))
    # print("Nums: " + str(nums[1]))
    for num in nums[0]:
        count = nums[1].count(num)
        if count > 0 and score == 0:
            score = 1
            count -= 1
        for _ in range(count):
            score *= 2
    
    # print("Score: " + str(score))
    
    sum += score

print(sum)

