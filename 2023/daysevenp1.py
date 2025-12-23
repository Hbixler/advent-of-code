from collections import Counter
from enum import Enum
import functools

file = open("day_seven_input.txt")

cardMap = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}
class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

def compare(hand1Full, hand2Full):
    hand1 = hand1Full[0]
    hand2 = hand2Full[0]

    hand1Count = [Counter(hand1)[key] if key != "J" else 0 for key in Counter(hand1)]
    hand1Count.sort(reverse=True)
    hand2Count = [Counter(hand2)[key] if key != "J" else 0 for key in Counter(hand2)]
    hand2Count.sort(reverse=True)

    hand1Type = HandType.HIGH_CARD
    hand2Type = HandType.HIGH_CARD

    # print(hand1)
    # print(hand1Count)
    for _ in range(hand1.count("J")):
        for x in range(len(hand1Count)):
            if hand1Count[x] < 5:
                hand1Count[x] += 1
                break
    # print(hand1Count)
    
    for _ in range(hand2.count("J")):
        for x in range(len(hand2Count)):
            if hand2Count[x] < 5:
                hand2Count[x] += 1
                break

    if 5 in hand1Count:
        hand1Type = HandType.FIVE_KIND
    elif 4 in hand1Count:
        hand1Type = HandType.FOUR_KIND
    elif 3 in hand1Count:
        # print("There is a 3!")
        # print(hand1Count)
        if 2 in hand1Count:
            hand1Type = HandType.FULL_HOUSE
        else:
            hand1Type = HandType.THREE_KIND
    elif 2 in hand1Count:
        if hand1Count.count(2) == 2:
            hand1Type = HandType.TWO_PAIR
        else:
            hand1Type = HandType.ONE_PAIR
    
    if 5 in hand2Count:
        hand2Type = HandType.FIVE_KIND
    elif 4 in hand2Count:
        hand2Type = HandType.FOUR_KIND
    elif 3 in hand2Count:
        if 2 in hand2Count:
            hand2Type = HandType.FULL_HOUSE
        else:
            hand2Type = HandType.THREE_KIND
    elif 2 in hand2Count:
        if hand2Count.count(2) == 2:
            hand2Type = HandType.TWO_PAIR
        else:
            hand2Type = HandType.ONE_PAIR
    
    #  print(hand1Type)
    if hand1Type == hand2Type:
        for x in range(len(hand1)):
            if hand1[x] != hand2[x]:
                return cardMap[hand1[x]] - cardMap[hand2[x]]
        return 0
    else:
        return hand1Type.value - hand2Type.value
        
hands = []

for line in file:
    handSplit = line.split(" ")
    hands.append([handSplit[0], int(handSplit[1])])

hands = sorted(hands, key=functools.cmp_to_key(compare))

print(hands)

winnings = 0

for x in range(len(hands)):
    winnings += (x + 1) * hands[x][1]

print(winnings)