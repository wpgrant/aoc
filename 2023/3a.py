import re

class potentialPart:
  def __init__(self, num, posX, posY, length):
    self.num = num
    self.posX = posX
    self.posY = posY
    self.length = length
  
  def __repr__(self):
    return f"PotentialPart: {self.num} - ({self.posX}:{self.posY}) - len-{self.length}"

def addPartsAndSymbols(lines):
  iRow = 0
  for line in lines:
    for num in re.finditer(r'\d+', line.strip()):
      potentialParts.append( \
        potentialPart(num.group(), \
        num.start(), iRow, num.end() - num.start() \
        ))
    for sym in re.finditer(r'[^0-9\.]', line.strip()):
      col = "{:04d}".format(sym.start())
      row = "{:04d}".format(iRow)
      symbols[f"{col}:{row}"] = sym.group()

    iRow += 1

def checkRow(potPart, row, colStart, colEnd):
  for col in range(colStart, colEnd):
    coordsCol = "{:04d}".format(col)
    coordsRow = "{:04d}".format(row)
    if f"{coordsCol}:{coordsRow}" in symbols:
      return True
    
  return False

def findParts():
  for potPart in potentialParts:
    # Check all positions surrounding the potential part, including diagonals
    # Row above, check all spaces above plus previous column and next column
    row = potPart.posY - 1
    colStart = potPart.posX - 1
    colEnd = potPart.posX + potPart.length + 1
    result = checkRow( potPart, row, colStart, colEnd )
    if result:
      parts.append(potPart)
    else:
      # Check before and after
      row = potPart.posY
      colStart = potPart.posX - 1
      colEnd = potPart.posX
      resultBefore = checkRow( potPart, row, colStart, colEnd )
      colStart = potPart.posX + potPart.length
      colEnd = colStart + 1
      resultAfter = checkRow( potPart, row, colStart, colEnd )
      if resultBefore or resultAfter:
        parts.append(potPart)
      else:
        # Check next row
        row = potPart.posY + 1
        colStart = potPart.posX - 1
        colEnd = potPart.posX + potPart.length + 1
        result = checkRow( potPart, row, colStart, colEnd )
        if result:
          parts.append(potPart)

def processLines(lines):
  global potentialParts
  global symbols
  global parts
  potentialParts = []
  symbols = {}
  parts = []
  addPartsAndSymbols(lines)
  findParts()

  sumPartNumbers = 0
  for part in parts:
    sumPartNumbers += int(part.num)

  print(sumPartNumbers)

if __name__ == '__main__':
  #with open('3a.txt', 'r') as file:
  with open('3.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
