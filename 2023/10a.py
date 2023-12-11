NORTH = 0x1000
SOUTH = 0x0100
EAST = 0x0010
WEST = 0x0001

def getPossibleMoves(char):
  if char == '|': return [ NORTH, SOUTH ]
  elif char == '-': return [ EAST, WEST ]
  elif char == 'L': return [ NORTH, EAST ]
  elif char == 'J': return [ NORTH, WEST ]
  elif char == '7': return [ SOUTH, WEST ]
  elif char == 'F': return [ SOUTH, EAST ]
  else:
    print(f"Illegal Space: {char}")
    exit(1)

def getMoveCount(map, firstMove):
  # firstMove has [ row, col, movedFrom, cnt ]
  row = firstMove[0]
  col = firstMove[1]
  movedFrom = firstMove[2]
  stepCount = firstMove[3]
  while map[row][col] != 'S':
    # In order to know which way we can go we need to eliminate the other direction
    moves = getPossibleMoves( map[row][col] )
    moves.remove( movedFrom )

    # Make the move by going in the remaining direction
    if moves[0] == NORTH:
      row -= 1
      movedFrom = SOUTH
    elif moves[0] == SOUTH:
      row += 1
      movedFrom = NORTH
    elif moves[0] == WEST:
      col -= 1
      movedFrom = EAST
    elif moves[0] == EAST:
      col += 1
      movedFrom = WEST
    else:
      print(f"Illegal Move: {moves[0]}")
      exit(1)
    
    stepCount += 1
  
  return stepCount

def getFirstMove(map, start):
  # The first one is weird, there are two ways to go, we will just take the first one
  row = start[0]
  col = start[1]
  # Check around it for an out; return new position (row, col), where we came from, and step count
  if map[row - 1][col] in ['|','F','7']:
    return [ row - 1, col, SOUTH, 1 ]
  elif map[row + 1][col] in ['|','L','J']:
    return [ row + 1, col, NORTH, 1 ]
  elif map[row][col - 1] in ['-','L','F']:
    return [ row, col - 1, EAST, 1 ]
  elif map[row][col + 1] in ['-','J','7']:
    return [ row, col + 1, WEST, 1 ]
  else:
    print('Problem starting out!')
    exit(1)  

def getStart(map):
  theRow = -1
  theCol = -1
  for row in range(0, len(map)):
    try:
      col = map[row].index("S")
      theRow = row
      theCol = col
      break
    except:
      pass
  
  return [ theRow, theCol ]  

def createMap(lines):
  map = []
  for line in lines:
    arrLine = []
    for char in line.strip():
      arrLine.append(char)
    map.append(arrLine)
  return map

if __name__ == '__main__':
  #with open('10a.txt', 'r') as file:
  with open('10.txt', 'r') as file:
    lines = file.readlines()
    map = createMap(lines)
    start = getStart(map)
    firstMove = getFirstMove(map, start)
    moveCount = getMoveCount(map, firstMove)
    print(int(moveCount/2))