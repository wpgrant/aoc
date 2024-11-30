import re

def navigate(instructions, theMap, thePaths):
  # In part 2, instead of looking at a single path we must navigate all paths
  # and stop when both are at the destination (last char = "Z")
  cntSteps = 0
  currPaths = thePaths
  found = False
  while not found:
    for step in instructions:
      cntZs = 0
      found = True # When evaluating paths we will assume found until we find one that isn't
      cntSteps += 1
      nextPaths = []
      for path in currPaths:
        if step == "L":
          nextPath = theMap[path][0]  
        elif step == "R":
          nextPath = theMap[path][1]
        if nextPath[-1] != "Z":
          found = False
        else:
          cntZs += 1

        nextPaths.append(nextPath)
      
      if found == True:
        print(nextPaths)
        break
      elif cntZs >= 5:
        print(cntZs)
        print(f'{currPaths}-{nextPaths}')
      
      currPaths = nextPaths
      #print(currPaths)
  
  print(cntSteps)

def processLines(lines):
  # First line are the directions
  # Second line is blank
  # Third through the end is the map
  #
  # For part 2 we need to construct multiple paths
  # based on number of "last letters" (A, B, C, etc.)
  theMap = {}
  thePaths = []
  instructions = lines[0].strip()
  for i in range(2, len(lines)):
    theLineMatch = re.match(r'(.*) = \((.*), (.*)\)', lines[i].strip())
    theMap[theLineMatch.group(1)] = [theLineMatch.group(2), theLineMatch.group(3)]
    lastLetter = theLineMatch.group(1)[-1]
    if lastLetter == "A":
      thePaths.append(theLineMatch.group(1))

  navigate(instructions, theMap, thePaths)

if __name__ == '__main__':
  #with open('8b.txt', 'r') as file:
  with open('8.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
  