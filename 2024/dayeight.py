from collections import defaultdict

file = open("dayeight.txt")

antennae = defaultdict(list)
points = set()
maxWidth = 0
maxHeight = -1

for line in file:
    maxHeight += 1
    maxWidth = -1
    for char in line:
        if char != "\n":
            maxWidth += 1
            if char != ".":
                print(char)
                antennae[char].append([maxHeight, maxWidth])

# print(maxHeight)
# print(maxWidth)

for key in antennae.keys():
    listy = antennae[key]
    # print(listy)
    for index in range(len(listy)):
        item = listy[index]
        if len(listy) > 2:
            points.add(str(item))
        for compare in listy[index+1:]:
            # print("item: " + str(item) + ", compare: " + str(compare))
            widthDiff = item[1] - compare[1]
            heightDiff = item[0] - compare[0]

            # potentialPoints = [(item[0] + heightDiff, item[1] + widthDiff), (item[0] - (heightDiff * 2), item[1] - (widthDiff * 2))]
            # print(potentialPoints)

            smallPoint = [item[0] + heightDiff, item[1] + widthDiff]
            largePoint = [item[0] - (heightDiff * 2), item[1] - (widthDiff * 2)]

            while (smallPoint[0] >= 0 and smallPoint[0] <= maxHeight and smallPoint[1] >= 0 and smallPoint[1] <= maxWidth):
                points.add(str(smallPoint))
                smallPoint[0] += heightDiff
                smallPoint[1] += widthDiff

                print(smallPoint)
            
            while (largePoint[0] >= 0 and largePoint[0] <= maxHeight and largePoint[1] >= 0 and largePoint[1] <= maxWidth):
                points.add(str(largePoint))
                largePoint[0] -= heightDiff
                largePoint[1] -= widthDiff

print(points)
print(len(points))
