from re import search
from re import finditer

def setupRules(rules):
  theRules = {}
  i = 0
  for rule in rules:
    theRules[i] = rule
    i += 1
  theRules[i] = "end"
  return theRules

def changeRules(rules, stepNum):
  ruleType = rules[stepNum].split(" ")[0]
  ruleValue = rules[stepNum].split(" ")[1]
  if ruleType == "nop":
    rules[stepNum] = f"jmp {ruleValue}"
    return rules
  if ruleType == "jmp":
    rules[stepNum] = f"nop {ruleValue}"
    return rules
  return None

def runStep(rules, stepNum, acc):
  if stepNum >= len(rules) - 1:
    return acc
  currRule = rules[stepNum]
  if currRule == "x":
    return -1 # signify infinite loop
  ruleType = currRule.split(" ")[0]
  ruleValue = int(currRule.split(" ")[1])
  rules[stepNum] = "x"
  if ruleType == "nop":
    stepNum += 1
  if ruleType == "acc":
    stepNum += 1
    acc += ruleValue
  if ruleType == "jmp":
    stepNum += ruleValue
  return runStep(rules, stepNum, acc)

if __name__ == '__main__':
  with open('8.txt', 'r') as file:
    rules = file.readlines()
    theRules = setupRules(rules)
    for i in range(0, len(theRules) -1):
      theRules = setupRules(rules)
      theCustomRules = changeRules(theRules, i)
      if theCustomRules != None: # rules changed
        acc = runStep(theCustomRules, 0, 0)
        if acc != -1: # not infinite
          print(f'The acc is {acc}.')
          exit
  