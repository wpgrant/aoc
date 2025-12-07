def addSpace(theArr, row, col):
  if row < 0 or row >= len(theArr) or col < 0 or col >= len(theArr[0]):
    return 0
  if theArr[row][col] == '@':
    return 1
  return 0

def countRolls(theArr):
  theCount = 0
  for row in range(0,len(theArr)):
    for col in range(0,len(theArr[0])):
      if theArr[row][col] == '@':
        rollCount = addSpace(theArr, row-1, col-1) + addSpace(theArr, row-1, col) + addSpace(theArr, row-1, col+1)
        rollCount += addSpace(theArr, row, col-1) + addSpace(theArr, row, col+1)
        rollCount += addSpace(theArr, row+1, col-1) + addSpace(theArr, row+1, col) + addSpace(theArr, row+1, col+1)
        if rollCount < 4:
          theCount += 1
  return theCount

if __name__ == '__main__':
  #with open('4tst.txt', 'r') as file:
  with open('4.txt', 'r') as file:
    lines = file.readlines()

    theArr = []
    for line in lines:
      theArr.append(list(line.strip()))
    
    theCount = countRolls(theArr)
    print(theCount)