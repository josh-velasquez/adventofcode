

def getHighestValPower(sets):
	red = 0
	green = 0
	blue = 0
	for set in sets:
		for val in set.split(', '):
			num, colour = val.split(' ')
			intNum = int(num)
			if (colour == 'red' and intNum > red):
				red = intNum
			elif (colour == 'green' and intNum > green):
				green = intNum
			elif (colour == 'blue' and intNum > blue):
				blue = intNum
	return red * green * blue

def main():
  file = open('input2.txt', 'r')
  line = file.readline()
  totalSum = 0
  while(line):
    # process the game
    sets = line.replace('\n', '').split(': ')[1].split('; ')
    totalSum += getHighestValPower(sets)

    line = file.readline()
    
  print(totalSum)
  
main()