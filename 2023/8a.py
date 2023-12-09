import re

def navigate(instructions, theMap):
  found = False
  nextLoc = "AAA"
  cntSteps = 0
  while not found:
    for step in instructions:
      cntSteps += 1
      if step == "L":
        nextLoc = theMap[nextLoc][0]
      elif step == "R":
        nextLoc = theMap[nextLoc][1]
      if nextLoc == "ZZZ":
        found = True
        break
  
  print(cntSteps)

def processLines(lines):
  # First line are the directions
  # Second line is blank
  # Third through the end is the map
  theMap = {}  
  instructions = lines[0].strip()
  for i in range(2, len(lines)):
    theLineMatch = re.match(r'(.*) = \((.*), (.*)\)', lines[i].strip())
    theMap[theLineMatch.group(1)] = [theLineMatch.group(2), theLineMatch.group(3)]

  navigate(instructions, theMap)

if __name__ == '__main__':
  #with open('8a.txt', 'r') as file:
  #with open('8aa.txt', 'r') as file:
  with open('8.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
  