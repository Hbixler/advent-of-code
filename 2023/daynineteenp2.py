file = open("day_nineteen_input.txt")

onWorkflows = True
workflows = {}
parts = []

for line in file:
    if "\n" in line:
        line = line[:-1]
    if len(line) == 0:
        onWorkflows = False
        continue
    if onWorkflows:
        flowName = line.split("{")[0]
        flows = line[len(flowName) + 1:-1].split(",")
        workflows[flowName] = flows
    else:
        partsArr = line[1:-1].split(",")
        partsMap = {}
        for item in partsArr:
            partsMap[item.split("=")[0]] = int(item.split("=")[1])
        parts.append(partsMap)

sum = 0

for part in parts:
    currentFlow = "in"

    while currentFlow != "A" and currentFlow != "R":
        for item in workflows[currentFlow]:
            if ":" in item:
                # Condition
                conditional = item.split(":")[0]
                if "<" in item:
                    feature = conditional.split("<")[0]
                    condition = int(conditional.split("<")[1])
                    if part[feature] < condition:
                        currentFlow = item.split(":")[1]
                        break
                else:
                    feature = conditional.split(">")[0]
                    condition = int(conditional.split(">")[1])
                    if part[feature] > condition:
                        currentFlow = item.split(":")[1]
                        break
            else:
                currentFlow = item
                break
    
    if currentFlow == "A":
        for rating in part:
            sum += part[rating]

print(sum)
