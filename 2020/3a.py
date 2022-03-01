import sys

with open('3.txt', 'r') as file:
	lines = file.readlines()

cntTrees = 0
lenMatrix = len(lines[0])
iLoc = 0
for str in lines[1:]:
  iLoc = (iLoc + 3) % (lenMatrix - 1)
  currCar = str[iLoc]
  #print(f'{iLoc} -{currCar}')
  if (currCar == '#'):
    cntTrees += 1

print(cntTrees)