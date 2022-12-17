def findDupe(theString):
  testString = theString[0:1]
  for i in range(1, len(theString)):
    theChar = theString[i:i+1]
    if (testString.find(theChar) >= 0):
      return True
    else:
      testString += theChar
  
  return False


if __name__ == '__main__':
  with open('6.txt', 'r') as file:
    theSignal = file.readline()
    i = 14
    isFound = False
    while(i < len(theSignal) + 1):
      testChars = theSignal[i-14:i]
      if not findDupe(testChars):
        print(i)
        quit()
        
      i += 1

  print("Not found.")