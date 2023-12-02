
## Part One
# def findFirstAndLastNum(line):
# 	num = ''
# 	for i in line:
# 		if (i.isnumeric()):
# 			num += i
# 			break
# 	for i in line[::-1]:
# 		if (i.isnumeric()):
# 			num += i
# 			break
# 	return int(num)

# def main():
# 	file = open('input.txt', 'r')
# 	line = file.readline()
# 	totalSum = 0
# 	while(line):
# 		totalSum += findFirstAndLastNum(line)
# 		line = file.readline()

# 	print(totalSum)


# main()

## Part two
numDic = {
'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}
def findFirstAndSecondNum(line, reversedArr = False):
	for i in range(0, len(line) - 1):
		if (line[i].isnumeric()):
			return line[i]
		else:
			tempNum = line[i]
			for j in range(i + 1, len(line) - 1):
				tempNum += line[j]
				if (reversedArr):
					if (tempNum[::-1] in numDic):
						return numDic.get(tempNum[::-1])
				elif tempNum in numDic:
					return numDic.get(tempNum)

def findFirstAndLastNum(line):
	first = findFirstAndSecondNum(line)
	second = findFirstAndSecondNum(line[::-1], True)
	if (second == None):
		second = first
	return int(str(first) + str(second))
						
	
def main():
    file = open('input2.txt', 'r')
    line = file.readline()
    totalSum = 0
    while(line):
        totalSum += findFirstAndLastNum(line)
        line = file.readline()
    print(totalSum)
    
main()