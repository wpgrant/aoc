from enum import Enum

Direction = Enum('Direction', ['Top', 'Bottom', 'Left', 'Right'])
colCount = 0
rowCount = 0
visibleTrees = []

def checkSight(theArray, direction):
  if ( (direction == Direction.Left) or (direction == Direction.Right) ):
    if (direction == Direction.Left):
      startCol = 0
      endCol = colCount
      stepCol = 1
    else:
      startCol = colCount - 1
      endCol = -1
      stepCol = -1

    for row in range(0, rowCount):
      maxVal = 0
      for col in range(startCol, endCol, stepCol):
        if ( (row == 0) or (row == rowCount - 1) or \
          (col == 0) or (col == colCount - 1) ):
          visibleTrees.append(f'{row}-{col}')
          maxVal = int(theArray[row][col])
        else:
          if ( int(theArray[row][col]) > maxVal ):
            visibleTrees.append(f'{row}-{col}')
            maxVal = int(theArray[row][col])
  else:
    if ( (direction == Direction.Top) or (direction == Direction.Bottom) ):
      if (direction == Direction.Top):
        startRow = 0
        endRow = rowCount
        stepRow = 1
      else:
        startRow = rowCount - 1
        endRow = -1
        stepRow = -1

      for col in range(0, colCount):
        maxVal = 0
        for row in range(startRow, endRow, stepRow):
          if ( (row == 0) or (row == rowCount - 1) or \
            (col == 0) or (col == colCount - 1) ):
            visibleTrees.append(f'{row}-{col}')
            maxVal = int(theArray[row][col])
          else:
            if ( int(theArray[row][col]) > maxVal ):
              visibleTrees.append(f'{row}-{col}')
              maxVal = int(theArray[row][col])


if __name__ == '__main__':
  with open('8.txt', 'r') as file:
    lines = file.readlines()

    colCount = len(lines[0].strip())
    rowCount = len(lines)

    theArray = [[0 for i in range(colCount)] for j in range(rowCount)]

    # Fill the array
    row = 0
    for treeLine in lines:
      col = 0
      for tree in treeLine.strip():
        theArray[row][col] = tree
        col += 1
      row += 1

    # Check all the directions
    checkSight(theArray, Direction.Top)
    checkSight(theArray, Direction.Bottom)
    checkSight(theArray, Direction.Left)
    checkSight(theArray, Direction.Right)

    # Remove the duplicates
    noDupes = [*set(visibleTrees)]
    # Sort the list
    noDupes.sort()

    # Print the results
    # print( noDupes )
    print( len(noDupes) )