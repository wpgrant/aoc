def processGroup(groupLines):
  groupList = []
  for char in groupLines:
    if char != '\n':
      groupList += char
  return len(set(groupList))

if __name__ == '__main__':
  with open('6.txt', 'r') as file:
    lines = file.readlines()
    groupLines = ""
    countAllGroups = 0
    for line in lines:
      if len(line.strip()) == 0:
        countAllGroups += processGroup(groupLines)
        groupLines = ""
      groupLines += line
    # Process last group
    countAllGroups += processGroup(groupLines)
    print(f'Count is {countAllGroups}')