def convertToNumString(theNum: str):
  if len(theNum) == 1:
    sNum = theNum
  else:
    sNum = theNum.replace('one','1').replace('two','2').replace('three','3') \
                .replace('four','4').replace('five','5').replace('six','6') \
                .replace('seven','7').replace('eight','8').replace('nine','9') \
                .replace('zero','0')
  return sNum

def getNum(sString: str, fromLeft: bool):
  # If fromLeft = true, from left, else from right
  arrValues = ['one','two','three','four','five','six','seven','eight', \
               'nine','zero','1','2','3','4','5','6','7','8','9','0']
  if(fromLeft):
    bestPos = 1000
    bestLen = -1
    for val in arrValues:
      pos = sString.find(val)
      if pos >=0 and pos<bestPos:
        bestPos = pos
        bestLen = len(val)
  else:
    bestPos = -1
    bestLen = -1
    for val in arrValues:
      pos = sString.rfind(val)
      if pos >=0 and pos>bestPos:
        bestPos = pos
        bestLen = len(val)
  
  return convertToNumString( sString[bestPos:bestPos+bestLen] )


if __name__ == '__main__':
#  with open('1b.txt', 'r') as file:
  with open('1.txt', 'r') as file:
    lines = file.readlines()

  total = 0
  for line in lines:
    firstNumber = getNum(line.strip(), True)
    lastNumber = getNum(line.strip(), False)
    iNum = int(f"{firstNumber}{lastNumber}")
    total += iNum

  print(total)