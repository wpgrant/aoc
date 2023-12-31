import re

def countSpaces(instructions):
  # Needed help on this to understand the geometric formulas
  # We can get the interior area with pick's theorem
  # Then we can add the boundary points (shoelace?)
  points = [(0, 0)]
  boundary = 0
  directions = {}
  directions["U"] = (-1, 0)
  directions["D"] = (1, 0)
  directions["L"] = (0, -1)
  directions["R"] = (0, 1)
  for instruction in instructions:
    # Next point = Previous Point moved a number of steps in a direction
    dir = directions[instruction[0]]
    steps = int(instruction[1])
    boundary += steps
    rowSteps = dir[0] * steps
    colSteps = dir[1] * steps
    newPoint = (points[-1][0] + rowSteps, points[-1][1] + colSteps)
    points.append(newPoint)
  
  internalCount = 0
  for i in range(0,len(points)):
    internalCount += points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1])
  internalCount = int(abs(internalCount)/2)
  internalCount = int(internalCount - (boundary/2) + 1)
  count = int(internalCount + boundary)
  return count

def getInstructions(lines):
  instructions = []
  for line in lines:
    pattern = r'([RLUD]) (\d*) \(#([a-z0-9]{5})([a-z0-9]{1})\)'
    match = re.match(pattern, line.strip())
    dirs = { 0: "R", 1: "D", 2: "L", 3: "U" }
    instructions.append([dirs[int(match.group(4))], int(match.group(3), 16)])
  return instructions

if __name__ == '__main__':
  #with open('18b.txt', 'r') as file:
  with open('18.txt', 'r') as file:
    lines = file.readlines()
    instructions = getInstructions(lines)
    count = countSpaces(instructions)
    print(count)
