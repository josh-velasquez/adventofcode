

def isHighCard(handDic):
    return len(handDic) == 5

def isFullHouse(handDic):
    return isOfAKind(handDic, 3) and isOfAKind(handDic, 2)

# checks if its of a kind
# 5 = five of a kind
# 4 = four of a kind
# 3 = three of a kind
# 2 = two pair (special case)
# 1 = one pair (special case)
def isOfAKind(handDic, kind):
    if (kind == 1):
        return len(handDic) == 4
    elif (kind == 2):
        pair = 0
        for _, value in handDic.items():
            if (value == 2):
                pair += 1
        return pair == 2
    elif(kind == 3):
        for _, value in handDic.items():
            if (value == 3):
                return True
        return False
    elif(kind == 4):
        return (len(handDic) == 2)
    elif (kind == 5):
        return (len(handDic) == 1)
    return False

    
def checkHand(hand):
    handDict = {}
    for i in hand:
        if (handDict.get(i) != None):
            handDict[i] = handDict.get(i) +  1
        else:
            handDict[i] = 1
    print(handDict)
    if (isOfAKind(handDict, 5)):
        return 7
        # return "FIVE_OF_A_KIND"
    if(isOfAKind(handDict, 4)):
        return 6
        # return 'FOUR_OF_A_KIND'
    elif(isFullHouse(handDict)):
        return 5
        # return 'FULL_HOUSE'
    if(isOfAKind(handDict, 3)):
        return 4
        # return "THREE_OF_A_KIND"
    if(isOfAKind(handDict, 2)):
        return 3
        # return 'TWO_PAIR'
    if (isOfAKind(handDict, 1)):
        return 2
        # return 'ONE_PAIR'
    if (isHighCard(handDict)):
        return 1
        # return 'HIGH_CARD'
    return 0


def main():
    file = open('sample.txt', 'r')
    line = file.readline()
    handsList = {}
    while(line):
        hands = line.replace('\n','').split(' ')
        handsList[hands[0]] = hands[1]
        line = file.readline()
    
    # main logic where we populate the ranks based on the value of hand
    ranking = []
    unsortedRankings = []
    for hand, value in handsList.items():
        unsortedRankings.append(checkHand(hand))
        
    print(unsortedRankings)
    # merge sort along their rankings?
    
    # deal with their local rankings (resolve tie breakers) and make sure you update ranking
    # we need to pass in the tie breakers array and then compare them to each other one by one and do 
    # a local ranking
    
        
    # get total rankings
    # total = 0
    # for i in range(0, len(ranking)):
    #     total += (ranking[i] * (i + 1))
    # return total


main()