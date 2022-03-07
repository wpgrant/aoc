import sys

def processPassport(passportLines):
  checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #leaving cid out, it is optional
  for check in checks:
    if (passportLines.count(check) == 0):
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
      print(passportLines)
      cntValidPassports += 1
    print(f"Valid Passports: {cntValidPassports}")

if __name__ == '__main__':
  countPassports('4.txt')