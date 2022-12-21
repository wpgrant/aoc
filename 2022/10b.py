
import re

cycle = 0
registerX = 1
display = []

def writePixel():
  global cycle
  global registerX
  global display

  # Reset on new rows
  if cycle >= 40:
    cycle -= 40

  if (registerX-1 <= cycle <= registerX+1):
    display.append('#')
  else:
    display.append('.')

def processInstruction(operation, value):
  global cycle
  global registerX

  if (operation == 'noop'):
    writePixel()
    cycle += 1
  if (operation == 'addx'):
    for i in range(0, 2): # 2 cycles
      writePixel()
      cycle += 1
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

    # Print the array in rows
    for row in range(0, 6):
      txtRow = ''
      for col in range(0,40):
        txtRow += display[(row*40) + col]
      print(txtRow)

        
