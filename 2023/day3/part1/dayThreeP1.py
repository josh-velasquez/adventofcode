
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
    return num


def findTotalNumAdjacentToSymbols(arr, symbolsCoord):
    sum = 0
    for i in symbolsCoord:
        # check left
        if ((i[1] - 1) >= 0):
            num = arr[i[0]][i[1] - 1]
            # print('LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0], i[1]-1])
                sum += int(newVal)
        
        # check top left
        if ((i[0] - 1) >= 0 and (i[1] - 1) >= 0):
            num = arr[i[0]-1][i[1]-1]
            # print('TOP LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]-1])
                sum += int(newVal)
        
        # check top
        if ((i[0] - 1) >= 0):
            num = arr[i[0]-1][i[1]]
            # print('TOP: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]])
                sum += int(newVal)
                
        # check top right
        if ((i[0] - 1) >= 0 and (i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]-1][i[1]+1]
            # print('TOP RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]-1, i[1]+1])
                sum += int(newVal)
        
        # check right
        if ((i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]][i[1] + 1]
            # print('RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0], i[1]+1])
                sum += int(newVal)
        
        # check bottom right
        if ((i[0] + 1) <= len(arr) - 1 and (i[1] + 1) <= len(arr[0]) - 1):
            num = arr[i[0]+1][i[1]+1]
            # print('BOTTOM RIGHT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]+1, i[1]+1])
                sum += int(newVal)
        
        # check bottom
        # [8,3]
        if ((i[0] + 1) <= len(arr) - 1):
            num = arr[i[0] + 1][i[1]]
            # print('BOTTOM: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0] + 1, i[1]])
                sum += int(newVal)
                
        # check bottom left
        if ((i[0] + 1) <= len(arr) - 1 and (i[1] - 1) >= 0):
            num = arr[i[0]+1][i[1]-1]
            # print('BOTTOM LEFT: ', num)
            if num.isnumeric():
                newVal = processAdjacentNum(arr, [i[0]+1, i[1]-1])
                sum += int(newVal)
    # print(arr)
    return sum

def getSymbolCoordInLine(line, row):
    symbolCoord = []
    for i in range(0, len(line)):
        if (not line[i].isnumeric() and line[i] != '.' and line[i] != ' '):
            symbolCoord.append([row, i])
    return symbolCoord

def main():
    file = open('input1.txt', 'r')
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
    totalSum = findTotalNumAdjacentToSymbols(arr, symbolsCoord)
    
    print(totalSum)

main()