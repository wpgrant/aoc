import re

class card:
  def __init__(self, cardNum, numWins):
    self.cardNum = cardNum
    self.numWins = numWins
    self.cardCount = 1

  def __repr__(self):
    return f"Card {self.cardNum}: {str(self.numWins)} wins, {str(self.cardCount)} cards"

  def addCards(self, num):
    self.cardCount += num
  
def removeBlanks(theList):
  while '' in theList:
    theList.remove('')
  return theList

def processCardInitial(cardNum, winningNums, numsOnCard):
  # Format for nums is space-separated (i.e. '1 2 33 47')
  listWins = winningNums.split(' ')
  listWins = removeBlanks(listWins)
  listCard = numsOnCard.split(' ')
  listCard = removeBlanks(listCard)

  numWins = 0
  for num in listCard:
    if num in listWins:
      numWins += 1

  theCard = card(cardNum, numWins)
  return theCard

def processCards(lines):
  cards = {}
  # First, go through the cards and capture the wins
  for line in lines:
    parsedCard = re.match(r'Card (.*):(.*)\|(.*)', line.strip())
    theCard = processCardInitial(parsedCard.group(1).strip(), parsedCard.group(2).strip(),  parsedCard.group(3).strip())
    cards[theCard.cardNum] = theCard

  # Then, go back through the cards and add all of the additional cards
  totCards = len(cards)
  for cardNum in cards:
    theCard = cards[cardNum]
    for i in range(int(theCard.cardNum) + 1, int(theCard.cardNum) + 1 + int(theCard.numWins)):
      if i <= totCards:
        cards[str(i)].addCards(theCard.cardCount)

  # Finally, count all the cards
  totCardCount = 0
  for cardNum in cards:
    totCardCount += cards[cardNum].cardCount

  print(totCardCount)

  #print(cardCount)


if __name__ == '__main__':
  #with open('4b.txt', 'r') as file:
  with open('4.txt', 'r') as file:
    lines = file.readlines()
    processCards(lines)
