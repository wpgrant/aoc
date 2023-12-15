import re

def countPatterns(pattern, combos):
  # pattern is like 1, 2, 3
  nums = pattern.split(',')
  thePattern = "^[ .]*"
  for num in nums:
    thePattern += f"#{{{num}}}[ .]+"

  theRegexPattern = thePattern[:-1] + "*$"
  
  cnt = 0
  for combo in combos:
    #theCombo = combo.replace(".", " ")
    if re.match(theRegexPattern, combo):
      #print(f'SUCCESS --> {theRegexPattern}-{combo}')
      cnt += 1
  return cnt

def generateCombos(combos):
  # Find first ? position
  pos = combos[0].find('?')
  newCombos = []
  # Add new combos
  for combo in combos:
    newPound = combo[:pos] + "#" + combo[pos+1:]
    newCombos.append(newPound)
    newPeriod = combo[:pos] + "." + combo[pos+1:]
    newCombos.append(newPeriod)
  return(newCombos)


def getCombos(part):
  # We will get a pattern, let's say 
  #   ..#??#..
  # We will turn this into combos:
  #   ..####..
  #   ..#..#..
  #   ..##.#..
  #   ..#.##..
  combos = []
  combos.append(part)
  stillQuestions = True
  while stillQuestions:
    stillQuestions = False
    for combo in combos:
      if combo.find('?') >= 0:
        stillQuestions = True
        break
    if stillQuestions:
      combos = generateCombos(combos)
  return combos

def getCount(line):
  pattern = r'([?#.]+) (.*)'
  match = re.match(pattern, line)
  # There is a more streamlined way to do this, but let's just 
  # generate all combos and check them
  combos = getCombos(match.group(1))
  cntPatterns = countPatterns(match.group(2), combos)
  return cntPatterns

if __name__ == '__main__':
  #with open('12a.txt', 'r') as file:
  with open('12.txt', 'r') as file:
    lines = file.readlines()
    totArrangements = 0
    for line in lines:
      cntArrangements = getCount(line.strip())
      totArrangements += cntArrangements
    print(totArrangements)