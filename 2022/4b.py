import sys

def checkForOverlap(pair):
  comma = pair.find(',')
  elf1 = pair[0:comma]
  elf2 = pair[comma+1:]

  dash1 = elf1.find('-')
  elf1start = int(elf1[0:dash1])
  elf1end = int(elf1[dash1+1:])
  dash2 = elf2.find('-')
  elf2start = int(elf2[0:dash2])
  elf2end = int(elf2[dash2+1:])

  if ( (elf2start <= elf1start <= elf2end) or \
      (elf2start <= elf1end <= elf2end) or \
      (elf1start <= elf2start <= elf1end) or \
      (elf1start <= elf2end <= elf1end) ):
    return True
  else:
    return False

if __name__ == '__main__':
  totalOverlap = 0
  with open('4.txt', 'r') as file:
    lines = file.readlines()
    for pair in lines:
      if (checkForOverlap(pair.strip())):
        totalOverlap += 1

  print(totalOverlap)