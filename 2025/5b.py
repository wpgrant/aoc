if __name__ == '__main__':
  #with open('5tst.txt', 'r') as file:
  with open('5.txt', 'r') as file:
    lines = file.readlines()

    theDB = []
    for line in lines:
      if '-' in line:
        theDB.append(line.strip().split('-'))

    # Sort the array by the first column
    theSortedDB = sorted(theDB, key=lambda theDB: int(theDB[0]))
    print(theSortedDB)
    
    cntFresh = 0
    lastEnd = 0
    for row in range(0, len(theSortedDB)):
      if int(theSortedDB[row][0]) > lastEnd:
        # No overlap, count full range
        cntFresh += int(theSortedDB[row][1]) - int(theSortedDB[row][0]) + 1
        lastEnd = int(theSortedDB[row][1])
      else:
        # Overlap, only count the gap between the last end and the new end,
        # if it's positive. Otherwise leave the last end alone.
        tmpCount = int(theSortedDB[row][1]) - lastEnd
        if tmpCount > 0:
          cntFresh += tmpCount
          lastEnd = int(theSortedDB[row][1])
    print(cntFresh)