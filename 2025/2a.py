theRepeats = 0
theTotal = 0

def addRepeats(theRange):
  global theRepeats, theTotal

  bounds = theRange.split('-')
  for i in range(int(bounds[0]), int(bounds[1])+1):
    theStr = str(i)
    theLen = len(theStr)
    if theStr[0:(theLen//2)] == theStr[(theLen//2):]:
      theRepeats += 1
      theTotal += i

if __name__ == '__main__':
  #with open('2tst.txt', 'r') as file:
  with open('2.txt', 'r') as file:
    theRanges = file.readline().split(',')
    for theRange in theRanges:
      addRepeats(theRange)
    
    print(theTotal)