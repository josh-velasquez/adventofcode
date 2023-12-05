

def getSoilLocationNumber(seed, gardenDic):
    # loop over the dictionary and map out the seed

def main():
    file = open('sample.txt', 'r')
    line = file.readline()

    gardenDic = {}
    
    # read the seeds first

    seeds = line.replace('\n', '').split(': ')[1].split(' ')
    line = file.readline()
    while(line):
        if (line != '\n' and ':' in line):
            lineKey = line.replace('\n', '')
            processLine = file.readline()
            while(processLine and processLine != '\n'):
                gardenDic[lineKey] = processLine.replace('\n', '').split(' ')
                processLine = file.readline()

        line = file.readline()
    
    locationNumbers = []
    for seed in seeds:
        locationNumbers.append(getSoilLocationNumber(seed, gardenDic))
    
    print(min(locationNumbers))
    
    file.close()

main()