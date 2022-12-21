import re

headRow = 0
tailRow = 0
headCol = 0
tailCol = 0

thePositions = []

# Origin is 0,0
# Right and Up is +1
# Left and Down is -1

def makeHeadMove(direction, numMoves):
  global headCol
  global headRow

  for move in range(0, numMoves):
    if direction == "R":
      headCol += 1
    elif direction == "L":
      headCol -= 1
    elif direction == "U":
      headRow += 1
    elif direction == "D":
      headRow -= 1

    #print(f'Head Move: ({headRow}-{headCol})')
    
    makeTailMove()

def makeTailMove():
  global tailCol
  global tailRow

  if ( (abs(headRow - tailRow) > 1) or (abs(headCol - tailCol) > 1) ):
    # The tail isn't within 1; need to move
    # Using `delta / abs(delta)` to constrain the move to 1
    if (headRow != tailRow):
      tailRow += int( (headRow - tailRow) / abs(headRow - tailRow) )
    if (headCol != tailCol):
      tailCol += int( (headCol - tailCol) / abs(headCol - tailCol) )
    thePositions.append(f'{tailRow}-{tailCol}')

  #print(f'Tail Move: ({tailRow}-{tailCol})')

if __name__ == '__main__':
  with open('9.txt', 'r') as file:
    headMoves = file.readlines()

    # Add 0,0 position
    thePositions.append('0-0')

    for move in headMoves:
      parsedMove = re.match('([RLUD]) (\d+)', move.strip())
      direction = parsedMove.group(1)
      numMoves = int(parsedMove.group(2))
      makeHeadMove(direction, numMoves)

    # Remove dupes
    noDupes = [*set(thePositions)]
    # Sort the list
    noDupes.sort()

    #print(noDupes)
    print( len(noDupes) )