import re

def getHandStrength(hand: str):
  # For strength we will simply convert each hand to base 16, since
  # hands are evaluated by card location (not simply highest to lowest)
  strHex = hand.replace('T','a').replace('J', 'b').replace('Q','c').replace('K','d') \
    .replace('A','e')
  return int(f'0x{strHex}', 16)

def getHandRank(hand):
  dCardCounts = {}
  threeOfAKind = 0
  pairs = 0
  for char in hand:
    if char in dCardCounts:
      dCardCounts[char] += 1
    else:
      dCardCounts[char] = 1

  for count in dCardCounts:
    if dCardCounts[count] == 5:
      return 1
    elif dCardCounts[count] == 4:
      return 2
    elif dCardCounts[count] == 3:
      threeOfAKind += 1
    elif dCardCounts[count] == 2:
      pairs += 1
  
  if threeOfAKind == 1 and pairs == 1:
    return 3
  elif threeOfAKind == 1:
    return 4
  elif pairs == 2:
    return 5
  elif pairs == 1:
    return 6
  else: return 7

def processHandAndBid(hand, bid):
  # Let's define a hand as a tuple of: hand rank, hand strength, bid
  # hand rank:
  # 1 - Five of a kind
  # 2 - Four of a kind
  # 3 - Full house
  # 4 - Three of a kind
  # 5 - Two pair
  # 6 - One pair
  # 7 - High card
  # hand strength - Based on the algorithm we can simply change the hand
  #                 to hex and reverse sort it
  rank = getHandRank(hand)
  strength = getHandStrength(hand)
  bid = int(bid)
  return [rank, strength, bid]


def processLines(lines):
  hands = []
  for line in lines:
    handAndBid = re.match(r'(.*) (.*)', line.strip())
    hand = handAndBid.group(1)
    bid = handAndBid.group(2)
    hands.append(processHandAndBid(hand, bid))
  
  # sorting = hand rank and strength; worst first
  # for ranks that is reverse order (7, high card worst)
  # for strengths that is forward order (low number is worst)
  sortedHands = sorted(hands, key = lambda x: (-x[0], x[1]))
  totWinnings = 0
  for i in range(0,len(sortedHands)):
    # winnings = bid * rank
    totWinnings += sortedHands[i][2] * (i+1)

  print(totWinnings)

if __name__ == '__main__':
  #with open('7a.txt', 'r') as file:
  with open('7.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
  