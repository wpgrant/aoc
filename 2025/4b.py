def addSpace(row, col):
  global theArr
  if row < 0 or row >= len(theArr) or col < 0 or col >= len(theArr[0]):
    return 0
  if theArr[row][col] == '@':
    return 1
  return 0

def findRolls():
  global theArr
  theCount = 0
  for row in range(0,len(theArr)):
    for col in range(0,len(theArr[0])):
      if theArr[row][col] == '@':
        rollCount = addSpace(row-1, col-1) + addSpace(row-1, col) + addSpace(row-1, col+1)
        rollCount += addSpace(row, col-1) + addSpace(row, col+1)
        rollCount += addSpace(row+1, col-1) + addSpace(row+1, col) + addSpace(row+1, col+1)
        if rollCount < 4:
          theCount += 1
          theArr[row][col] = '.'
  return theCount

if __name__ == '__main__':
  #with open('4tst.txt', 'r') as file:
  with open('4.txt', 'r') as file:
    lines = file.readlines()

    global theArr
    theArr = []
    for line in lines:
      theArr.append(list(line.strip()))
    
    totRolls = 0
    theCount = 1
    while theCount > 0:
      theCount = findRolls()
      totRolls += theCount

    print(totRolls)