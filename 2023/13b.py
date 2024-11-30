def findColumn(puzzle):
  numCols = len(puzzle[0])
  for iCol in range(0, numCols-1):
    # Maybe it would be smarter to start on each side and work
    # our way in, but we will just go left-to-right for simplicity
    
    # Establish the ranges
    startLeft = iCol
    startRight = iCol + 1
    matchGood = False
    matchRepaired = False
    if startRight > numCols / 2:
      sizeOfCols = numCols - startRight
    else:
      sizeOfCols = startRight
    for eRow in range(0, len(puzzle)):
      for eCol in range(0, sizeOfCols):
        if puzzle[eRow][startLeft-eCol] != puzzle[eRow][startRight+eCol]:
          if matchRepaired == False:
            # Repairing now; match good
            #print(f'{iCol}-{eCol}')
            #print(puzzle[eRow])
            puzzle[eRow] = puzzle[eRow][0:startLeft-eCol] + puzzle[eRow][startRight+eCol] + puzzle[eRow][startLeft-eCol+1:]
            #print(puzzle[eRow])
            matchRepaired = True
            matchGood = True
          else:
            # Already been repaied; no good
            matchGood = False
            break
      else:
        continue
      break

    if matchGood:
      return iCol

  return -1

def findRow(puzzle):
  numRows = len(puzzle)
  for iRow in range(0, numRows-1):
    # Establish the ranges
    startTop = iRow
    startBelow = iRow + 1
    matchGood = False
    matchRepaired = False
    if startBelow > numRows / 2:
      sizeOfRows = numRows - startBelow
    else:
      sizeOfRows = startBelow
    for eCol in range(0, len(puzzle[0])):
      for eRow in range(0, sizeOfRows):
        if puzzle[startTop-eRow][eCol] != puzzle[startBelow+eRow][eCol]:
          if matchRepaired == False:
            # Repairing now; match good
            puzzle[startTop-eRow] = puzzle[startTop-eRow][0:eCol] + puzzle[startBelow+eRow][eCol] + puzzle[startTop-eRow][eCol+1:] 
            #print(puzzle[startTop-eRow])
            #print(puzzle[startBelow+eRow])
            #print(f'here-{iRow}')
            matchRepaired = True
            matchGood = True
          else:
            # Already been repaied; no good
            #print(f'no good anymore-{iRow}')
            matchGood = False
            break
      else:
        continue
      break

    if matchGood:
      return iRow

  return -1

def processPuzzle(puzzle):
  totPuzzle = 0
  col = findColumn(puzzle)
  print(col)
  if col >= 0:
    totPuzzle += col + 1

  row = findRow(puzzle)
  print(row)
  if row >= 0:
    totPuzzle += 100 * (row + 1)

  return totPuzzle

if __name__ == '__main__':
  x = 'hello'
  print(x[0:0])

  totPuzzles = 0
  with open('13b.txt', 'r') as file:
  #with open('13.txt', 'r') as file:
    lines = file.readlines()
    i = 0
    puzzle = []
    while i < len(lines):
      if lines[i].strip() == '':
        totPuzzles += processPuzzle(puzzle)
        puzzle = []
      else:
        puzzle.append(lines[i].strip())
      i += 1
    # Process the last one
    totPuzzles += processPuzzle(puzzle)
    print(totPuzzles)