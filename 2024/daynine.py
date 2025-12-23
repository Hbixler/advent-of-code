file = open("daynine.txt")

fileMap = []
for line in file:
    id = 0
    rep = []
    for x in range(0,len(line),2):
        rep += [str(id)] * int(line[x])
        if x + 1 < len(line):
            rep += ["."] * int(line[x+1])
        id += 1
    fileMap += rep

print(fileMap)
start = 0
end = len(fileMap) - 1
while start < end:
    head = fileMap[start]
    tail = fileMap[end]

    if head != ".":
        start += 1
    if tail == ".":
        end -= 1
    
    if head == "." and tail != ".":
        fileMap = fileMap[:start] + [tail] + fileMap[start+1:end]
        # print(fileMap)
        start += 1
        end -= 1

print(fileMap)

checksum = 0
for index in range(len(fileMap)):
    checksum += index * int(fileMap[index])

print(checksum)


