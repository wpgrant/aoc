
import re

cycle = 0
registerX = 1
totalValue = 0

def checkCycle():
  global cycle
  global registerX
  global totalValue

  if ((cycle-20) % 40 == 0):
    totalValue += cycle * registerX


def processInstruction(operation, value):
  global cycle
  global registerX

  if (operation == 'noop'):
    cycle += 1
    checkCycle()
  if (operation == 'addx'):
    for i in range(0, 2): # 2 cycles
      cycle += 1
      checkCycle()
    registerX += value

if __name__ == '__main__':
  with open('10.txt', 'r') as file:
    instructions = file.readlines()

    for instruction in instructions:
      parsedInstruction = re.match('(addx|noop)\s*([0-9-]*)', instruction.strip())
      operation = parsedInstruction.group(1)
      if (operation == 'addx'):
        changeX = int(parsedInstruction.group(2))
      else:
        changeX = 0
      processInstruction(operation, changeX)

    print(totalValue)
