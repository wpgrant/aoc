def getMax(bank):
  tens = 0
  ones = 0
  for index,strBattery in enumerate(bank):
    battery = int(strBattery)
    if battery > tens:
      if index < len(bank) - 1:
        tens = battery
        ones = 0
      else:
        if battery > ones:
          ones = battery
    else:
      if battery > ones:
        ones = battery
  return int(f"{tens}{ones}")

if __name__ == '__main__':
  #with open('3tst.txt', 'r') as file:
  with open('3.txt', 'r') as file:
    lines = file.readlines()
    
    theTotal = 0
    for line in lines:
      theTotal += getMax(line.strip())

    print(theTotal)
