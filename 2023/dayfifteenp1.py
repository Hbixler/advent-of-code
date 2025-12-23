from collections import defaultdict

file = open("day_fifteen_input.txt")

codes = []
map = defaultdict(lambda: [])

for line in file:
    codes += line.split(",")

def getHash(code):
    currentVal = 0
    for char in code:
        currentVal += ord(char)
        currentVal *= 17
        currentVal %= 256
    return str(currentVal)

for code in codes:
    if "-" in code:
        label = code.split("-")[0]
        hash = getHash(label)
        arr = map[hash]        
        for x in range(len(arr)):
            item = arr[x]
            # print(item)
            if item.split(" ")[0] == label:
                arr.pop(x)
                # print("getting rid of it!")
                break
    else:
        label = code.split("=")[0]
        focus = code.split("=")[1]
        hash = getHash(label)
        arr = map[hash]
        for x in range(len(arr) + 1):
            if x == len(arr):
                arr.append(label + " " + focus)
            item = arr[x]
            if item.split(" ")[0] == label:
                arr[x] = label + " " + focus
                break
    # for key in map.keys():
        # print(key)
        # print(map[key])
        # print("-----")

sum = 0
for key in map.keys():
    boxArr = map[key]
    boxNum = 1 + int(key)
    # print(key)
    # print(boxArr)
    for x in range(len(boxArr)):
        sum += boxNum * (x + 1) * int(boxArr[x].split(" ")[1])

print(sum)
