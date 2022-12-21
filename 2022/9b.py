import re

knots = [] # Head is 0, Tail is 9
thePositions = []

class Knot:
  def __init__(self):
    self.row = 0
    self.col = 0

  def changeRow(self, val):
    self.row += val

  def changeCol(self, val):
    self.col += val


# Origin is 0,0
# Right and Up is +1
# Left and Down is -1

def makeMove(direction, numMoves):
  for move in range(0, numMoves):
    if direction == "R":
      knots[0].changeCol(1)
    elif direction == "L":
      knots[0].changeCol(-1)
    elif direction == "U":
      knots[0].changeRow(1)
    elif direction == "D":
      knots[0].changeRow(-1)

    #print(f'Head Move: ({knots[0].row}-{knots[0].col})')
    
    makeTailMove()

def makeTailMove():

  for knotNum in range(1, 10):
    prevKnotRow = knots[knotNum-1].row
    prevKnotCol = knots[knotNum-1].col
    currentKnotRow = knots[knotNum].row
    currentKnotCol = knots[knotNum].col
    if ( (abs(prevKnotRow - currentKnotRow) > 1) \
      or (abs(prevKnotCol - currentKnotCol) > 1) ):
      # This knot isn't within 1 of previous; need to move
      # Using `delta / abs(delta)` to constrain the move to 1
      if (prevKnotRow != currentKnotRow):
        knots[knotNum].changeRow( int( (prevKnotRow - currentKnotRow) / abs(prevKnotRow - currentKnotRow) ) )
      if (prevKnotCol != currentKnotCol):
        knots[knotNum].changeCol( int( (prevKnotCol - currentKnotCol) / abs(prevKnotCol - currentKnotCol) ) )
  
  # Record the tail (9) move    
  thePositions.append( f'{knots[9].row}-{knots[9].col}' )
  #print(f'Tail Move: ({knots[9].row}-{knots[9].col})')

if __name__ == '__main__':
  with open('9.txt', 'r') as file:
    headMoves = file.readlines()

    # Create the 10 knots at their starting position
    for knotNum in range(0,10):
      newKnot = Knot()
      knots.append(newKnot)

    # Add 0,0 position
    thePositions.append('0-0')

    for move in headMoves:
      parsedMove = re.match('([RLUD]) (\d+)', move.strip())
      direction = parsedMove.group(1)
      numMoves = int(parsedMove.group(2))
      makeMove(direction, numMoves)

    # Remove dupes
    noDupes = [*set(thePositions)]
    # Sort the list
    noDupes.sort()

    #print(noDupes)
    print( len(noDupes) )