file = open("dayfive.txt")

ranges = []

isRange = True
freshCounter = 0
for line in file:
    if line == "\n":
        isRange = False
        continue

    if isRange:
        rangeToInsert = [int(line.split("-")[0]), int(line[:-1].split("-")[1])]
        reachedFinalState = False

        if len(ranges) == 0:
            ranges.append(rangeToInsert)

        for x in range(len(ranges)):
            arrRange = ranges[x]
            begin = rangeToInsert[0]
            end = rangeToInsert[1]

            if begin < arrRange[0]:
                # entire thing goes before
                if end < arrRange[0]:
                    ranges.insert(x, rangeToInsert)
                    reachedFinalState = True
                    break

                # overlap in beginning
                if end >= arrRange[0]:
                    # end occurs in interval
                    if end <= arrRange[1]:
                        arrRange[0] = begin
                        reachedFinalState = True
                        break
                    
                    # end is after interval
                    if end > arrRange[1]:
                        # we don't need old range anymore, null it out and see where this range fits next
                        arrRange[0] = -1
                        arrRange[1] = -1
                        continue

            if begin >= arrRange[0]:
                # entirely goes after
                if begin >= arrRange[1]:
                    continue

                # entirely in middle
                if end <= arrRange[1]:
                    # we don't need the range
                    reachedFinalState = True
                    break
                
                # overlap at end
                if end > arrRange[1]:
                    # we don't need old range anymore, null it out and see where new range fits next
                    rangeToInsert[0] = arrRange[0]
                    arrRange[0] = -1
                    arrRange[1] = -1
                    continue
        
        if not reachedFinalState:
            # must go at the end
            ranges.append(rangeToInsert)
        
        # take out nulled out values
        ranges = [x for x in ranges if x[0] != -1]
    
    if not isRange:
        # getting ingredients now!
        ingredient = int(line.strip())

        for arrRange in ranges:
            if ingredient >= arrRange[0] and ingredient <= arrRange[1]:
                freshCounter += 1
                break

print(ranges)
print(freshCounter)