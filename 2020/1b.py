import sys

with open('1.txt', 'r') as file:
	lines = file.readlines()
for num1 in lines:
  for num2 in lines[1:]:
    for num3 in lines[2:]:
      if (int(num1) + int(num2) + int(num3) == 2020):
        print(int(num1) * int(num2) * int(num3))
        sys.exit(0)