import sys

with open('2.txt', 'r') as file:
	lines = file.readlines()

cntValid = 0
for str in lines:
  splitStr = str.split()
  lowRange = int(splitStr[0].split('-')[0])
  highRange = int(splitStr[0].split('-')[1])
  char = splitStr[1].split(':')[0]
  password = splitStr[2]
  cntChar = password.count(char)
  if ((cntChar >= lowRange) & (cntChar <= highRange)):
    cntValid += 1

print(cntValid)