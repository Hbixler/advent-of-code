file = open("day_eight_input.txt")

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

currentNode = "AAA"
currentCount = 0
instructionCount = 0

while currentNode != "ZZZ":
    # print(currentNode)
    if instructions[instructionCount] == "R":
        currentNode = graphMap[currentNode][1]
    else:
        currentNode = graphMap[currentNode][0]
    instructionCount = (instructionCount + 1) % len(instructions)
    currentCount += 1

print(currentCount)
