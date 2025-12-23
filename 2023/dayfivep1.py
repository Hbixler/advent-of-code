file = open("day_five_input.txt")
maps = []
seeds = []

pastInput = False
currentList = []
for line in file:
    if "seeds" in line:
        seeds = line.split(" ")[1:]
    elif "-" in line:
        # Is a map title
        pastInput = True
        # print("Adding new dictionary")
        if len(currentList) > 0:
            # print(currentList)
            maps.append(currentList)
            currentList = []
    elif pastInput and len(line) > 1:
        # List item = [source start range, source end range, destination start]
        # print("Map key!")
        rangeItems = line.split(" ")
        currentList.append([int(rangeItems[1]), int(rangeItems[1]) + int(rangeItems[2]), int(rangeItems[0])])

maps.append(currentList)

seedLocations = []
for seed in seeds:
    code = int(seed)
    for listy in maps:
        # print(code)
        # print(map)
        # print(pair)
        for pair in listy:
            if code >= pair[0] and code <= pair[1]:
                code = pair[2] + (code - pair[0])
                break
    seedLocations.append(code)

print(min(seedLocations))

