numZeroes = 0

def adjustLock(startingLoc, instruction):
  global numZeroes
  direction = instruction[:1]
  numSteps = int( instruction[1:] )
  if direction == 'L':
    newLoc = startingLoc - numSteps
  else:
    newLoc = startingLoc + numSteps

  if newLoc <= 0:
    numZeroes += (abs(newLoc) // 100) + 1
    if startingLoc == 0:
      numZeroes -= 1 # Don't want to double-count these
  if newLoc >= 100:
    numZeroes += newLoc // 100
  newLoc = newLoc % 100
  #print(f'{numZeroes}-{newLoc}')

  return newLoc

if __name__ == '__main__':
  #with open('1tst.txt', 'r') as file:
  with open('1.txt', 'r') as file:
    lines = file.readlines()

    loc = 50
    for line in lines:
      loc = adjustLock(loc, line)
      #print(loc)
    
    print(numZeroes)