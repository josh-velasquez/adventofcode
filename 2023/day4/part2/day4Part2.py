
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
    
    return cardPoint


def main():
    file = open('input.txt','r')
    line = file.readline()
    
    scoreArr = []
    while(line):
        multiplier = getCardPoint(line.replace('\n',''))
        scoreArr.append([1, multiplier])
        line = file.readline()

    for i in range(0, len(scoreArr)):
        scoreToDistribute = scoreArr[i][1]
        multiplier = scoreArr[i][0]
        for j in range(i + 1, len(scoreArr)):
            if (scoreToDistribute != 0):
                scoreArr[j][0] = scoreArr[j][0] + multiplier
                scoreToDistribute -= 1
            else:
                break

    totalSum = 0
    for i in range(0, len(scoreArr)):
        totalSum += scoreArr[i][0]
    print(totalSum)
main()
