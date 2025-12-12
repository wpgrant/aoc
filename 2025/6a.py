import operator

operations = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv
}

def calc(theProblems, probNumber):
  operation = theProblems[len(theProblems)-1][probNumber]
  if operation not in operations:
    print(f"Unknown operator: {operation}")
  
  theTotal = int(theProblems[0][probNumber])
  for row in range(1,len(theProblems)-1):
    theTotal = operations[operation](theTotal, int(theProblems[row][probNumber]))
  return theTotal

if __name__ == '__main__':
  #with open('6tst.txt', 'r') as file:
  with open('6.txt', 'r') as file:
    lines = file.readlines()

    theProblems = []
    for line in lines:
      theProblems.append(line.strip().split())
    
    theSum = 0
    for i in range(0,len(theProblems[0])):
      theSum += calc(theProblems, i)
    
    print(theSum)