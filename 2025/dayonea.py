file = open("dayone.txt")

zeroCounter = 0
currentNum = 50

for line in file:
    direction = line[0]
    num = int(line[1:])
    pastNum = currentNum

    if num > 99:
         zeroCounter += num // 100
         num = num % 100

    if direction == 'L':
        currentNum = (currentNum - num) % 100
        if currentNum > pastNum and currentNum != 0 and pastNum != 0:
             zeroCounter += 1
             print("down down")
    else:
        currentNum = (currentNum + num) % 100
        if currentNum < pastNum and currentNum != 0 and pastNum != 0:
             zeroCounter += 1
             print('up up')
    
    if currentNum == 0:
            zeroCounter += 1
            print("even steven")
    
    print("current num is " + str(currentNum))

print(zeroCounter)