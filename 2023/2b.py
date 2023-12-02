import re

def getMinimumSets(games):
  totGamePower = 0
  for line in lines:
    parsedGame = re.match('Game (\\d+):(.*)', line.strip())
    gameId = parsedGame.group(1)
    draws = parsedGame.group(2).split(';')
    maxRed=0; maxGreen=0; maxBlue=0
    for draw in draws:
      marbles = draw.split(',')
      for marble in marbles:
        parsedMarble = re.match('(\\d+)\\s(.*)', marble.strip())
        marbleQty = int(parsedMarble.group(1))
        marbleColor = parsedMarble.group(2)
        match marbleColor:
          case 'red':
            maxRed = marbleQty if marbleQty > maxRed else maxRed
          case 'green':
            maxGreen = marbleQty if marbleQty > maxGreen else maxGreen
          case 'blue':
            maxBlue = marbleQty if marbleQty > maxBlue else maxBlue

    gamePower = int(f"{maxRed}") * int(f"{maxGreen}") * int(f"{maxBlue}")
    totGamePower += gamePower

  return totGamePower

if __name__ == '__main__':
  #with open('2b.txt', 'r') as file:
  with open('2.txt', 'r') as file:
    lines = file.readlines()
    power = getMinimumSets(lines)
    print(power)