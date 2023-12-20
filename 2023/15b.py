import re

boxes = {}

def calcFocusingPower():
  totPower = 0
  for boxNum in range(0,257):
    lensNum = 1
    for lens in boxes[boxNum].values():
      totPower += (boxNum+1) * lensNum * int(lens)
      lensNum += 1
  return totPower

def runHash(lens):
  cv = 0
  for char in lens:
    val = ord(char)
    cv += val
    cv = cv * 17
    cv = cv % 256
  return cv

def updateBoxes(lens, boxNum, opChar, focalLength):
  if opChar == '-':
    # Remove if found
    if lens in boxes[boxNum]:
      del boxes[boxNum][lens]
  elif opChar == '=':
    if lens in boxes[boxNum]:
      boxes[boxNum][lens] = focalLength
    else:
      boxes[boxNum][lens] = focalLength
  else:
    # Shouldn't happen
    print('ERROR: Invalid char')
    exit(1)


def processStep(step):
  matches = re.match(r'(.*)([=-])(\d)?', step)
  lens = matches.group(1)
  boxNum = runHash(lens)  
  opChar = matches.group(2)
  focalLength = None
  if opChar == '=':
    focalLength = matches.group(3)
  updateBoxes(lens, boxNum, opChar, focalLength)

def initializeBoxes():
  for i in range(0,257):
    boxes[i] = {}

if __name__ == '__main__':
  initializeBoxes()
  #with open('15b.txt', 'r') as file:
  with open('15.txt', 'r') as file:
    lines = file.readlines()
    totValue = 0
    for line in lines:
      steps = line.split(',')
      for step in steps:
        if len(step.strip()) > 0:
          processStep(step.strip())
  
  totalFocus = calcFocusingPower()
  print(totalFocus)