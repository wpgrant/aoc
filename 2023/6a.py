import re

def getRaceSuccesses(time, distance):
  cntSuccesses = 0
  for i in range(1, time-1):
    result = i * (time-i)
    if result > distance: cntSuccesses += 1
  return cntSuccesses

def processRaces(arrTimes, arrDistances):
  arrRaces = []
  for i in range(0,len(arrTimes)):
    raceSuccesses = getRaceSuccesses(int(arrTimes[i]), int(arrDistances[i]))
    arrRaces.append(raceSuccesses)

  total = 1
  for race in arrRaces:
    total *= race

  print(total)
  
if __name__ == '__main__':
  #with open('6a.txt', 'r') as file:
  with open('6.txt', 'r') as file:
    lines = file.readlines()
    strTimes = re.match(r'[^\d]*(.*)', lines[0].strip()).group(1)
    strDistances = re.match(r'[^\d]*(.*)', lines[1].strip()).group(1)
    arrTimes = list(filter(''.__ne__, strTimes.split(' ')))
    arrDistances = list(filter(''.__ne__, strDistances.split(' ')))
    processRaces(arrTimes, arrDistances)
