import operator

operations = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv
}

def calc(nums, operation):
  if operation not in operations:
    print(f"Unknown operator: {operation}")
  
  total = int(nums[0])
  for num in nums[1:]:
    total = operations[operation](total, int(num))
  
  return total

def processAll(theProblems):
  theSum = 0
  nums = []
  for col in range(len(theProblems[0])-1,-1,-1):
    num = ""
    for row in range(0,len(theProblems)-1):
      if theProblems[row][col] != '':
        num += theProblems[row][col]
    if num.strip() != '':
      nums.append(int(num))
      if theProblems[len(theProblems)-1][col] != ' ':
        theCalc = calc(nums, theProblems[len(theProblems)-1][col])
        theSum += theCalc
        nums = []
  
  return theSum

if __name__ == '__main__':
  #with open('6tst.txt', 'r') as file:
  with open('6.txt', 'r') as file:
    lines = file.readlines()

    theProblems = []
    for line in lines:
      theProblems.append(list(line.rstrip('\n\r'))) # Leave trailing spaces
    
    theSum = processAll(theProblems)
    print(theSum)