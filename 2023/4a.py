import re

def removeBlanks(theList):
  while '' in theList:
    theList.remove('')
  return theList

def assessCard(winningNums, numsOnCard):
  # Format is space-separated (i.e. '1 2 33 47')
  listWins = winningNums.split(' ')
  listWins = removeBlanks(listWins)
  listCard = numsOnCard.split(' ')
  listCard = removeBlanks(listCard)
  cntWinningNums = 0
  for num in listCard:
    if num in listWins:
      cntWinningNums += 1

  return cntWinningNums

def processCards(lines):
  totPoints = 0
  for card in lines:
    parsedCard = re.fullmatch(r'(.*):(.*)\|(.*)', card.strip())
    cardWinningNums = assessCard(parsedCard.group(2).strip(),  parsedCard.group(3).strip())
    if cardWinningNums >= 1:
      totPoints += 2 ** (cardWinningNums-1) # 1 win = 1, 2 wins = 2, 3 wins = 4, 4 wins = 8, etc.

  print(totPoints)


if __name__ == '__main__':
  #with open('4a.txt', 'r') as file:
  with open('4.txt', 'r') as file:
    lines = file.readlines()
    processCards(lines)
