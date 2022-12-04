import sys

objects = {
  "A": "Rock",
  "B" : "Paper",
  "C" : "Scissors"
}

strategies = {
  "X": "Lose",
  "Y": "Tie",
  "Z": "Win"
}

pointsForObject = {
  "Rock": 1,
  "Paper" : 2,
  "Scissors": 3
}

pointsForStrategy = {
  "Win": 6,
  "Tie": 3,
  "Lose": 0
}

playToWin = {
  "Rock": "Paper",
  "Paper": "Scissors",
  "Scissors": "Rock"
}

playToLose = {
  "Rock": "Scissors",
  "Paper": "Rock",
  "Scissors": "Paper"
}

def calculateScore(strategy):
  opponentPlay = objects[strategy[0:1]]
  myStrategy = strategies[strategy[2:3]]
  
  if (myStrategy == "Win"):
    myPlay = playToWin[opponentPlay]
  elif (myStrategy == "Lose"):
    myPlay = playToLose[opponentPlay]
  elif (myStrategy == "Tie"):
    myPlay = opponentPlay
  else:
    print(f"BAD INPUT: {opponentPlay}")

  score = pointsForObject[myPlay] + pointsForStrategy[myStrategy]
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