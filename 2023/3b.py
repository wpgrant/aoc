import re

class gear:
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.parts = []

  def __repr__(self):
    return f"Count {len(self.parts)} - Coords ({self.posX}:{self.posY})"
  
  def set_count(self, value):
    self.count = value

  def addParts(self, partNum):
    self.parts.append(partNum)

def addPotentialGears(lines):
  potentialGears = []
  iRow = 0
  for line in lines:
    for reGear in re.finditer(r'\*', line.strip()):
      potentialGears.append(gear(iRow, reGear.start()))
    iRow += 1
  return potentialGears

def addGearParts(lines, potentialGears):
  row = 0
  for line in lines:
    for part in re.finditer(r'\d+', line.strip()):
      colStart = part.start()
      colEnd = part.start() + len(part.group()) - 1
      for gear in potentialGears:
        if (gear.posX == row - 1 or gear.posX == row + 1) and (\
          (gear.posY - 1 <= colEnd and gear.posY - 1 >= colStart) or \
          (gear.posY + 1 >= colStart and gear.posY + 1 <= colEnd) or \
          (gear.posY >= colStart and gear.posY <= colEnd) ):
          # Row above or below
          gear.addParts(part.group())
        elif gear.posX == row and gear.posY - 1 == colEnd:
          # Same row (to the left)
          gear.addParts(part.group())
        elif gear.posX == row and gear.posY + 1 == colStart:
          # Same row (to the right)
          gear.addParts(part.group())
    row += 1
  return potentialGears

def totalGears(potentialGears):
  tot = 0
  for iGear in potentialGears:
    if len(iGear.parts) == 2:
      gearTot = int(iGear.parts[0]) * int(iGear.parts[1])
      tot += gearTot
  return tot


def processLines(lines):
  potentialGears = addPotentialGears(lines)
  potentialGears = addGearParts(lines, potentialGears)
  total = totalGears(potentialGears)
  print(total)

if __name__ == '__main__':
  #with open('3c.txt', 'r') as file:
  #with open('3b.txt', 'r') as file:
  with open('3.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
