def getGalaxies(map):
  galaxies = []
  for row in range(0, len(map)):
    for col in range(0, len(map[0])):
      if map[row][col] == "#":
        galaxies.append([row, col])
  return galaxies

def makeExpandedMap(map, emptyRows, emptyCols):
  # First make an empty row to use
  emptyRow = []
  lenExpandedMap = len(map[0]) + len(emptyCols)
  for col in range(0, lenExpandedMap):
    emptyRow.append('.')

  expandedMap = []
  eRow = 0
  for row in range(0, len(map)):
    eCol = 0
    expandedRow = []
    for col in range(0, len(map[0])):
      expandedRow.append(map[row][col])
      if col in emptyCols:
        eCol += 1
        expandedRow.append(map[row][col])
    expandedMap.append(expandedRow)
    if row in emptyRows:
      eRow += 1
      expandedMap.append(emptyRow)
  
  return expandedMap

def getEmptyCols(map):
  lstCols = {}
  # find empty cols
  for col in range(0, len(map[0])):
    aCols = []
    for row in map:
      aCols.append(row[col])
    if '#' in aCols:
      #Not empty, continue
      continue
    else:
      lstCols[col] = 'Y'
  return lstCols

def getEmptyRows(map):
  lstRows = {}
  # find empty rows
  for rowNum in range(0, len(map)):
    if '#' in map[rowNum]:
      # Not empty, continue
      continue
    else:
      lstRows[rowNum] = 'Y' # Doesn't matter what we put here
  return lstRows

def createMap(lines):
  map = []
  for line in lines:
    row = []
    for char in line.strip():
      row.append(char)
    map.append(row)
  return map

def sumShorterstPaths(galaxies):
  sumPaths = 0
  # We will not worry about the distance between the same galaxy
  # since the distance is 0
  for galaxy1 in galaxies:
    for galaxy2 in galaxies:
      dist = abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1])
      sumPaths += dist
  
  # We need to cut it in half because we double-counted paths
  return int(sumPaths / 2)

if __name__ == '__main__':
  #with open('11a.txt', 'r') as file:
  with open('11.txt', 'r') as file:
    lines = file.readlines()
    map = createMap(lines)
    emptyRows = getEmptyRows(map)
    emptyCols = getEmptyCols(map)
    expandedMap = makeExpandedMap(map, emptyRows, emptyCols)
    galaxies = getGalaxies(expandedMap)
    theSum = sumShorterstPaths(galaxies)
    print(theSum)
