DIR_UP = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_RIGHT = 4

MIN_ROW = 0
MIN_COL = 0
MAX_ROW = 0
MAX_COL = 0

def nagigateNextStep(theGrid, theTiles, theBeams):
  # This method makes me cringe... Definitely should be refactored.
  # beam: 0=row, 1=col, 2=direction
  alreadyNavigated = []
  while len(theBeams) > 0:
    currBeams = theBeams
    theBeams = []
    for beam in currBeams:
      if beam not in alreadyNavigated:
        alreadyNavigated.append(beam)
        row = beam[0]
        col = beam[1]
        dir = beam[2]
        if dir == DIR_UP:
          row -= 1
        if dir == DIR_DOWN:
          row += 1
        if dir == DIR_LEFT:
          col -= 1
        if dir == DIR_RIGHT:
          col += 1
        if row >= MIN_ROW and row <= MAX_ROW and col >= MIN_COL and col <= MAX_COL:
          # Update the tiles lit up
          theTiles[row][col] = '#'
          # Determine the new direction
          if theGrid[row][col] == '/':
            if dir == DIR_UP: dir = DIR_RIGHT
            elif dir == DIR_DOWN: dir = DIR_LEFT
            elif dir == DIR_RIGHT: dir = DIR_UP
            elif dir == DIR_LEFT: dir = DIR_DOWN
            # Update the beam
            beam = [row, col, dir]
            theBeams.append(beam)
          elif theGrid[row][col] == '\\':
            if dir == DIR_UP: dir = DIR_LEFT
            elif dir == DIR_DOWN: dir = DIR_RIGHT
            elif dir == DIR_RIGHT: dir = DIR_DOWN
            elif dir == DIR_LEFT: dir = DIR_UP
            # Update the beam
            beam = [row, col, dir]
            theBeams.append(beam)
          elif theGrid[row][col] == '|':
            if dir == DIR_LEFT or dir == DIR_RIGHT:
              # Split the beams
              beam = [row, col, DIR_UP]
              theBeams.append(beam)
              newBeam = [row, col, DIR_DOWN]
              theBeams.append(newBeam)
            else:
              # Just continue the beam
              beam = [row, col, dir]
              theBeams.append(beam)
          elif theGrid[row][col] == '-':
            if dir == DIR_UP or dir == DIR_DOWN:
              # Split the beams
              beam = [row, col, DIR_LEFT]
              theBeams.append(beam)
              newBeam = [row, col, DIR_RIGHT]
              theBeams.append(newBeam)
            else:
              # Just continue the beam
              beam = [row, col, dir]
              theBeams.append(beam)
          else:
            # Just continue the beam
            beam = [row, col, dir]
            theBeams.append(beam)
      
  return theTiles

def initializeTiles(lines):
  # This is the grid of tiles
  theGrid = {}
  for row in range(0, len(lines)):
    theGrid[row] = {}
    for col in range(0, len(lines[row].strip())):
      theGrid[row][col] = '.'
  
  #theGrid[0][0] = '#'
  return theGrid

def initializeGrid(lines):
  # This is the grid of mirrors
  theGrid = {}
  for row in range(0, len(lines)):
    theGrid[row] = {}
    for col in range(0, len(lines[row].strip())):
      theGrid[row][col] = lines[row][col]
  return theGrid

if __name__ == '__main__':
  #with open('16b.txt', 'r') as file:
  with open('16.txt', 'r') as file:
    lines = file.readlines()
    MAX_ROW = len(lines) - 1
    MAX_COL = len(lines[0].strip()) - 1
    theGrid = initializeGrid(lines)
    # Each beam is a {row, col, direction}
    maxEnergized = 0
    theBeams = []
    # Add all the starting beams (just outside the grid)
    for row in range(MIN_ROW, MAX_ROW + 1):
      theBeams.append([row, MIN_COL - 1, DIR_RIGHT])
      theBeams.append([row, MAX_COL + 1, DIR_LEFT])
    for col in range(MIN_COL, MAX_COL + 1):
      theBeams.append([MIN_ROW - 1, col, DIR_DOWN])
      theBeams.append([MAX_ROW + 1, col, DIR_UP])

    beamNum = 1
    for beam in theBeams:
      theBeam = [beam]
      theTiles = initializeTiles(lines)
      theTiles = nagigateNextStep(theGrid, theTiles, theBeam)
      
      cntTotal = 0
      for row in range(0, len(theTiles)):
        for col in range(0, len(theTiles[row])):
          if theTiles[row][col] == '#':
            cntTotal += 1
      print(f'{beamNum} - {cntTotal}')
      if cntTotal > maxEnergized: maxEnergized = cntTotal
      beamNum += 1

    print(f'Max: {maxEnergized}')