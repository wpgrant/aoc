import sys

with open('1.txt', 'r') as file:
  lines = file.readlines()

calsList = []
totCals = 0
for cal in lines:
  if cal.strip().isnumeric():
    totCals += int(cal)
  else:
    calsList.append(totCals)
    totCals = 0

calsList.sort(reverse=True)
topthree = calsList[0] + calsList[1] + calsList[2]
#print(calsList)
print(topthree)