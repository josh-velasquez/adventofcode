
def processAdjacentNum(arr, coord):
    # we only check the row
    row = coord[0]
    col = coord[1]
    num = arr[row][col]
    arr[row][col] = '.'
    # scan left of the num (keep decreasing col until we're all the way to the left)
    while(col >= 0):
        newVal = arr[row][col - 1]
        if (newVal.isnumeric()):
            num = newVal + num
        else:
            break
        col -= 1
        arr[row][col] = '.'
	# scan right of the num
    col = coord[1]
    while(col < len(arr[0]) - 1):
        newVal = arr[row][col + 1]
        if (newVal.isnumeric()):
            num = num + newVal
        else:
            break
        col += 1
        arr[row][col] = '.'
    return int(num)


def findTotalNumAdjacentToSymbols(arr, symbolsCoord):
    adjacentPower = []
    for i in symbolsCoord:
        # check left
        adjacentTempPower = 1
        adjacentCounter = 0
        if ((i[1] - 1) >= 0):
            num = arr[i[0]][i[1] - 1]
            # print('LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0], i[1]-1])
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
        
        # check top left
        if ((i[0] - 1) >= 0 and (i[1] - 1) >= 0):
            num = arr[i[0]-1][i[1]-1]
            # print('TOP LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]-1])
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
        
        # check top
        if ((i[0] - 1) >= 0):
            num = arr[i[0]-1][i[1]]
            # print('TOP: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]])
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
                
        # check top right
        if ((i[0] - 1) >= 0 and (i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]-1][i[1]+1]
            # print('TOP RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]+1])
                
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
        
        # check right
        if ((i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]][i[1] + 1]
            # print('RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0], i[1]+1])
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
        
        # check bottom right
        if ((i[0] + 1) <= len(arr) - 1 and (i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]+1][i[1]+1]
            # print('BOTTOM RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]+1, i[1]+1])
                
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
        
        # check bottom
        if ((i[0] + 1) <= len(arr) - 1):
            num = arr[i[0] + 1][i[1]]
            # print('BOTTOM: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0] + 1, i[1]])
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1
                
        # check bottom left
        if ((i[0] + 1) <= len(arr) - 1 and (i[1] - 1) >= 0):
            num = arr[i[0]+1][i[1]-1]
            # print('BOTTOM LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]+1, i[1]-1])
                
                if (adjacentCounter <= 2):
                    adjacentTempPower *= newVal
                    adjacentCounter += 1

        if (adjacentTempPower != 1 and adjacentCounter == 2):
            adjacentPower.append(adjacentTempPower)

    return adjacentPower

def getSymbolCoordInLine(line, row):
    symbolCoord = []
    for i in range(0, len(line)):
        if (not line[i].isnumeric() and line[i] != '.' and line[i] != ' '):
            symbolCoord.append([row, i])
    return symbolCoord

def main():
    file = open('input2.txt', 'r')
    line = file.readline()
    
    arr = []
    symbolsCoord = []
    row = 0
    while(line):
        lineArr = list(line.replace('\n',''))
        # print(lineArr)
        coord = getSymbolCoordInLine(lineArr, row)
        arr.append(lineArr)
        symbolsCoord += coord
        row += 1
        line = file.readline()
    
    # arr will contain the 2d array
    # symbolsCoord will contain the symbols found coordinate
    # print(symbolsCoord)
    totalPowers = findTotalNumAdjacentToSymbols(arr, symbolsCoord)
    totalSum = 0
    for i in totalPowers:
        totalSum += i
    print(totalSum)

main()