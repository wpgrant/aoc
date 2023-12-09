def getOutput(input):
  steps = []
  steps.append(input)
  allZeroes = False
  while not allZeroes:
    lastStep = len(steps)-1
    nextStep = []
    # Get the next step
    for i in range(0, len(steps[lastStep])-1):
      nextStep.append(steps[lastStep][i+1] - steps[lastStep][i])
    # See if they are all zeroes
    totStep = 0
    for val in nextStep:
      totStep += val
    if totStep == 0:
      allZeroes = True
    else:
      steps.append(nextStep)
  
  # Now that we have the steps, traverse back up
  # In part 2 we are getting the left values
  prevStep = 0
  finalVal = -1
  for iStep in range(len(steps)-1,-1,-1):
    finalVal = steps[iStep][0] - prevStep
    prevStep = finalVal
  
  return finalVal

def processLines(lines):
  theInputs = []
  theOutputs = []
  for line in lines:
    strInput = line.strip().split(' ')
    # Convert each element into an int (probably a more elegant way to do this)
    iInput = []
    for theStr in strInput:
      iInput.append(int(theStr))

    theInputs.append(iInput)

  for input in theInputs:
    theOutputs.append(getOutput(input))
  
  totOutput = 0
  for output in theOutputs:
    totOutput += output

  print(totOutput)

if __name__ == '__main__':
  #with open('9b.txt', 'r') as file:
  with open('9.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
  