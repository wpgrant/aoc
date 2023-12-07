import re

class Map:
  def __init__(self, mapType, sourceStart, destStart, rangeLen):
    self.mapType = mapType
    self.sourceStart = sourceStart
    self.sourceEnd = sourceStart + rangeLen - 1
    self.destStart = destStart
    self.destEnd = destStart + rangeLen - 1
    self.translation = destStart - sourceStart

def getNext(mapType, num):
  for map in almanac:
    if map.mapType == mapType:
      if num >= map.sourceStart and num <= map.sourceEnd:
        # Found it, now translate it
        return num + map.translation
  # If I get here, return the same number
  return num

def getLocation(seed):
  # The chain is known, so we will just process these in order
  # Any items not found, the destination is the same as the source
  # Chain is: seed-soil-fertilizer-water-light-temperature-humidity-location
  soil = getNext('seed-to-soil', seed)
  fertilizer = getNext('soil-to-fertilizer', soil)
  water = getNext('fertilizer-to-water', fertilizer)
  light = getNext('water-to-light', water)
  temperature = getNext('light-to-temperature', light)
  humidity = getNext('temperature-to-humidity', temperature)
  location = getNext('humidity-to-location', humidity)
  return location

def addToMap(line, mapType):
  # parse the destStart, sourceStart, and rangeLen values
  theNums = line.split(' ')
  destStart = int(theNums[0])
  sourceStart = int(theNums[1])
  rangeLen = int(theNums[2])
  almanac.append(Map( mapType, sourceStart, destStart, rangeLen) )

def addSeeds(line):
  seedsMatch = re.match('seeds: (.*)', line)
  seeds = seedsMatch.group(1)
  seedStrings = seeds.split(' ')
  return seedStrings
  
def processLines(lines):
  # Add the input
  for line in lines:
    # First, determine what kind of line it is
    if line.find('seeds:') >= 0:
      seedStrings = addSeeds(line.strip())
    elif line.find(':') >= 0:
      mapTypeMatch = re.match(r'(.*) map:', line.strip())
      mapType = mapTypeMatch.group(1)
    elif len(line.strip()) == 0:
      continue
    else:
      addToMap(line.strip(), mapType)
  
  # Now navigate each seed to find the location
  lowestLoc = None
  for seed in seedStrings:
    loc = getLocation(int(seed))
    if lowestLoc == None or lowestLoc > loc:
      lowestLoc = loc

  print(lowestLoc)

if __name__ == '__main__':
  global almanac
  almanac = []
  #with open('5a.txt', 'r') as file:
  with open('5.txt', 'r') as file:
    lines = file.readlines()
    processLines(lines)
