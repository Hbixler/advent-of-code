file = open("day_two_input.txt", "r")
map = {
    "red": 12,
    "green": 13,
    "blue": 14
}
isPossible = True
idSum = 0
for line in file:
    isPossible = True
    colonSplit = line.split(":")
    gameId = colonSplit[0].split(" ")[1]
    newLineSplit = colonSplit[1].split("\n")
    rounds = newLineSplit[0].split(";")
    for round in rounds:
        for cubeCount in round.split(","):
            cubeNum = cubeCount.split(" ")[1]
            cubeColor = cubeCount.split(" ")[2]
            if int(cubeNum) > map[cubeColor]:
                isPossible = False
    if isPossible:
        idSum += int(gameId)

print(idSum)


