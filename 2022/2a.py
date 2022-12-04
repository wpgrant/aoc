import sys

ROCK = 1
PAPER = 2
SCISSORS = 3
WIN_POINTS = 6
TIE_POINTS = 3
LOSS_POINTS = 0

def getObject(letter):
  if (letter == 'A' or letter == 'X'):
    return ROCK
  elif (letter == 'B' or letter == 'Y'):
    return PAPER
  elif (letter == 'C' or letter == 'Z'):
    return SCISSORS
  else:
    print(f"BAD INPUT: {letter}")   

def calculateScore(strategy):
  score = 0
  opponentPlay = getObject(strategy[0:1])
  myPlay = getObject(strategy[2:3])
  score += myPlay
  if (opponentPlay == myPlay):
    score += TIE_POINTS
  elif ( (opponentPlay == 1 and myPlay == 2) or (opponentPlay == 2 and myPlay == 3) or (opponentPlay == 3 and myPlay == 1) ):
    score += WIN_POINTS
  else:
    score += LOSS_POINTS

  return score


if __name__ == '__main__':
  with open('2.txt', 'r') as file:
    lines = file.readlines()

  totalScore = 0
  for strategy in lines:
    if len(strategy.strip()) == 3:
      score = calculateScore(strategy.strip())
      totalScore += score

  print(totalScore)