


def getBestHoldTimes(time, dist):
    # i is speed here
    bestTimes = []
    for i in range(1, time):
        distWithTime = int(i * (time - i))
        if (distWithTime > dist):
            bestTimes.append(i)
    # print(bestTimes)
    return len(bestTimes)

def main():
    file = open('input.txt', 'r')
    line = file.readline()
    
    # read time
    tempTime = line.replace('\n','').split(': ')[1].split(" ")
    times = list(filter(None, tempTime))
    line = file.readline()
    # read distance
    tempDist = line.replace('\n','').split(': ')[1].split(" ")
    dists = list(filter(None, tempDist))
    
    holdTimes = []
    for i in range(len(times)):
        holdTimes.append(getBestHoldTimes(int(times[i]), int(dists[i])))
        
    total = 1
    for i in holdTimes:
        total *= i
    print(total)
        
    
main()