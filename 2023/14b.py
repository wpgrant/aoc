from deepdiff import DeepHash

DIR_UP = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_RIGHT = 4

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

def adjustRocks(rockColumns, direction):
  if direction == DIR_UP or direction == DIR_DOWN:
    colStart = 0
    colEnd = len(rockColumns)
    colStep = 1
    if direction == DIR_UP:
      rowStart = 0
      rowEnd = len(rockColumns[0])
      rowStep = 1    
    elif direction == DIR_DOWN:
      rowStart = len(rockColumns[0]) - 1
      rowEnd = -1
      rowStep = -1
    for iCol in range(colStart, colEnd, colStep):
      cntSpaces = 0
      for pos in range (rowStart, rowEnd, rowStep):
        if rockColumns[iCol][pos] == '.':
          cntSpaces += 1
        elif rockColumns[iCol][pos] == 'O' and cntSpaces > 0:
          if direction == DIR_UP:
            rockColumns[iCol][pos-cntSpaces] = 'O'
          else:
            rockColumns[iCol][pos+cntSpaces] = 'O'
          rockColumns[iCol][pos] = '.'        
        elif rockColumns[iCol][pos] == '#':
          cntSpaces = 0    
  else:
    rowStart = 0
    rowEnd = len(rockColumns[0])
    rowStep = 1        
    if direction == DIR_LEFT:
      colStart = 0
      colEnd = len(rockColumns)
      colStep = 1
    elif direction == DIR_RIGHT:
      colStart = len(rockColumns) - 1
      colEnd = -1
      colStep = -1
    for pos in range (rowStart, rowEnd, rowStep):
      cntSpaces = 0
      for iCol in range(colStart, colEnd, colStep):
        if rockColumns[iCol][pos] == '.':
          cntSpaces += 1
        elif rockColumns[iCol][pos] == 'O' and cntSpaces > 0:
          if direction == DIR_LEFT:
            rockColumns[iCol-cntSpaces][pos] = 'O'
          else:
            rockColumns[iCol+cntSpaces][pos] = 'O'
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
  hashList = []
  foundList = []
  rockColumns = getRockColumns(lines)
  for i in range(1,100):
    rockColumnsAdjusted = adjustRocks(rockColumns, DIR_UP)
    rockColumnsAdjusted = adjustRocks(rockColumns, DIR_LEFT)
    rockColumnsAdjusted = adjustRocks(rockColumns, DIR_DOWN)
    rockColumnsAdjusted = adjustRocks(rockColumns, DIR_RIGHT)

    theHash_o = DeepHash(rockColumnsAdjusted)
    theHash = DeepHash(theHash_o)[theHash_o]
    if theHash in hashList:
      # Found the first time
      foundList.append(theHash)
    if theHash in foundList:
      # Found the second time, we have a cycle
      print(f'cycle-{i}-{theHash}')
      print(sumColumns(rockColumnsAdjusted))
    hashList.append(theHash)

  sumRocks = sumColumns(rockColumnsAdjusted)
  print(sumRocks)

if __name__ == '__main__':
  print('Need to identify the pattern for this one...')
  exit(0)
  with open('14b.txt', 'r') as file:
  #with open('14.txt', 'r') as file:
    lines = file.readlines()
    sum = sumRocks(lines)