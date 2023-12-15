def getGalaxies(map):
  galaxies = []
  for row in range(0, len(map)):
    for col in range(0, len(map[0])):
      if map[row][col] == "#":
        galaxies.append([row, col])
  return galaxies

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

def sumShorterstPaths(galaxies, emptyRows, emptyCols):
  sumPaths = 0
  sumSpaces = 0
  # We will not worry about the distance between the same galaxy
  # since the distance is 0
  for galaxy1 in galaxies:
    for galaxy2 in galaxies:
      # Calculate the distances
      dist = abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1])
      sumPaths += dist
      # Calculate the spaces
      for row in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
        if row in emptyRows:
          sumSpaces += 1
      for col in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
        if col in emptyCols:
          sumSpaces += 1
  # If the space was normally 1 it is now 1,000,000; need to subtract the original
  sum = int(((sumSpaces * 1000000) - sumSpaces + sumPaths) / 2)
  return sum

if __name__ == '__main__':
  #with open('11b.txt', 'r') as file:
  with open('11.txt', 'r') as file:
    lines = file.readlines()
    map = createMap(lines)
    emptyRows = getEmptyRows(map)
    emptyCols = getEmptyCols(map)
    galaxies = getGalaxies(map)
    theSum = sumShorterstPaths(galaxies, emptyRows, emptyCols)
    print(theSum)
