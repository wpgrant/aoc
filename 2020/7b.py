from re import search
from re import finditer

def findBags(rules, currentCount, colorsToFind, multiplier):
  newColorsToFind = []
  for color in colorsToFind:
    theMultiplier = int(search('(\d+)\s(.*)', color)[1])
    thisMultiplier = theMultiplier * multiplier
    currentCount += thisMultiplier
    theColor = search('(\d+)\s(.*)', color)[2]
    if theColor in rules.keys():
      currentCount = findBags(rules, currentCount, rules[theColor], thisMultiplier)
    
  return currentCount

def setupRules(rules):
  theRules = {}
  for rule in rules:
    # Split rule into outsideBag and insideBag, with quantities
    if rule.find('contain') >= 0:
      outsideBag = rule.split("contain", 1)[0]
      insideBags = rule.split("contain", 1)[1]
      outsideBagColor = search('(.*)\sbags', outsideBag)[1]
      for insideBag in finditer('(\d+)\s(.*?)\sbag', insideBags):
        insideQuantity = insideBag[1]
        insideColor = insideBag[2]
        insideBagColorAndQty = f"{insideQuantity} {insideColor}"
        if outsideBagColor in theRules:
          theRules[outsideBagColor].append(insideBagColorAndQty)
        else:
          theRules[outsideBagColor] = [insideBagColorAndQty]
  return theRules

if __name__ == '__main__':
  with open('7.txt', 'r') as file:
    rules = file.readlines()
    theRules = setupRules(rules)
    colorsToFind = ["1 shiny gold"]
    count = findBags(theRules, 0, colorsToFind, 1)
    count -= 1 # Exclude the bag by itself
    print(f'The count is {count}.') 