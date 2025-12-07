theRepeats = 0
theTotal = 0

def isRepeat(theVal):
  theStr = str(theVal)
  wholeSize = len(theStr)
  for segSize in range(1, (wholeSize//2)+1): # no point going past half way
    bFound = True
    if wholeSize % segSize == 0: # if the ID can be split into even segments
      for j in range(1,(wholeSize//segSize)):
        if theStr[0:segSize] != theStr[j*segSize:((j*segSize)+segSize)]:
          bFound = False
          break
      if bFound:
        return True
  return False

def addRepeats(theRange):
  global theRepeats, theTotal

  bounds = theRange.split('-')
  for i in range(int(bounds[0]), int(bounds[1])+1):
    if isRepeat(i):
      theRepeats += 1
      theTotal += i

if __name__ == '__main__':
  #with open('2tst.txt', 'r') as file:
  with open('2.txt', 'r') as file:
    theRanges = file.readline().split(',')
    for theRange in theRanges:
      addRepeats(theRange)
    
    print(theTotal)