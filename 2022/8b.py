treeArray = []

colCount = 0
rowCount = 0
maxTrees = 0
maxTreePos = ""

def countTreesAcross(treeHeight, row, startCol, endCol, stepCol):
  cnt = 0
  for col in range(startCol, endCol, stepCol):
    if ( int(treeArray[row][col]) < treeHeight ):
      cnt += 1
    else:
      # Tree is same height or taller
      cnt += 1
      break

  return cnt

def countTreesUpDown(treeHeight, col, startRow, endRow, stepRow):
  cnt = 0
  for row in range(startRow, endRow, stepRow):
    if ( int(treeArray[row][col]) < treeHeight ):
      cnt += 1
    else:
      # Tree is same height or taller
      cnt += 1
      break

  return cnt

def countTrees(row, col):
  treeHeight = int(treeArray[row][col])
  # Left
  cntLeft = countTreesAcross(treeHeight, row, col-1, -1, -1)
  # Right
  cntRight = countTreesAcross(treeHeight, row, col+1, colCount, 1)
  # Up
  cntUp = countTreesUpDown(treeHeight, col, row-1, -1, -1)
  # Down
  cntDown = countTreesUpDown(treeHeight, col, row+1, rowCount, 1)

  # Calculate the score
  score = cntLeft * cntRight * cntUp * cntDown

  return score

if __name__ == '__main__':
  with open('8.txt', 'r') as file:
    lines = file.readlines()

    colCount = len(lines[0].strip())
    rowCount = len(lines)

    treeArray = [[0 for i in range(colCount)] for j in range(rowCount)]

    # Fill the array
    row = 0
    for treeLine in lines:
      col = 0
      for tree in treeLine.strip():
        treeArray[row][col] = tree
        col += 1
      row += 1

    cnt = 0
    for row in range(0, rowCount):
      for col in range(0, colCount):
        thisTree = countTrees(row, col)
        if (thisTree > maxTrees):
          maxTrees = thisTree
          maxTreePos = f"{row}-{col}"

    print(f'Max Score: {maxTrees} - Position: {maxTreePos}')