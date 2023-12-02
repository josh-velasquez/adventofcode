
def isCubeValid(sets):
  threshold = {
    'red': 12,
    'green': 13,
    'blue': 14
  }
  
  isValid = True
  for i in sets:
    for j in i.split(', '):
      num, colour = j.replace('\n', '').split(' ')
      if (int(num) > threshold.get(colour)):
        isValid = False
  return isValid

def main():
  file = open('input1.txt', 'r')
  line = file.readline()
  totalNumGames = 0
  game = 1
  while(line):
    # process the game
    sets = line.split(': ')[1].split('; ')
    if (isCubeValid(sets)):
      totalNumGames += game
    game += 1
    line = file.readline()
    
  print(totalNumGames)
  
main()