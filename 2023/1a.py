if __name__ == '__main__':
  #with open('1a.txt', 'r') as file:
  with open('1.txt', 'r') as file:
    lines = file.readlines()

  total = 0
  for line in lines:
    sNumber = ''.join(filter(str.isdigit, line))
    sTwoDigitNumber = ''.join([ sNumber[0], sNumber[len(sNumber) - 1]])    
    iNum = int(sTwoDigitNumber)
    total += iNum

  print(total)
