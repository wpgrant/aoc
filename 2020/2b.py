import sys

with open('2.txt', 'r') as file:
	lines = file.readlines()

cntValid = 0
for str in lines:
  splitStr = str.split()
  firstPos = int(splitStr[0].split('-')[0])
  secondPos = int(splitStr[0].split('-')[1])
  char = splitStr[1].split(':')[0]
  password = splitStr[2]
  firstChar = True if password[firstPos-1] == char else False
  secondChar = True if password[secondPos-1] == char else False
  if (firstChar != secondChar):
    cntValid += 1

print(cntValid)