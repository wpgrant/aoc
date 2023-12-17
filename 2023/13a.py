def findColumn(puzzle):
  numCols = len(puzzle[0])
  for iCol in range(0, numCols-1):
    # Maybe it would be smarter to start on each side and work
    # our way in, but we will just go left-to-right for simplicity
    
    # Establish the ranges
    startLeft = iCol
    startRight = iCol + 1
    matchGood = True
    if startRight > numCols / 2:
      sizeOfCols = numCols - startRight
    else:
      sizeOfCols = startRight
    for eRow in range(0, len(puzzle)):
      for eCol in range(0, sizeOfCols):
        if puzzle[eRow][startLeft-eCol] != puzzle[eRow][startRight+eCol]:
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
    matchGood = True
    if startBelow > numRows / 2:
      sizeOfRows = numRows - startBelow
    else:
      sizeOfRows = startBelow
    for eCol in range(0, len(puzzle[0])):
      for eRow in range(0, sizeOfRows):
        if puzzle[startTop-eRow][eCol] != puzzle[startBelow+eRow][eCol]:
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
  if col >= 0:
    totPuzzle += col + 1

  row = findRow(puzzle)
  if row >= 0:
    totPuzzle += 100 * (row + 1)

  return totPuzzle

if __name__ == '__main__':
  totPuzzles = 0
  #with open('13a.txt', 'r') as file:
  with open('13.txt', 'r') as file:
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