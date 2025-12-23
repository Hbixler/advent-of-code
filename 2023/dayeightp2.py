from math import gcd

file = open("Dec8Input.txt")

graphMap = {}
instructions = ""

for line in file:
    if "\n" in line:
        line = line[:-1]
    if len(instructions) == 0:
        instructions = line
    elif "=" in line:
        splitSpace = line.split(" ")
        graphMap[splitSpace[0]] = [splitSpace[2][1:-1], splitSpace[3][:-1]]

startNodes = []
for key in graphMap.keys():
    if key[-1] == "A":
        startNodes.append(key)

currentNodes = startNodes[:]
currentCount = 0
instructionCount = 0
endCondition = False
steps = [0] * len(currentNodes)
print(steps)

while 0 in steps:
    for x in range(len(currentNodes)):
        node = currentNodes[x]
        if instructions[instructionCount] == "R":
            currentNodes[x] = graphMap[node][1]
        else:
            currentNodes[x] = graphMap[node][0]
    instructionCount = (instructionCount + 1) % len(instructions)
    currentCount += 1

    for x in range(len(currentNodes)):
        if currentNodes[x][-1] == "Z" and steps[x] == 0:
            steps[x] = currentCount
            print(steps)

lcm = 1
for stepCount in steps:
    lcm = lcm * stepCount // gcd(lcm, stepCount)

print(lcm)
