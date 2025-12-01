def adjustLock(startingLoc, instruction):
  direction = instruction[:1]
  numSteps = int( instruction[1:] )
  if direction == 'L':
    newLoc = startingLoc - numSteps
  else:
    newLoc = startingLoc + numSteps  
  if newLoc < 0 or newLoc >= 100:
      newLoc = newLoc % 100
  return newLoc

if __name__ == '__main__':
  #with open('1a.txt', 'r') as file:
  #with open('1tst.txt', 'r') as file:
  with open('1.txt', 'r') as file:
    lines = file.readlines()

    loc = 50
    numZeroes = 0
    for line in lines:
      loc = adjustLock(loc, line)
      #print(loc)
      if loc == 0:
        numZeroes += 1
    
    print(numZeroes)