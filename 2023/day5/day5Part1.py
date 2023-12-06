
def getValuesArray(start, ranges):
    return [element for element in range(start, start + ranges)]

# guaranteed to one mapping that exists
def getSoilLocationNumber(seed, gardenDic):
    # loop over the dictionary and map out the seed
    mappingPath = []
    intSeed = int(seed)
    mappingPath.append(intSeed)
    for key, values in gardenDic.items():
        # process the seed first
        for value in values:
            start1, start2, range = value
            firstRange = getValuesArray(int(start1), int(range))
            secondRange = getValuesArray(int(start2), int(range))
            # check if seed exists in the first mapping
            
            if (intSeed in secondRange):
                # check if seed is in the second mapping
                mappingIndex = secondRange.index(intSeed)
                if (mappingIndex != 0):
                    mappingPath.append(firstRange[mappingIndex])
                    intSeed = firstRange[mappingIndex]
                else:
                    mappingPath.append(int(start1))
                    intSeed = int(start1)
                    break
            else:
                continue
    return mappingPath[-1]

def main():
    file = open('input.txt', 'r')
    line = file.readline()

    gardenDic = {}
    seeds = line.replace('\n', '').split(': ')[1].split(' ')
    line = file.readline()
    while(line):
        if (line != '\n' and ':' in line):
            lineKey = line.replace('\n', '')
            processLine = file.readline()
            while(processLine and processLine != '\n'):
                if (not gardenDic.get(lineKey)):
                    gardenDic[lineKey] = [processLine.replace('\n', '').split(' ')]
                else:
                    gardenDic[lineKey] = list(gardenDic.get(lineKey)) + [(processLine.replace('\n', '').split(' '))]
                processLine = file.readline()

        line = file.readline()

    locationNumbers = []
    for seed in seeds:
        locationNumbers.append(getSoilLocationNumber(seed, gardenDic))
    
    print(locationNumbers)
    
    file.close()

main()