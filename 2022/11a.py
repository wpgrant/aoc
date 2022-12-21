import re
import operator

ops = {
  '+' : operator.add,
  '-' : operator.sub,
  '*' : operator.mul,
  '/' : operator.truediv
}

currentMonkeyNumber = '0'
monkeys = {}

class Monkey:

  def __init__(self, number):
    self.number = number
    self.numberOfInspections = 0
    self.items = []
    self.operationNumber1 = ''
    self.operationNumber2 = ''
    self.operator = None
    self.testerDivisibleBy = 0
    self.trueMonkeyDestination = ''
    self.falseMonkeyDestination = ''

  def addItem(self, number):
    self.items.append(number)

  def addInspection(self):
    self.numberOfInspections += 1

def processInstruction(instruction):
  global currentMonkeyNumber
  global monkeys

  if ( instruction.startswith('Monkey') ):
    # Set the new monkey number, and add a monkey
    currentMonkeyNumber = re.match('Monkey ([\d]+):', instruction).group(1)
    monkeys[currentMonkeyNumber] = Monkey(currentMonkeyNumber)

  else:
    theMonkey = monkeys[currentMonkeyNumber]
    if ( instruction.startswith('Starting') ):
      # Add the starting items to that monkey
      strListOfItems = re.match('Starting items: (.*)', instruction).group(1)
      listOfItems = strListOfItems.split(', ')
      for item in listOfItems:
        theMonkey.addItem(item)
      
    elif ( instruction.startswith('Operation') ):
      # Get the operation and process each item
      operation = re.match('.*new = (old|[\d]+) ([-+\*\/]) (old|[\d]+)', instruction)
      theMonkey.operationNumber1 = operation.group(1)
      theMonkey.operationNumber2 = operation.group(3)
      theMonkey.operator = ops[operation.group(2)]

    elif ( instruction.startswith('Test') ):
      # Set the tester on the monkee
      tester = re.match('.*divisible by ([\d]+)', instruction)
      theMonkey.testerDivisibleBy = int( tester.group(1) )

    elif ( instruction.startswith('If true') ):
      # Set the true destination monkey
      destMonkey = re.match('.*throw to monkey ([\d]+)', instruction).group(1)
      theMonkey.trueMonkeyDestination = destMonkey

    elif ( instruction.startswith('If false') ):
      # Set the false destination monkey
      destMonkey = re.match('.*throw to monkey ([\d]+)', instruction).group(1)
      theMonkey.falseMonkeyDestination = destMonkey

def tossItems():
  global monkeys

  for i in range(0, len(monkeys)):
    theMonkey = monkeys[str(i)]
    for item in theMonkey.items:
      # Increment monkee inspection level
      theMonkey.addInspection()

      # Operate on worry level
      number1 = int( theMonkey.operationNumber1.replace('old', str(item)) )
      number2 = int( theMonkey.operationNumber2.replace('old', str(item)) )
      result = theMonkey.operator(number1, number2)
      
      # Divide worry level by 3
      result = int(result / 3)
      
      # Check if divisible, and throw
      if ( result % theMonkey.testerDivisibleBy == 0 ):
        monkeys[theMonkey.trueMonkeyDestination].items.append(result)
      else:
        monkeys[theMonkey.falseMonkeyDestination].items.append(result)
    
    theMonkey.items = []

if __name__ == '__main__':
  with open('11.txt', 'r') as file:
    monkeyInstructions = file.readlines()

    for instruction in monkeyInstructions:
      processInstruction(instruction.strip())

    for rnd in range(0, 20):
      tossItems()

    # Display the monkeys, number of inspections, and final list
    #for i in range(0, len(monkeys)):
    #  monkey = monkeys[str(i)]
    #  print(f'{monkey.number} - {monkey.numberOfInspections} - {monkey.items}')

    # Level of Monkey Business
    sorted_monkeys = sorted( monkeys.items(), key=lambda x: x[1].numberOfInspections, reverse=True)
    firstMost = monkeys[str(sorted_monkeys[0][0])].numberOfInspections
    secondMost = monkeys[str(sorted_monkeys[1][0])].numberOfInspections
    levelOfMonkeeBusiness = int(firstMost) * int(secondMost)
    print(levelOfMonkeeBusiness)
