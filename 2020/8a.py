from re import search
from re import finditer

def setupRules(rules):
  theRules = {}
  i = 0
  for rule in rules:
    theRules[i] = rule
    i += 1
  return theRules

def runStep(rules, stepNum, acc):
  currRule = rules[stepNum]
  if currRule == "x":
    return acc
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
    acc = 0
    value = runStep(theRules, 0, acc)
    print(f'The count is {value}.') 