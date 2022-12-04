import sys

def calculatePriorityForItem(item):
  if item.islower():
    num = ord(item) - 96 # ord('a') = 97, a-z = 1-26
  else:
    num = ord(item) - 38 # ord('A') = 65, A-Z = 27-52
  return num

def calculatePriority(rucksack):
  totalLength = len(rucksack)
  index1 = 0
  index2 = int(totalLength / 2)
  found = False
  for i in range(index2): # not inclusive
    item = rucksack[i]
    if (item in rucksack[index2:]):
      found = True
      break

  if found:
    
    return calculatePriorityForItem(item)
  else:
    print('ERROR: Couldn''t find one.')
    quit()

if __name__ == '__main__':
  with open('3.txt', 'r') as file:
    lines = file.readlines()

  totalPriority = 0
  for rucksack in lines:
    priority = calculatePriority(rucksack.strip())
    totalPriority += priority

  print(totalPriority)