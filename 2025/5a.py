def isFresh(id, theDB):
  for test in theDB:
    if id >= int(test[0]) and id <= int(test[1]):
      return True
  return False

if __name__ == '__main__':
  #with open('5tst.txt', 'r') as file:
  with open('5.txt', 'r') as file:
    lines = file.readlines()

    theDB = []
    for line in lines:
      if '-' in line:
        theDB.append(line.strip().split('-'))

    theIDs = []
    for line in lines:
      if '-' not in line and line.strip() != '':
        theIDs.append(int(line.strip()))

    freshCount = 0
    for id in theIDs:
      if isFresh(id, theDB):
        freshCount += 1

    print(freshCount)  