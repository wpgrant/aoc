def sumColumns(rockColumns):
  sumColumns = 0
  for iCol in range(0, len(rockColumns)):
    sumColumn = 0
    rowValue = len(rockColumns[iCol])
    for pos in range (0, len(rockColumns[iCol])):
      if rockColumns[iCol][pos] == 'O':
        sumColumn += rowValue
      rowValue -= 1
    sumColumns += sumColumn

  return sumColumns

def adjustRocksUp(rockColumns):
  for iCol in range(0, len(rockColumns)):
    cntSpaces = 0
    for pos in range (0, len(rockColumns[iCol])):
      if rockColumns[iCol][pos] == '.':
        cntSpaces += 1
      elif rockColumns[iCol][pos] == 'O' and cntSpaces > 0:
        rockColumns[iCol][pos-cntSpaces] = 'O'
        rockColumns[iCol][pos] = '.'        
      elif rockColumns[iCol][pos] == '#':
        cntSpaces = 0

  return rockColumns 

def getRockColumns(lines):
  rockColumns = {}
  numColumns = len(lines[0].strip())
  numRows = len(lines)
  # Initialize columns with lists
  for col in range(0,numColumns):
    rockColumns[col] = []
  
  # Now add the rocks
  for col in range(0,numColumns):
    for row in range(0,numRows):
      rockColumns[col].append(lines[row][col])
  
  return rockColumns

def sumRocks(lines):
  rockColumns = getRockColumns(lines)
  rockColumnsAdjusted = adjustRocksUp(rockColumns)
  sumRocks = sumColumns(rockColumnsAdjusted)
  print(sumRocks)

if __name__ == '__main__':
  #with open('14a.txt', 'r') as file:
  with open('14.txt', 'r') as file:
    lines = file.readlines()
    sum = sumRocks(lines)