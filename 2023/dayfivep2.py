import threading

file = open("day_five_input.txt")
maps = []
seeds = []

pastInput = False
currentList = []
for line in file:
    if "seeds" in line:
        originalSeeds = line.split(" ")[1:]
        for x in range(len(originalSeeds)):
            if x % 2 == 0:
                pair = [int(originalSeeds[x]), int(originalSeeds[x+1])]
                seeds.append([pair[0], pair[0] + pair[1] - 1])
                currentList.append([pair[0], pair[0] + pair[1] - 1, pair[0], pair[0] + pair[1] - 1])
        currentList.sort()
        maps.append(currentList)
        currentList = []
    elif "-" in line:
        # Is a map title
        pastInput = True
        # print("Adding new dictionary")
        if len(currentList) > 0:
            # print(currentList)
            currentList.sort()
            maps.append(currentList)
            currentList = []
    elif pastInput and len(line) > 1:
        # List item = [source start range, source end range, destination start, destination end]
        # print("Map key!")
        rangeItems = line.split(" ")
        # print([int(rangeItems[1]), int(rangeItems[1]) + int(rangeItems[2]), int(rangeItems[0]), int(rangeItems[0]) + int(rangeItems[2])])
        currentList.append([int(rangeItems[1]), int(rangeItems[1]) + int(rangeItems[2]) - 1, int(rangeItems[0]), int(rangeItems[0]) + int(rangeItems[2]) - 1])

currentList.sort()
maps.append(currentList)
mins = []
# print(maps)

currentMap = maps[0]
for x in range(1, len(maps)):
    # print(currentMap)
    y = 0
    while y < len(currentMap):
        # print(currentMap)
        sourceStart = currentMap[y][0]
        sourceEnd = currentMap[y][1]
        destStart = currentMap[y][2]
        destEnd = currentMap[y][3]
        destMap = maps[x]

        for destItem in destMap:

            if destStart >= destItem[0] and destStart <= destItem[1]:
                # Start fits within this range, check end
                if destEnd <= destItem[1]:
                    # Start and end both within range
                    currentMap[y][2] = destItem[2] + destStart - destItem[0]
                    currentMap[y][3] = destItem[2] + destEnd - destItem[0]
                else:
                    # Start within range, end borders over 
                    # print("end borders over:")
                    # print(currentMap[y])
                    currentMap[y][1] = sourceEnd - (destEnd - destItem[1])
                    currentMap[y][2] = destItem[2] + destStart - destItem[0]
                    currentMap[y][3] = destItem[3]
                    # print(currentMap[y])

                    currentMap.append([sourceEnd - (destEnd - destItem[1]) + 1, sourceEnd, destItem[1] + 1, destEnd])
                    break
            elif destStart < destItem[0] and destEnd >= destItem[0] and destEnd <= destItem[1]:
                # Start borders over but end overlaps
                print("start borders over")
                currentMap[y][1] = sourceEnd - (destEnd - destItem[1])
                currentMap[y][3] = destItem[3]

                currentMap.append([sourceStart + (destItem[0] - destStart), currentMap[y][1], destItem[1], destItem[3] - (destItem[1] - destEnd)])
                break
            elif destStart < destItem[0] and destEnd > destItem[1]:
                print("contained")
                currentMap[y][0] = sourceStart + (destItem[0] - destStart)
                currentMap[y][1] = sourceEnd - (destEnd - destItem[1])
                currentMap[y][2] = destItem[2]
                currentMap[y][3] = destItem[3]

                currentMap.append([sourceEnd - (destEnd - destItem[1]) + 1, sourceEnd, destItem[1] + 1, destEnd])
                break
        # print("At end: " + str(currentMap))
        y += 1

# print(currentMap)
    

seedLocations = []
# print(seeds)
# print(maps[0])
# print(seeds)
# print(mapArg)

currentMin = maps[0][0][2]

for item in maps[0][1:]:
    print(item)
    if item[2] < currentMin:
        currentMin = item[2]

# print(seedLocations)
print(currentMin)


