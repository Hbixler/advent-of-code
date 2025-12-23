from collections import Counter

file = open("dayone.txt")

arr1 = []
arr2 = []
distance = 0
for line in file:
    splitVersion = line.split("   ")
    arr1.append(int(splitVersion[0]))
    arr2.append(int(splitVersion[1]))

arr1.sort()
arr2.sort()

for x in range(len(arr1)):
    distance += abs(arr1[x] - arr2[x])

print("P1: " + str(distance))

counter = Counter(arr2)
sim = 0

for num in arr1:
    sim += counter[num] * num

print("P2: " + str(sim))