import sys

def calculatePriorityForItem(item):
  if item.islower():
    num = ord(item) - 96 # ord('a') = 97, a-z = 1-26
  else:
    num = ord(item) - 38 # ord('A') = 65, A-Z = 27-52
  return num

def calculatePriority(elf1, elf2, elf3):
  checks = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  found = False
  for i in range(len(checks)):
    if(elf1.find(checks[i]) >= 0):
      if(elf2.find(checks[i]) >= 0):
        if(elf3.find(checks[i]) >= 0):
          found = True
          break
  if(found):
    return calculatePriorityForItem(checks[i])
  else:
    print('ERROR: Couldn''t find one.')
    print(elf1)
    print(elf2)
    print(elf3)
    quit()

if __name__ == '__main__':
  totalPriority = 0
  with open('3.txt', 'r') as file:
    while True:
      elf1 = file.readline().strip()
      elf2 = file.readline().strip()
      elf3 = file.readline().strip()
      if ( (len(elf1) > 0) and (len(elf2) > 0) and (len(elf3) > 0)):
        priority = calculatePriority(elf1, elf2, elf3)
        totalPriority += priority
      else:
        break

  print(totalPriority)