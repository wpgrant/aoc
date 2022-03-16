from re import search
from re import finditer

def findBags(rules, currentCount, colorsToFind, colorsProcessed):
  newColorsToFind = []
  for color in colorsToFind:
    if color not in colorsProcessed:
      currentCount += 1
      colorsProcessed.append(color)
      if color in rules.keys():
        newColorsToFind += rules[color]
  if len(newColorsToFind) > 0:
    return findBags(rules, currentCount, newColorsToFind, colorsProcessed)
  else:
    return currentCount

def setupRules(rules):
  theRules = {}
  for rule in rules:
    # Split rule into outsideBag and insideBag
    if rule.find('contain') >= 0:
      outsideBag = rule.split("contain", 1)[0]
      insideBags = rule.split("contain", 1)[1]
      outsideBagColor = search('(.*)\sbags', outsideBag)[1]
      for insideBagColorStr in finditer('(\d+)\s(.*?)\sbag', insideBags):
        insideBagColor = insideBagColorStr[2]
        if insideBagColor in theRules:
          theRules[insideBagColor].append(outsideBagColor)
        else:
          theRules[insideBagColor] = [outsideBagColor]
  return theRules

if __name__ == '__main__':
  with open('7.txt', 'r') as file:
    rules = file.readlines()
    theRules = setupRules(rules)
    colorsToFind = ["shiny gold"]
    colorsProcessed = []
    count = findBags(theRules, 0, colorsToFind, colorsProcessed)
    count -= 1 # Exclude the bag by itself
    print(f'The count is {count}.') 