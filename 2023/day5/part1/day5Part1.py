
# guaranteed to one mapping that exists
def getSoilLocationNumber(seed, gardenDic):
    # loop over the dictionary and map out the seed
    mappingPath = []
    intSeed = int(seed)
    mappingPath.append(intSeed)
    for key, values in gardenDic.items():
        for value in values:
            start1, start2, rangeVal = value
            if (intSeed in range(int(start2), int(start2) + int(rangeVal))):
                # check if seed is in the second mapping
                mappingIndex = intSeed - int(start2)
                if (mappingIndex != 0):
                    mappedVal = int(start1) + mappingIndex
                    mappingPath.append(mappedVal)
                    intSeed = mappedVal
                    break
                else:
                    mappingPath.append(int(start1))
                    intSeed = int(start1)
                    break
            else:
                if (values.index(value) == len(values) - 1):
                    mappingPath.append(int(mappingPath[-1]))
                    intSeed = int(mappingPath[-1])
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
    print(min(locationNumbers))
    
    file.close()

main()