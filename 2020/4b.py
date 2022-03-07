import sys
from re import search

def performCheck(check, passportLines):
  if passportLines.count(check) == 0:
    return False
  matches = search(f'{check}:(\S*)', passportLines)
  value = matches[1]

  if check == 'byr' or check == 'iyr' or check == 'eyr':
    if value.isdigit and len(value) == 4:
      year = int(value)
      if check == 'byr':
        if year >= 1920 and year <= 2002:
          return True
      elif check == 'iyr':
        if year >= 2010 and year <= 2020:
          return True
      elif check == 'eyr':
        if year >= 2020 and year <= 2030:
          return True
  elif check == 'hgt':
    strHeight = search('^(\d+)(cm|in)$', value)
    if strHeight != None:
      height = int(strHeight[1])
      if strHeight[2] == 'cm':
        if height >= 150 and height <= 193:
          return True
      elif strHeight[2] == 'in':
        if height >= 59 and height <= 76:
          return True
  elif check == 'hcl':
    haircolor = search(f'^#[0-9a-f]{{6}}$', value)
    if haircolor != None:
      return True
  elif check == 'ecl':
    list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in list:
      return True
  elif check == 'pid':
    if search(f'^[0-9]{{9}}$', value) != None:
      return True
  return False

def processPassport(passportLines):
  checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #leaving cid out, it is optional
  for check in checks:
    if performCheck(check, passportLines) == False:
      return False      
  return True

def countPassports(strInputFile):
  cntValidPassports = 0
  with open('4.txt', 'r') as file:
    lines = file.readlines()
    passportLines = ""
    for line in lines:
      if len(line.strip()) == 0:
        # New Passport
        if processPassport(passportLines):
          cntValidPassports += 1
        passportLines = ""
        continue
      else:
        passportLines += line
    # Need to process last passport
    if processPassport(passportLines):
      cntValidPassports += 1
    print(f"Valid Passports: {cntValidPassports}")

if __name__ == '__main__':
  countPassports('4.txt')