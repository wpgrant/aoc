import sys

def countSlope(right, down):
  cntTrees = 0
  lenMatrix = len(lines[0])
  iLoc = 0
  downCount = 0
  for str in lines[1:]:
    downCount = downCount + 1
    if (downCount < down):
      continue
    iLoc = (iLoc + right) % (lenMatrix - 1)
    currCar = str[iLoc]
    if (currCar == '#'):
      cntTrees += 1
    downCount = 0
  return cntTrees

if __name__ == '__main__':
  with open('3.txt', 'r') as file:
    lines = file.readlines()

    test1 = countSlope(1, 1)
    test2 = countSlope(3, 1)
    test3 = countSlope(5, 1)
    test4 = countSlope(7, 1)
    test5 = countSlope(1, 2)
  #print(f'{test1},{test2},{test3},{test4},{test5}')
  print(test1 * test2 * test3 * test4 * test5)