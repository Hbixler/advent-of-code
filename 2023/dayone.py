file = open("day_one_input.txt", "r")
map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
sum = 0
for line in file:
    firstDig = -1
    lastDig = -1
    for x in range(len(line)):
        char = line[x]
        if char.isnumeric():
            if firstDig == -1:
                firstDig = int(char)
            lastDig = int(char)
        else:
            for key in map.keys():
                if line[x:].find(key) == 0:
                    if firstDig == -1:
                        firstDig = map[key]
                    lastDig = map[key]

    sum += firstDig * 10
    sum += lastDig

print(sum)
