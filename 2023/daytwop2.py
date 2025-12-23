file = open("day_two_input.txt", "r")
powerSum = 0
for line in file:
    colonSplit = line.split(":")
    newLineSplit = colonSplit[1].split("\n")
    rounds = newLineSplit[0].split(";")
    minMap = {
            "red": 0,
            "green": 0,
            "blue": 0
    }
    for round in rounds:
        for cubeCount in round.split(","):
            cubeNum = int(cubeCount.split(" ")[1])
            cubeColor = cubeCount.split(" ")[2]
            if cubeNum > minMap[cubeColor]:
                minMap[cubeColor] = cubeNum
    power = 1
    for key in minMap.keys():
        power *= minMap[key]
    powerSum += power

print(powerSum)