def getMax(bank):
  strFinalNum = ""
  lastIndex = -1
  while len(strFinalNum) != 12:
    lastNum = 0
    bFound = False
    for searchNum in range(9,-1,-1):
      for index in range(lastIndex+1,len(bank)-12+len(strFinalNum)+1):
        if int(bank[index:index+1]) == searchNum:
          lastNum = searchNum
          lastIndex = index
          bFound = True
          break
      if bFound:
        break
    strFinalNum = strFinalNum + str(lastNum)
    #print(strFinalNum)
  return int(strFinalNum)


if __name__ == '__main__':
  #with open('3tst.txt', 'r') as file:
  with open('3.txt', 'r') as file:
    lines = file.readlines()
    
    theTotal = 0
    for line in lines:
      theTotal += getMax(line.strip())

    print(theTotal)
