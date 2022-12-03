import sys

with open('1.txt', 'r') as file:
  lines = file.readlines()

maxCals = 0
totCals = 0
for cal in lines:
  if cal.strip().isnumeric():
    totCals += int(cal)
    if (totCals > maxCals):
      maxCals = totCals
  else:
    totCals = 0

print(maxCals)
