def countStep(step):
  cv = 0
  for char in step:
    val = ord(char)
    cv += val
    cv = cv * 17
    cv = cv % 256
  return cv

if __name__ == '__main__':
  #with open('15a.txt', 'r') as file:
  with open('15.txt', 'r') as file:
    lines = file.readlines()
    totValue = 0
    for line in lines:
      steps = line.split(',')
      for step in steps:
        if len(step.strip()) > 0:
          totValue += countStep(step.strip())

    print(totValue)