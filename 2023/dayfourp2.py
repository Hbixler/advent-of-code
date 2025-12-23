from collections import defaultdict

file = open("day_four_input.txt")
cardCounts = defaultdict(lambda: 1)
sum = 0
cardNum = 1

for line in file:
    nums = line.split("|")
    nums[0] = [x for x in nums[0].split(":")[1].strip().split(" ") if len(x) > 0]
    nums[1] = [x for x in nums[1].strip().split(" ") if len(x) > 0]
    score = 0

    print("Card num: " + str(cardNum))
    print("Copies: " + str(cardCounts[cardNum]))
    # print("Winning nums: " + str(nums[0]))
    # print("Nums: " + str(nums[1]))
    for num in nums[0]:
        count = nums[1].count(num)
        for _ in range(count):
            score += 1
    
    for x in range(1, score + 1):
        cardCounts[cardNum + x] += cardCounts[cardNum]
    
    # print("Score: " + str(score))
    
    sum += cardCounts[cardNum]
    cardNum += 1

print(sum)
