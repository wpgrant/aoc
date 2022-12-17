import sys
import re

if __name__ == '__main__':
  readingStacks = True
  stackLines = []
  stacks = {}
  moves = []
  with open('5.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      # File is split between initial stacks (top)
      # and moves (bottom), split by a single blank
      # line. Process the stacks and then switch to
      # the moves.
      if (readingStacks):
        if (line.strip() != ''):
          # Reading Stacks
          stackLines.append(line)
        elif (line.strip() == ''):
          # Dividing line, should process the stacks

          # Get last stack number
          stackNamesLine = stackLines[len(stackLines)-1].strip()
          lastStack = re.search('.*(\d+)$', stackNamesLine).group(1)

          # Load the stacks
          for stackNum in range(1, int(lastStack) + 1):
            stacks[str(stackNum)] = []
            for stackLine in range(len(stackLines)-2, -1, -1):
              locCrate = ((stackNum - 1) * 4) + 1
              crate = stackLines[stackLine][locCrate:locCrate + 1].strip()
              if (len(crate) == 1):
                stacks[str(stackNum)].append(crate)
          
          # From now on we can read in the moves
          readingStacks = False
      else:
        # Processing moves: moving crates 1 by 1
        if (line.strip() != ''):
          count = int(re.match("move (\d+).*", line.strip()).group(1))
          fromStack = re.match(".*from (\d+).*", line.strip()).group(1)
          toStack = re.match(".*to (\d+).*", line.strip()).group(1)
          for i in range(1, count + 1):
            ltr = stacks[fromStack].pop()
            stacks[toStack].append(ltr)

  topStack = ""
  for stackNum in range(1, int(lastStack) + 1):
    topStack = topStack + stacks[str(stackNum)][-1]
  
  print(topStack)
