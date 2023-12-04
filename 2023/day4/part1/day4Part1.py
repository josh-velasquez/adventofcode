


def getCardPoint(line):
    cardNumbersLine = line.split(": ")[1]
    cardNumbers = cardNumbersLine.split(" | ")
    winningNumbers = cardNumbers[0].split(" ")
    handNumbers = cardNumbers[1].split(" ")
    winningNumbersHashMap = {}
    for i in winningNumbers:
        winningNumbersHashMap[i] = i
    
    cardPoint = 0
    for i in handNumbers:
        if (i in winningNumbersHashMap and i != ''):
            cardPoint += 1
    
    if (cardPoint == 0):
        return 0
    else:
        return 2**(cardPoint - 1)


def main():
    file = open('input1.txt','r')
    line = file.readline()
    
    cardPoints = 0
    while(line):
        linePoint = getCardPoint(line.replace('\n',''))
        cardPoints += linePoint
        line = file.readline()
        
    print(cardPoints)

main()