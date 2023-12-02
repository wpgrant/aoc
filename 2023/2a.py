import re

def getPossibleGames(games, totRed, totGreen, totBlue):
  totGameIDs = 0
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
  
    if maxRed <= totRed and maxGreen <= totGreen and maxBlue <= totBlue:
      # Possible Game
      totGameIDs += int(gameId)

  return totGameIDs

if __name__ == '__main__':
  #with open('2a.txt', 'r') as file:
  with open('2.txt', 'r') as file:
    lines = file.readlines()
    possibleGamesCount = getPossibleGames(lines, 12, 13, 14)
    print(possibleGamesCount)